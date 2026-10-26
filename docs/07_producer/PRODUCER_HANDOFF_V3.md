# GROKBOT PRODUCER MASTER HANDOFF — V3 CURRENT
**Repository:** https://github.com/worldinyj/safety-up  
**Branch:** `feat/pagephone-confession-v1`  
**Human authority:** operator/director. **No unsolicited paid generations or final publishing.**

## First objective
Make **15 separate genuine high-detail 16:9 stills** for director QC: each of 5 × 6s video slots gets start/mid/end. Do NOT use the AI-generated 15-grid concept art or enlargements of its crops as production input. After frames get approved, generate minimal 6-sec clips / edit microcuts.

### Read in order
`README.md`, `docs/02_storyboard/STORYBOARD_30S_V3.md`,
`docs/03_visual/VISUAL_BIBLE_V3.md`,
`docs/03_visual/FRAME_CONTINUITY_V3.md`,
`docs/04_audio/AUDIO_PLAN_V3.md`,
`docs/05_generation/SHOT_PROMPTS_V3.md`,
`docs/06_review/QC_GATES_V3.md`,
`production/shot_manifest_v3.json`.

### Creative locks (exact)
1. Phone source PHOTO_REF = `IMG_9556.jpeg`, wall-mounted gray IP PAGE PHONE, **inside** plant.
2. Intro display **“안녕하세요. 전 페이지폰입니다.”**, editorial text overlay not model hallucination.
3. S02 male/female/male fast response. Female only one beat.
4. S03 same **male field worker A** in 3 frames, no female swap; ID label exactly **A** (NOT `-A`, NOT `21`). Spoken **“알파 밸브 한 번 더 확인하겠습니다.”**
5. S04 **male leader B**, response exactly **“오케이. 작업 잠시 멈추고 같이 확인합시다”**.
6. Phone narrator exactly **“바로 이런 순간이죠. 안전문화는, 연결된 목소리에서 시작됩니다.”**
7. S05a indoors two men jointly check **A** valve. At ~27s a **normal edit cut** to sunset nuclear coastal exterior **end title card** following END_REF `IMG_9558.jpeg`.
8. End exactly: **멈춰 말하는 팔로우십 / 귀 기울이는 리더십 / 그것이 원자력안전문화입니다.**
9. **Calling tone before narration**, beginning and end production disclosure **“본 영상은 AI를 활용하여 제작되었습니다.”**.
10. Video format 30s 16:9 1920×1080 FHD MP4 <500MB.

### Specialized subteams
- Investigator: source reference hashes, publicity rights and non-specific generic fictional setting verification.
- Writer: read script, TTS duration test; preserve locked Korean sentences, ensure time.
- Visual Director: establish PHONE / CAST A / CAST B / CAST F masters with shot consistency.
- Shot Director within Visual: story continuity and 15 independent keyframes. S02 uses 3 separate ~2s mini-clips; S05 transitions via editorial cut, never morph.
- Audio/Editor: 0-sec pagephone tone, separate ElevenLabs voices, gentle instrumental BGM from appropriately licensed/verified Google music tool, editorial Korean subtitles + intro/outro notices.
- QC: all 15 images, cross-shot identity, text accuracy, audio, format, source rights, SHA256 before release.
- Producer: deliver completed asset table, screenshot index, SHA, exact model/settings/cost, blockers, next **specific approval request**.

### Critical dependency
**GitHub holds instructions, not binary source photos.** The user previously uploaded both photos in ChatGPT; Grokbot cannot read them from this repo until the operator supplies copies after publicity review. If unavailable, report BLOCKED and do not invent alternative device/end-card.

### STOP conditions
Ref image missing, fake device, wrong A label/pronunciation, woman as protagonist, outdoor pagephone, new payment or batch video call without approval, copyright/security uncertainty. Do not merge to `main` without review.

### Artifact naming
`assets/frames_v3/S01_F01_START.png` ... `S05_F03_END.png`, `production/shot_manifest_v3.json`, `logs/QC_V3.md`, each with SHA256/status/human decision. **NO `LOCKED` status based on collage crop.**


## V3 미디어 로컬 인계 체크 (2026-10-26 추가)
- 반드시 `production/assets_manifest_v3.json` 및 `docs/09_assets/MEDIA_HANDOFF_V3.md`를 함께 읽는다.
- ChatGPT 첨부 미디어 패키지 `safety_up_grokbot_media_handoff_v3.zip`을 로컬 저장소에 해제한 후 `python3 scripts/verify_media_v3.py` 검증에서 PASS가 나와야 참조 이미지를 기반으로 고화질 키프레임을 제작할 수 있다.
- 이 ZIP의 SHA256은 `f19f1ae4d8e7413392559337b437dc1cd94042aea9d6928ec1f7516c1f40e21d`. **공개 GitHub 저장소에는 해당 바이너리가 없으며**, Grokbot Cloud에는 자동 전달되지 않는다.
- ZIP에 포함된 15장의 `*_PREVIS_V3.jpg`는 1920×1080로 업스케일되었지만 출처는 작은 보드 컷이다. **별도 네이티브 FHD 키프레임 15장 승인 전 영상 생성 금지**.
- 감독에게 30초 무음 애니매틱 `safety_up_30sec_animatic_previs_v3.mp4`(720p, 타이밍 점검용)를 별도 제공할 수 있으나, 영상 원본 또는 납품본으로 등록하지 않는다.
