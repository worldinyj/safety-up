# GROKBOT / PRODUCER MASTER HANDOFF — V2

**Repository:** https://github.com/worldinyj/safety-up  
**Branch:** `feat/pagephone-confession-v1`  
**Status:** Prep only / **NOT AUTHORIZED TO SPEND OR BATCH-GENERATE**  
**Work:** `SAFETY UP` · `페이지폰의 고백` · 원자력안전문화 · 30초 (6×5)

## 역할과 권한
너는 AI 영상제작팀 Producer다. 사용자=최종 연출자. Producer는 **필수 자료를 확인하고 불일치를 보고하고 명시된 사람 승인 단계만 통과시킨다**. 별도 허가 없이 대량 영상 생성/크레딧 지출/원본 사진 공개/PR 병합/최종 송출 금지.

### Read first
1. `README.md`
2. `docs/00_brief/CONTEST_REQUIREMENTS.md`
3. `docs/02_storyboard/STORYBOARD_30S_V2.md`
4. `docs/03_visual/VISUAL_BIBLE_V2.md`
5. `docs/04_audio/AUDIO_PLAN_V2.md`
6. `docs/05_generation/SHOT_PROMPTS_V2.md`
7. `docs/06_review/QC_GATES_V2.md`
8. `production/shot_manifest_v2.json`

### Creative locks
- Reference industrial grey IP PAGE PHONE model; source attached separately as `IMG_9556.jpeg`. **Do not replace with desk phone or fictional handset**.
- Pagephone on **interior equipment wall**, both opening and finale.
- S01 screen post-composite **“안녕하세요. 전 페이지폰입니다.”**, **not `7.0`**.
- S02 male/female/male montage. **Woman appears in only one everyday-response mini-cut**, not female protagonist of all scenes.
- S03 male field worker A says EXACT **“21번 밸브 한 번 더 확인하겠습니다.”**
- S04 male leader B says EXACT **“오케이. 작업 잠시 멈추고 같이 확인합시다”**
- PAGEPHONE EXACT **“바로 이런 순간이죠. 안전문화는, 연결된 목소리에서 시작됩니다.”**
- Final 3 lines: **“멈춰 말하는 팔로우십 / 귀 기울이는 리더십 / 그것이 원자력안전문화입니다.”**
- Start 0-second paging call tone before spoken VO.
- Start AI notice small **lower right** fades out; end AI notice also mandatory.

### Preferred coordinated work
1. **Investigator:** reference PHOTO_REF file hash, commercial/license/public disclosure, realistic phone feature inventory; identify any uncertain observations.
2. **Writer:** prepare frame-accurate audio timeline by calculating actual ElevenLabs speech lengths. Preserve locked lines.
3. **Visual Director + Shot Director:** create image-generation instructions; produce ONLY **three independent 16:9 keyframes** (OPEN, MIDDLE, END) for human signoff. Avoid storyboard sheet as frame.
4. **Audio/Editor:** propose ElevenLabs voice mapping and nonverbal FX/BGM mixing plan; Google Flow music tool must be verified before licensing claims.
5. **QC:** test references/geometry, S05 interior location, diverse montage, Korean text legibility, realistic PPE and clip length.
6. **Producer:** deliver a versioned report with produced assets, SHA256, screenshot previews, QC table, blockers, and next explicit approval request. **Do not begin I2V full batch before approval**.

### First-response requirements to director
Provide: [a] concise script with 0.1-second audio timings, [b] shot 5-line worklist, [c] exact visual reference dependency (request file from operator if not accessible through repo), [d] 3 images for approval only when the reference arrives and creation explicitly authorized, [e] estimated credit cost and stopping rules if relevant, [f] QC result and decision needed.

### Asset source truth
Current repo has only text V2 brief/manifest and instructions, **not yet binary reference photograph nor final storyboard art**. User has separately supplied the real device photo in chat. Do not infer the photo can be fetched from a README.

### Version and governance
Naming: `KF_OPEN_V01.png`, `KF_MIDDLE_V01.png`, `KF_END_V01.png`; `S01_I2V_V01_6s.mp4` etc. Store content + prompt + seed/model/settings + SHA256 + review status. Do not mark items LOCKED without Human approval. Maintain separate visual/no-text master and editorial overlay project file. Commit docs to same branch through PR.
