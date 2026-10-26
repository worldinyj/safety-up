> **최신 지시 V3.4 (2026-10-26):** 음성·밸브 명칭에 관한 이 문서의 `A/알파` 내용은 **폐기**되었습니다. **화면 V11 (작은 명판), 한국어 대사 “브이십일 밸브 한 번 더 확인하겠습니다.”**가 현행 지시입니다. `docs/04_audio/AUDIO_CUESHEET_V34.md` 및 `production/audio_cues_v34.json`를 우선하여 읽으십시오. 화자·음성 시점도 V3.4가 우선합니다.

## 최상위 한국어 음성 제작 지시 V3.4
- `docs/04_audio/AUDIO_CUESHEET_V34.md`, `docs/05_generation/KOREAN_VIDEO_PROMPTS_V34.md`, `production/audio_cues_v34.json`를 가장 먼저 읽을 것.
- **영상 모델 임의 영어 음성/영어 나레이션/애드리브 금지**. 가능하면 무음 I2V 출력. 말하는 인물의 입 모양은 한국어 ElevenLabs 실제 녹음 후 별도 싱크.
- 페이지폰 내레이션은 사람의 입이 움직이는 대사가 아니다. S04에서 22초 이후 리더의 입 움직임 중단.
- S03 12~13.6초 점검, 13.6~14.4초 수화기 들어 귀에 대기, 14.4~17.8초 **“브이십일 밸브 한 번 더 확인하겠습니다.”**. 패널 태그 **작게 `V11`**. 표기/발음 불일치 감독 검수 필요.
- 인물/페이지폰/로고 영상 품질 게이트는 기존과 동일. 이전 `A/알파` 지시를 생성에 사용하지 말 것.

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


## V3.1 KHNP 공식 CI 필수 중간 게이트 (2026-10-26 추가)
- **임의 AI 생성 녹색 마크/KHNP 유사 로고를 공식 CI로 간주하지 말 것.** 안전모와 가슴 패치 모두 원형 심볼·사선·청색 KHNP 글자의 비례 일치 확인.
- 읽을 파일: `docs/03_visual/KHNP_CI_QC_V31.md`, `production/ci_placements_TEMPLATE_v31.json`, `scripts/apply_official_ci_overlay.py`.
- **공식 다운로드 출처:** https://www.khnp.co.kr/main/contents.do?key=2238. PNG/AI 다운로드 가능; 실제 공식 원본과 브랜드·사용권 규정을 승인받은 후 로컬 `assets/brand/KHNP_OFFICIAL_SIGNATURE.png`에 보관. 반드시 SHA256 기록.
- 15개 이미지 생성 시에는 가능하면 **깨끗한 무로고 안전모/가슴 패치**로 먼저 작업. 이후 공식 CI를 마스킹/트래킹해서 합성. 공식 로고 원본이 확보되지 않았다면 `BRAND_QC_PENDING`으로 유지.
- 새 로컬 검수 패키지 `safety_up_khnp_ci_qc_v31.zip`은 채팅에서 별도 전달받는 비공개 자산. GitHub에는 해당 바이너리를 업로드하지 않음.
- 최종 이미지 QA는 **헬멧/가슴패치 200% 확대** + **6초 움직임 시 원근/크기 안정성** + 브랜드·권리 확인을 포함.
- 페이지폰 원본 형태 준수, S02 여성 한 꼭지, A 밸브(알파) 및 S05 석양 엔딩은 기존 V3 LOCK대로 유지.

## S01/S02 stage review note (V3.2)
Before image-to-video generation, read `docs/05_generation/FRAME_REVIEW_S01_S02_V32.md` and `production/frame_review_s01_s02_v32.json`. Retrieve private `safety_up_S01_S02_keyframes_REVIEW_V1.zip` via operator if available. It contains six **preview candidates**, not native FHD masters. Mark S01 phone design and official KHNP CI as pending; respect human review before S03 or I2V.

## Stage S03 V3.3 editorial anchors and S02 phone-physics correction
- Read `docs/05_generation/FRAME_REVIEW_S03_V33.md` and `production/frame_review_s03_v33.json`.
- Private handoff ZIP: `safety_up_S03_keyframes_REVIEW_V1.zip`, SHA256 `6f6c7b0d36ef45956d0f97ce4b278445d81ec745f49e9a55265301bbab08837e` (not in public repo).
- Three 1920x1080 S03 candidate frames are **three editorial crops from ONE previously generated scene**; don't mark as individual independently generated FHD masters.
- Replace defective S02 last frame showing duplicate handset with `S02_F03_END_CORRECTED_V2.png`. Physically one telephone receiver per device, wall cradle empty while worker holds it.
- S03 spoken `알파 밸브 한 번 더 확인하겠습니다.`, sign `A`. Review before S04; do not batch I2V before approval.

## S04 frame review V3.5 — do not mistake generated 6-panel storyboard for I2V master
- Open `docs/05_generation/FRAME_REVIEW_S04_V35.md` and `production/frame_review_s04_v35.json`.
- Private ZIP `safety_up_S04_keyframes_REVIEW_V1.zip` (SHA256 `d5d9e86d553f4e9b0515ff00c23227a40f8d8d79ddcfc2f44454692c33814c3d`), **not in GitHub**.
- Three S04 review PNGs are re-framed versions of one 1672x941 face master, NOT three independently generated FHD masters. Original device match is **FAIL/PENDING**, as handset is dark grey not ivory.
- 18–21.9s Korean male-leader line exact, 22–23.9s Korean PAGEPHONE VO exact; leader closes mouth during pagephone VO. Use user-approved real device reference to regenerate/refine before LOCK.

## Latest S05 image review V3.6: high priority correction
- Read `docs/05_generation/FRAME_REVIEW_S05_V36.md` and `production/frame_review_s05_v36.json` prior to any S05 I2V.
- Local ZIP `safety_up_S05_keyframes_REVIEW_V1.zip` SHA256 `4cfcc751ebbc66565c6a5ac6c049d6c4d9ee1578e0d534e809032518cb6a0bad` is not in public GitHub.
- **24–27s**: two MEN in same indoor plant, jointly visually verify exact SAME V11 valve as S03. This supplied indoor STILL is a low-detail crop from a storyboard, **not production-ready**. S03 red handwheel/gray valve/blue flange/yellow ring must match across sequence.
- **27–30s**: cut to operator-approved `IMG_9558.jpeg` sunset card. End exact 3-line title and AI notice. Do NOT synthesize outdoor phone or spatial morph.
- S05 audio **pagephone Korean voiceover ONLY**, no worker speaking. Voice may continue to 27.5s. Human approval needed for final video.
