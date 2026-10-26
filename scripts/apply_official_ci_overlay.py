#!/usr/bin/env python3
"""Project authentic transparent KHNP PNG on human-approved frame quadrilaterals.

Example:
 python scripts/apply_official_ci_overlay.py --image input.png --official-ci assets/brand/KHNP_OFFICIAL_SIGNATURE.png --placement placements_approved.json --output output.png

This is a basic post-production utility: geometry and rights must be manually verified.
"""
import argparse, hashlib, json, sys
from pathlib import Path
import cv2
import numpy as np

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as file:
        for part in iter(lambda:file.read(1048576),b""):h.update(part)
    return h.hexdigest()

def run():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--image",required=True)
    p.add_argument("--official-ci",required=True)
    p.add_argument("--placement",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    config=json.loads(Path(a.placement).read_text(encoding="utf-8"))
    if config.get("human_approved") is not True:
        sys.exit("BLOCKED: a human must approve precise placement quadrilaterals")
    frame=cv2.imread(a.image,cv2.IMREAD_COLOR)
    logo=cv2.imread(a.official_ci,cv2.IMREAD_UNCHANGED)
    if frame is None or logo is None:
        sys.exit("BLOCKED: missing input image or authorized official CI PNG")
    if len(logo.shape)!=3 or logo.shape[2]!=4 or np.min(logo[:,:,3])==255:
        sys.exit("BLOCKED: official CI must be a PNG with transparency (alpha channel)")
    h,w=frame.shape[:2];lh,lw=logo.shape[:2]
    src=np.float32([[0,0],[lw-1,0],[lw-1,lh-1],[0,lh-1]])
    for item in config["placements"]:
        dst=np.float32(item["quad"])
        if dst.shape!=(4,2) or np.any(dst[:,0]<0) or np.any(dst[:,1]<0) or np.any(dst[:,0]>=w) or np.any(dst[:,1]>=h):
            sys.exit("BLOCKED: invalid placement quadrilateral")
        transform=cv2.getPerspectiveTransform(src,dst)
        projected=cv2.warpPerspective(logo,transform,(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_CONSTANT,borderValue=(0,0,0,0))
        alpha=projected[:,:,3:4].astype(np.float32)/255.0
        frame=np.clip(frame.astype(np.float32)*(1-alpha)+projected[:,:,:3].astype(np.float32)*alpha,0,255).astype(np.uint8)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    if not cv2.imwrite(a.output,frame):sys.exit("BLOCKED: failed to write output")
    audit={"input":a.image,"input_sha256":sha256(a.image),"official_ci":a.official_ci,"official_ci_sha256":sha256(a.official_ci),"output_sha256":sha256(a.output),"qc_status":"PENDING_HUMAN_VISUAL_REVIEW"}
    Path(a.output+".provenance.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(audit,ensure_ascii=False,indent=2))
if __name__=="__main__":run()
