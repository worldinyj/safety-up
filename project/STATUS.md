> **최신 지시 V3.4 (2026-10-26):** 음성·밸브 명칭에 관한 이 문서의 `A/알파` 내용은 **폐기**되었습니다. **화면 V11 (작은 명판), 한국어 대사 “브이십일 밸브 한 번 더 확인하겠습니다.”**가 현행 지시입니다. `docs/04_audio/AUDIO_CUESHEET_V34.md` 및 `production/audio_cues_v34.json`를 우선하여 읽으십시오. 화자·음성 시점도 V3.4가 우선합니다.

## Audio timing V3.4 — PRE-TTS
- 요청에 따라 **영상 속 인물 직접 대사 / 페이지폰 내레이션 / 효과음·BGM** 분리 및 한국어 30초 초안 타임라인 문서화.
- S03 작은 금속판 `V11`, 음성 `브이십일` 별도 지정; **표기/발음 상이함은 QC 항목**.
- S03 13.6–14.4 수화기 수취, 14.4–17.8 대사 발화. 기존 S03 15초 프레임이 수화기 없는 상태면 영상 원본 제작 전 조정 필수.
- 6초 클립별 30초 타임라인은 초안. ElevenLabs 녹음/음성 파일 길이 확인 전 `VOICE_QC_PENDING`.
- Grokbot은 모든 음성 한국어, 기본 영상은 무음 생성, 한국어 음성 별도 합성.

# SAFETY UP STATUS — 2026-10-26 / V3

- Repo: `worldinyj/safety-up`, branch `feat/pagephone-confession-v1`.
- Current creative direction: realistic cinematic **「페이지폰의 고백」**.
- User correction latest: **A (no hyphen/no number)** valve sign, spoken **알파**.
- Final picture: user's selected sunset coastal nuclear plant view + emphasized 3-line followership/leadership/nuclear safety culture copy.
- Cast: one female response beat in S02, male field worker in S03, male leader S04; consistent males appear S05a.
- S01 phone mounted inside; screen greeting; 0s call; bottom-right AI notice at both ends.
- 15-point storyboard: described in `FRAME_CONTINUITY_V3.md`.
- **VISUAL GEN STATUS:** existing 15-panel images are concept/previews only; **15 independent production-ready high-resolution frames not approved or synced**.
- Source phone JPEG and source end-card JPEG: conversation only, not GitHub.
- ElevenLabs/BGM/6s clip files/final MP4: **NOT CREATED**.
- Stage: before asset review; do not claim completed video or final lock.
- Next: transfer source references to local Grokbot; generate *separate* real image files 15; validate, share human approval; only then 6s I2V/voice/editorial.

## 2026-10-26 CI 품질보증 V3.1
- 공식 CI 자료: https://www.khnp.co.kr/main/contents.do?key=2238
- 신규 남성 A밸브 시안 및 기존 여성 S02 시안 모두 안전모/가슴패치 로고 형태의 정식 원본 적용·확대 검수 필요.
- 실사형 남성 시안 1장 별도 생성했으나, 실제 페이지폰 형상과 공식 CI 정합성 미완료로 **REWORK / NOT LOCKED**.
- 공개 저장소에는 실제 KHNP CI 바이너리와 사내 제공 원본 이미지를 업로드하지 않았음.
- 별도 QC ZIP `safety_up_khnp_ci_qc_v31.zip` 보관; Grokbot 로컬에 전달 후 CI 원본 합성 진행.
- 상태 `BRAND_QC_PENDING`, 다음 게이트는 공식 CI 파일 확보 및 200% 확대/6초 로고 추적 승인.

## Stage S01/S02 frame review 2026-10-26 / V3.2
- 6 independent 16:9 pixel exports (three for S01 and three for S02) collected into private review ZIP `safety_up_S01_S02_keyframes_REVIEW_V1.zip`. SHA256: `6a4b5e98b86f38773249ced973c119d2c8e3bfc1993e57a80d0a4732a7c6514c`.
- Note: existing generated source images resized to 1920×1080, some reframed. These are **candidates not native master production keyframes**.
- `docs/05_generation/FRAME_REVIEW_S01_S02_V32.md` and `production/frame_review_s01_s02_v32.json` are current handoff docs; update after director review.
- S01 phone geometry across start/mid/end not fully consistent; `PHONE_GEOMETRY_QC_PENDING`. S02 one female mini-shot present; `BRAND_QC_PENDING` still applies.
- No paid 6-second video generation until approval. **Next image stage S03 only after director chooses approve or revision.**

## Stage S03 프레임 검토 2026-10-26 / V3.3
- S03(12–18초) A 밸브 → 동일 남성 작업자 → 페이지폰 통화, 3장 검토용 이미지를 별도 ZIP으로 생성.
- ZIP: `safety_up_S03_keyframes_REVIEW_V1.zip` SHA256 `6f6c7b0d36ef45956d0f97ce4b278445d81ec745f49e9a55265301bbab08837e`, 공개 GitHub 미업로드.
- **S02 수화기 두 개 오류**: 최종 컷 후보를 `S02_F03_END_CORRECTED_V2.png`로 대체, 빈 거치대 및 수화기 1개 원칙.
- S03 세 장은 기존 단독 실사 원본에서 각기 다른 크롭으로 구성. **네이티브 FHD 독립 생성 마스터가 아니므로 REVIEW_PENDING, MOTION_QC_PENDING**.
- 이번 단계 완료 후 감독 검토가 이어지면 다음 S04 이미지 제작. 영상 생성 및 S05 최종 승인 아직 없음.
