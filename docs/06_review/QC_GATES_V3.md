# QUALITY GATES V3

| Gate | Current state | Acceptance |
|---|---|---|
| G0 Brief | RECORDED | 30.000s / FHD / MP4 / <=500MB / AI notice both ends |
| G1 Storyboard V3 | WRITTEN | 5×6s, phone greeting, S02 woman one beat, S03 male A, S04 male B, A valve and '알파' |
| G2 Device reference | REFERENCE PRESENT IN CHAT ONLY | actual IP PAGE PHONE geometry, same model all relevant frames; security/publication checked |
| G3 15 individual frames | **NOT LOCKED** | start/mid/end ×5 as separate original photos, real 16:9 usable details, identical actors/phone, safe fictional scene |
| G4 Clip motion | NOT STARTED | reasonable 6s movements; no AI morph between S02 employees or S05 location change |
| G5 Audio | NOT STARTED | call tone first, ElevenLabs exact Korean, **'알파'** not ‘대시 알파’, clean mix |
| G6 Composite | NOT STARTED | S05a indoor / S05b 3s sunset end card, text legible, AI notice both ends |
| G7 Submission QC | NOT STARTED | 1920×1080 / 30fps / 30s / MP4 / <500MB, sound, AI tools named |
| G8 Human accepted | NOT AUTHORIZED | rights/privacy/trademarks, specific station absence, director full playback approval |

**Rejection triggers:** '21', '-A', '대시 알파'; S03 male turns into female; S05 outdoor phone; ending not sunset coast scene; false official pagephone UI claim; label/text distorted; generated storyboard crop used as I2V high-resolution master; absent start/end AI notice; overlong TTS.

**Draft preview status:** 15 frames can be exported from a concept-sheet purely as **visual inspection thumbnails**, but are never `LOCKED` master. Grokbot must generate independent FHD scene stills from original approved phone and end-card references. All rights & privacy must be evaluated before public-Repo image upload.

```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,r_frame_rate -of json deliverables/SAFETY_UP_PAGEPHONE_FINAL_V01.mp4
shasum -a 256 deliverables/SAFETY_UP_PAGEPHONE_FINAL_V01.mp4
```


## CI 게이트 V3.1 (G3 이전 필수)
- 공식 KHNP CI 참조: https://www.khnp.co.kr/main/contents.do?key=2238
- 안전모/작업복 패치에 쓰이는 AI 생성 로고는 공식 원본이 아닐 수 있으므로 `BRAND_QC_PENDING`.
- `docs/03_visual/KHNP_CI_QC_V31.md`의 CI01–CI06 전 항목을 통과하기 전에는 고화질 키프레임을 `LOCKED`로 변경하지 않는다.
- 공식 투명 PNG 사용 및 SHA256 기록, 바닥 이미지의 잘못된 로고 제거, 위치/곡률/트래킹/가림 검수, 법무·브랜드 사용권 확인.
- 제공되는 `safety_up_khnp_ci_qc_v31.zip`은 로컬용 확대 검수표와 시안 2장으로, **공식 CI 파일을 포함하지 않는다**.
