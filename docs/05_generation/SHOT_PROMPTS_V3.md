# GROK IMAGE-TO-VIDEO PROMPT PACK V3

## 준비
- GitHub `feat/pagephone-confession-v1`에서 **V3 문서만** 읽고 기존 V2의 ‘21번/-A/대시 알파’ 잔여 지시 사용 금지.
- PHONE_REF=`IMG_9556.jpeg` 실제 페이지폰 사진(별도 인계).
- END_REF=`IMG_9558.jpeg` 감독 승인 일몰 엔딩 구도(별도 인계).
- 남성 A / 여성 F / 남성 리더 B **캐릭터 ID 마스터를 먼저 승인**, PAGEPHONE 실물 구조 먼저 고정.
- 각 샷 시작/중간/끝 프레임이 `docs/03_visual/FRAME_CONTINUITY_V3.md`의 15개 명세를 정확히 따르도록 준비.
- **프레임 이미지의 한 장면에 시간표/그리드/제목/설명 텍스트를 굽지 말 것**. 생성된 콜라주 잘라서 확대하는 방식은 최종 프레임 승인이 불가능.

## Shared positive prompt
Photorealistic cinematic Korean industrial plant safety training film, consistent silver-gray industrial wall-mounted IP PAGE PHONE from reference, believable adult workers, documentary-style restrained facial expressions, tasteful neutral/warm lighting, physically plausible equipment, one continuous location within each single shot, 16:9 landscape. Worksite is generic fictional interior (not real station). Realistic protective equipment and handset grip, consistent background pipework and lighting. No generated dialog, subtitles, logos, or invented operating data. **Valve plate reads only A, no dash or numbers**.

## S01 (0-6s)
Three keyframes: wider view of fixed phone → gentle push-in → close-up same phone. Keep same perspective, phone display blank or clean for editor to overlay **“안녕하세요. 전 페이지폰입니다.”**. Pagephone paging tone at 0s created separately. No emergency strobe.

## S02 (6-12s)
Distinct three mini-shots, ~2s each: male employee answering phone → female employee saying 확인했습니다 → a different male employee answering. **Hard edits, not AI human morphing**. All use same model phone and believable navy PPE.

## S03 (12-18s)
Male worker A walks/looks toward valve with **A** mark → pauses to check visually → holds same phone handset and speaks. Keep male identity unchanged for all frames; he says **“알파 밸브 한 번 더 확인하겠습니다.”** in post. Never rotate valve or show hazardous manipulation. Mount the same phone inside nearby pipe gallery.

## S04 (18-24s)
Leader B in generic control room receives pagephone → attentive nod → prepares to join worker. His Korean exact line added with ElevenLabs: **“오케이. 작업 잠시 멈추고 같이 확인합시다”**. Ends with short pagephone VO “바로 이런 순간이죠.”. Does not teleport to site within same morph.

## S05 (24-30s, editor composite)
24–27s: Worker A and leader B stand together in same indoor pipe gallery by **A** valve and visually inspect. Phone may be seen on interior wall. At ~27s: **hard cut or clean dissolve** to static FHD sunset nuclear-station end card based on user reference. 27–30s hold 3-line closing text with blue highlights, AI creation notice at lower right. **Never let I2V morph the people or indoor phone into coastline.** Use separate 3s action source and 3s graphic.

## Negative
21, 21-A, -A, dash alpha, exterior wall-mounted page phone, woman replacing male A, woman replacing male leader B, extra hands, different phone, CGI plastic, disaster film, hallucinated station logos, readable process screen, illegal use of work permits, illegible on-image Korean text.

## Delivery and approval
For each slot: `S0X_F01_START.png`, `S0X_F02_MID.png`, `S0X_F03_END.png`, model/settings/reference SHA, human QC. Before any 6s video generation, verify each individual keyframe is its **own 16:9 photo with usable detail**, not storyboard screenshot.
Generate 6s I2V only after human approval; then audio in separate mix, final FHD MP4 QC.
