# 페이지폰의 고백 — 샌드아트 독립 제작본

> **현재 상태 (2026-10-26): S01 V3 이미지 조건부 검토 통과, S02 V1 프리비즈 8장 생성 후 통합 QC FAIL — 독립 HD 재생성 필요.** S01·S02 I2V/한국어 음원/최종 승인 전, S03–S05 미제작.

이 폴더는 원자력안전문화 공모전용 **〈페이지폰의 고백〉 30초 샌드아트 영상**의 독립 작업 공간입니다. 별도 저장소가 아니라 `worldinyj/safety-up`의 별도 폴더이며, 작업 브랜치는 `feat/pagephone-sandart-v1`입니다.

## 기존 실사판과의 격리

- 기존 실사 작업 브랜치: `feat/pagephone-confession-v1`. 이 브랜치/기존 `docs/`, `production/`, `project/` 파일은 **수정하지 않습니다**.
- 이 버전의 모든 신규 문서·메타데이터·씬별 산출물 경로: `projects/pagephone-sandart/` 내부만 허용합니다.
- 원작 스토리와 2026-10-26 한국어 음성 V3.4는 **서사 기준**으로 계승하되, 시각 스타일 및 독립 자산/승인 이력은 **별도로 관리**합니다. 샌드아트 전환은 기존 실사 프레임의 최종 승인/LOCK을 승계하지 않습니다.
- 기본 브랜치 `main`에는 아직 병합하지 않았습니다.

## 작품 사양

| 항목 | 기준 |
|---|---|
| 제목 | 페이지폰의 고백 |
| 러닝타임 | 30.000초 (S01–S05, 각각 6초) |
| 규격 | 16:9 / 편집 마스터 1920×1080 / 30fps / MP4 |
| 스타일 | 실사 대신 모래판 위에 펼쳐지는 따뜻한 세피아 샌드아트 |
| 음성 | **한국어만**. 페이지폰은 오프스크린 내레이션, 인물은 직접 대사 |
| 공모전 고지 | 0.5–2.5초 및 28–30초 우하단 '본 영상은 AI를 활용하여 제작되었습니다.' |
| 최종 문구 | 멈춰 말하는 팔로우십 / 귀 기울이는 리더십 / 그것이 원자력안전문화입니다. |

## 디렉터 승인 게이트

1. 스토리보드·오디오 타임라인 확인.
2. 각 씬 **0 / 3 / 6초** 이미지 3장(필요 시 브리지 포함) 제작, 검수.
3. 사람 감독 `ACCEPTED` 이후 해당 씬 모션 제작 착수.
4. **실제 샌드아트 움직임** 검수: 동일 전화기·수화기·인물·밸브, 낱알 흐름. 결함 발생 시 되돌려 수정.
5. ElevenLabs 한국어 음성 길이·발음 확인, 최종 오디오와 싱크·자막·BGM·고지 합성.
6. 30초 통합본 기술 QC + 사람 최종 승인 후 공개/병합.

**승인 전 일괄 I2V 생성·`LOCKED` 표시 금지.**

## 폴더 안내

- `docs/01_STORYBOARD_S01-S05_V1.md`: 5씬 시나리오/핵심 동선.
- `docs/02_SAND_ART_VISUAL_BIBLE_V1.md`: 샌드아트 룩, 설비·인물 연속성.
- `docs/03_AUDIO_CUES_V1.md`: 화자·타이밍·한국어 대사 원장.
- `docs/04_PRODUCTION_WORKFLOW_V1.md`: 제작/승인 규칙과 차례.
- `scenes/S01/`: 검토 기록, 이미지 SHA 및 무음 영상 생성 프롬프트.
- `production/SCENE_REGISTRY_V4.json`: S01–S05 최신 단계별 상태 (V1–V3 이력 보존).

## 이미지 파일 인계 (중요)

S01 V2의 PNG 3장과 컨택트시트는 별도 검토용 ZIP `safety_up_S01_SANDART_KEYFRAMES_REVIEW_V2.zip`로 제공했습니다. **GitHub 공개 저장소에는 바이너리 파일을 업로드하지 않았습니다.** 본 폴더에는 파일명, SHA256, 타임라인, 제작 지시와 검수 상태만 기록합니다.

