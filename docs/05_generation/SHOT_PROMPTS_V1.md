# Grok / Image-to-Video 5×6초 샷 프롬프트 V1

> 사용 전 페이지폰 참조 이미지를 모든 샷의 reference로 제공. 본 프롬프트만으로 모델이 정확한 실물 디자인을 재현한다고 가정하지 않는다.
> 촬영 영상에 speech, captions, text, logo, music을 **bake-in 하지 않음**. 대사/VO/BGM은 post-production.

## 공통 잠금 프롬프트
**Photorealistic Korean industrial power-station workplace, grounded documentary cinema, natural human motion, realistic lighting, 16:9 widescreen, visual continuity. The EXACT SAME wall-mounted silver-gray IP PAGE PHONE from the reference, black-bordered upper 7-inch horizontal screen, pale handset on the left and coiled cord, small blue subdisplay and keypad with colored lower buttons, right-side equipment housing. No anthropomorphic eyes or mouth, no fake logos, no text overlays, no accident drama.**

## S01 0–6: 전화기 첫 등장
**Start frame:** static photoreal wide cinematic close-up of the reference page phone mounted on a generic industrial column. Metal textures, soft moody neutral light, clear keypad and handset. **Motion:** brief amber indicator pulse (no wild flashing) and slow 5% dolly inward after opening tone. Keep phone fixed, no warping or self-moving handset. **End frame:** tighter phone display/handset focus. **Sound:** separate page phone summon tone, recorded in post. AI notice later at lower right.

## S02 6–12: 익숙한 응답
**Start frame:** helmeted Korean plant worker with the same phone, realistic routine workplace background. **Motion:** three sharp but coherent micro-cuts of distinct workers in different adjacent zones, each picking up or speaking into identical model handset; avoid handset teleportation. **End frame:** return to stable page phone. **Note:** If model struggles with 3 montage cuts, generate three 2-sec segments or assemble from stills at edit instead.

## S03 12–18: 한 번 더 확인
**Start frame:** worker in proper PPE next to an *illustrative fictional* pipe valve/identification plate 21, no real station schematic or operational procedure. **Motion:** worker compares visual status with expectation, slight professional hesitation then speaks into reference-model handset. **End frame:** calm confident intent to verify, not fear. **Negative:** no valve manipulation, no alarm, no leak.

## S04 18–24: 리더의 응답
**Start frame:** calm experienced Korean team leader receiving identical page phone in a generic control room, no readable operating data. **Motion:** leader attentive, empathetic expression, short affirmative nod, then beginning to move to jointly verify. **End frame:** action transition toward plant work zone without spatial discontinuity. **Negative:** patronizing gesture, yelling, disaster setting.

## S05 24–30: 안전은 연결된 목소리
**Start frame:** field worker and leader stand together near fictional valve 21, visually verify side by side without touching. Reference IP page phone in foreground or nearby background, clean composition, balanced visual depth. **Motion:** slight dolly out into relaxed steady final hold with clear negative space for editorial 3-line message. **End frame:** text-safe, high-contrast, no generated text. Music resolves in post.

## 공통 QC
Phone geometry & position must remain stable in all shots; each clip length 6 seconds;
no fake subtitles or accidental generated signage; no unauthorized operational information;
same worker, leader, PPE across scenes; output file naming `S01_I2V_V01.mp4` .. `S05_I2V_V01.mp4`.
