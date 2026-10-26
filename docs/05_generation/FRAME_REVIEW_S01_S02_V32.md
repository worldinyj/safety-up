# S01 / S02 independent-frame review package — V3.2

**Date:** 2026-10-26 (KST)  
**Branch:** `feat/pagephone-confession-v1`  
**Status:** `REVIEW_PENDING`; **NO frame `LOCKED`**.  
**Human-requested workflow:** Review one 6-sec clip before proceeding to next. S01 and S02 image proposals are gathered; do **not** generate S03 images until explicit director approval of this set.

## Images and intended timeline

| ID | Timestamp | Composition | Critical QC |
|---|---:|---|---|
| S01_F01_START | 00:00 | Inside pipe/equipment gallery, gray wall-mounted IP PAGE PHONE with greeting | Call-tone starts before speech; greeting exact on display as post overlay |
| S01_F02_MID | 00:03 | Slow push-in toward same phone | Front buttons, handset, right auxiliary housing must **match first frame** |
| S01_F03_END | 00:06 | Same phone, worker shoulder enters foreground at left | Camera direction and hardware match; cut to S02 worker |
| S02_F01_START | 00:06 | Male employee takes/holds pagephone handset | Dialogue: “네, 알겠습니다.”; 2-sec independent micro-cut |
| S02_F02_MID | 00:09 | **One female employee** holds handset | Dialogue: “확인했습니다.”; 2-sec independent micro-cut |
| S02_F03_END | 00:12 | Male employee finishes routine call | Dialogue: “진행하겠습니다.”; cut to S03 alpha-valve inspection |

## Asset provenance and handoff
- ChatGPT conversation ZIP: `safety_up_S01_S02_keyframes_REVIEW_V1.zip`.
- ZIP SHA256: `6a4b5e98b86f38773249ced973c119d2c8e3bfc1993e57a80d0a4732a7c6514c`.
- Inside ZIP: `frames/S01_F01_START.png` … `frames/S02_F03_END.png`, `CONTACT_SHEET_S01_S02_V1.jpg`, `FRAME_MANIFEST_S01_S02.json`, `DIRECTOR_REVIEW.md`.
- All PNGs are 1920×1080 pixel exports; **they derive from previously generated 1672×941 images and crops, NOT independent native FHD masters**.
- **No image binary stored in public GitHub**; this text is an exact reference to a separately downloadable local package.
- Grokbot local handoff: Download ZIP from the conversation; `unzip -o ~/Downloads/safety_up_S01_S02_keyframes_REVIEW_V1.zip -d assets/stage_S01_S02`. Verify archive SHA before use.

## Unresolved blockers
1. S01 generated first/mid/last differ slightly in keypad and phone geometry. **Must be corrected from user's actual PHONE_REF IMG_9556.jpeg** before I2V acceptance; never run unreviewed mismatched device stills as an interpolated 6-second shot.
2. S02 images are **reframed existing photos**, not a new visually locked model; ensure the screen doesn't show “7.0” or any superseded `21` label in rendered output.
3. All visible KHNP logos are AI approximations. Official CI transparent asset post-compositing and helmet/chest patch tracking still **BRAND_QC_PENDING**.
4. If user chooses to reject or alter S01/S02, regenerate only affected assets; preserve SHA/provenance of revised versions.

## Keep prior creative LOCK
- S03 valve identifier `A`, spoken **“알파 밸브 한 번 더 확인하겠습니다.”**
- S04 leader: **“오케이. 작업 잠시 멈추고 같이 확인합시다”**.
- S05 last 27–30 seconds: user's chosen sunset NPP endcard, with 3-line `팔로우십 / 리더십 / 원자력안전문화` slogan.
- Notice at video beginning and end indicating AI-generated content.