V2 ZIP SHA256: `4c74880649702007fc4598237c784d44a274aff7fddd479eb8857b3aa2997ebc`.

- 현재 S01 V2: 모래 입자 질감을 강조한 **디지털 프리비즈**(1672×941 소스 → 1920×1080 검토 출력). 동일한 페이지폰 마스터에서 0/3/6초 크롭. 감독 승인/모션/음성 미완료.
- [S01 이미지 검토 기록](scenes/S01/REVIEW_V2.md), [무음 영상 프롬프트](scenes/S01/I2V_PROMPT_V2.md), [V2 레지스트리](production/SCENE_REGISTRY_V2.json).
- V1은 기록으로 보존하고 현재 검토 기준은 **V2**입니다.

영상화 전에는 ZIP의 정확한 버전과 실물 페이지폰 참고자료 대조를 완료해야 합니다. 이미지/비공개 현장자료를 공개 저장소에 올리기 전에 권리·보안·공개적합성 확인이 필요합니다.

## 이미지 생성 직후 필수 통합 QC

씬별 이미지 생성이 끝나면 **이미지·프롬프트·나레이션·발화 시간·전후 씬 연속성·파일 무결성**을 한 번에 검수합니다. 기준: [`docs/05_IMAGE_POSTGEN_BATCH_QC_V1.md`](docs/05_IMAGE_POSTGEN_BATCH_QC_V1.md). 현 S02 검수: [`scenes/S02/QC_INTEGRATED_V1.md`](scenes/S02/QC_INTEGRATED_V1.md). 부족한 자료는 `PENDING`/`NOT_TESTED`, 실패는 `FAIL`로 기록하고 최종 승인이나 I2V 생성으로 진행하지 않습니다.

## S02 V2 제작 복구 및 통합 배치검수

- 현재 이미지 검토본: `safety_up_S02_SANDART_PREVIS_V2_INTEGRATED.zip` (SHA256 `fc2faed4f202c20b84f877d37f613354f88d6d413158d8c39358d7a65266e616`), PNG 8장·1920×1080 **업스케일 컴포지트**.
- 직원 독립 네이티브 HD 원화 생성은 **실패/미완료**. 영상 생성기에서 여러 패널이 들어간 스토리보드를 반복 출력하여 임시 검토본만 제작했으며, I2V에 아직 투입하지 않습니다.
- [통합 QC V2](scenes/S02/QC_INTEGRATED_V2.md), [씬별 영상 프롬프트](scenes/S02/I2V_SHOT_PROMPTS_V2.md), [오디오·손 전환 시점](scenes/S02/AUDIO_CUES_V2.csv), [프레임 SHA](scenes/S02/FRAME_MANIFEST_PREVIS_V2.json).
- 최신 제작 상태: [SCENE_REGISTRY_V5.json](production/SCENE_REGISTRY_V5.json). 이전 V1–V4는 감사 추적을 위해 보존합니다.

## 최신 샌드아트 전환 규칙 / S05

- **[통제형 모래 전환 표준 V2](docs/06_CONTROLLED_SAND_TRANSITIONS_V2.md)**가 최신 규칙입니다. 종전 '모든 변화마다 화가 손 직접 노출 필수' 규칙을 대체하여 **보이는 손은 선택적**, 방향성 모래 스윕·짧은 희미화·새 장면 안정화가 필수입니다.
- **[S05 V1 통합 검수](scenes/S05/S05_V1_INTEGRATED_QC.md)** / **[영상 프롬프트·한국어 오디오](scenes/S05/S05_V1_I2V_AND_AUDIO.md)** / **[제작 상태 V12](production/SCENE_REGISTRY_V12.json)**.
- S05 V1 검토 패키지: `safety_up_S05_CONTROLLED_TRANSITIONS_V1_INTEGRATED.zip` (SHA256 `12779584e8c72de17f8725d4c1e7fadb827434187ff2e116590bac73aca0632e`). PNG·MP4·ZIP은 다운로드 패키지로만 전달하고 **GitHub 공개 바이너리 업로드는 하지 않았습니다.**
- 현재 24초 영상에는 S01이 포함되지 않고 실제 ElevenLabs 한국어 음원·BGM·전체 30초 합본이 없습니다. `FINAL_LOCKED=false`.
