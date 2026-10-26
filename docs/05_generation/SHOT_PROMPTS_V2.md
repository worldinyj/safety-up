# Grok I2V Prompt Pack V2 — 5 × 6s

## Global asset IDs
- `PHONE_REF` = 사용자 업로드 `IMG_9556.jpeg`에서 제품만 크롭하고 모아레·배경 UI를 제거한 승인 reference 이미지.
- `CHAR_A` = 남성 작업자(장면 03,05).
- `CHAR_F` = 여성 작업자(장면 02 단일 몽타주 컷).
- `CHAR_B` = 남성 리더(장면 04,05).
- `SPACE_PIPE` = 일반 산업시설 **실내** 배관/밸브.
- `SPACE_CTRL` = 가상 제어실.

## Mandatory shared prompt
Photorealistic cinematic corporate safety short, believable Korean power plant workers in a fictional generic indoor industrial facility, natural camera movement, grounded documentary atmosphere, realistic materials and worker PPE, consistent characters and props, landscape 16:9. Keep the exact same industrial IP PAGE PHONE device design from PHOTO_REF: rectangular grey wall-mounted metal chassis, black-framed 7-inch upper display, pale telephone handset and long coiled cord on front left, small blue sub-display and dense keypad with green/red/blue buttons below, narrow adjacent grey accessory housing. Do not move the phone to an outdoor wall. Do not animate face parts on the device. No video-generated lettering, subtitles, logos, or voice. Audio/text added in post.

### Shot S01 — "Pagephone Speaks"
**Start frame:** PHONE_REF on metal support column INSIDE large pipe/valve gallery, soft industrial lights, front three-quarter view. **6-second movement:** extremely subtle dolly-in and reflections; light phone call signal without emergency siren red beacon. No person visible. Device display blank during generation; post comp exact Korean greeting `안녕하세요.\n전 페이지폰입니다.`. **End frame:** tighter view readable screen, no distortions. **Sound post:** real-like call tone then narrator. **Keyframe priority:** KF-OPEN.

### Shot S02 — "Yes, Understood"
**Start frame:** male extra holding pale handset inside plant. **6-second movement:** montage edit of 3 short beats; male extra, **one female extra** wearing hardhat and safety glasses, male extra, each with matching phone and believable mouth movement. Prefer separate closeups 2s each edited rather than forcing morphing within one model run. No change in female proportion to dominant protagonist. **End frame:** third male extra with phone. **Sound post:** short spoken responses and pagephone voice.

### Shot S03 — "Check Valve 21"
**Start frame:** CHAR_A in SPACE_PIPE near fictional tag `21`, with PHONE_REF visible in same space. **6-second movement:** gaze from valve to handset, confident questioning/reconfirmation, clean hand movements; do not rotate the valve or simulate operational action. Number plate `21` composited/verified separately, not trusted to video model. **End frame:** CHAR_A speaking over handset calmly. **Keyframe priority:** KF-MIDDLE.

### Shot S04 — "Leader Receives"
**Start frame:** CHAR_B in SPACE_CTRL, accepting call on PHONE_REF-matching handset. **6-second movement:** receptive nod, clear listening and calm affirmative response, hint of getting ready to join staff. No operator-screen sensitive details, no accident visualization. **End frame:** leader puts focus on colleague/screen and moves to leave. **Sound post:** exact leader line and pagephone short bridge narration.

### Shot S05 — "Together"
**Start frame:** same CHAR_A + CHAR_B in SPACE_PIPE; both inspect a fictional valve 21 together at safe distance while same phone model appears mounted on an interior equipment wall behind them. **6-second movement:** slight side tracking → steady hold; calm collaborative expressions. **End frame:** interior wall equipment/handset still recognizable; leave negative space for clear 3-line end copy. **NEVER:** outdoor phone, sunset/nuclear reactor skyline, fake disaster. **Keyframe priority:** KF-END.

## Common NEGATIVE PROMPT
deformed handset, extra cord, extra phone buttons, impossible screen shape, change of prop model, outdoor phone, coastline, sunset, exterior plant dome, cartoon, anime, LEGO, visible animated mouth on hardware, hallucinated Korean text, fake operational displays, incorrect PPE, swapped faces, duplicated hands, rotating valve, crisis alarm, explosion, generated soundtrack, generated captions.

## Delivery naming
`S01_I2V_V01_6s.mp4` through `S05_I2V_V01_6s.mp4`.
Alongside every clip: prompt text + negative + reference file hashes + seed/model/settings + visual continuity check + output SHA256 + user QC verdict.
