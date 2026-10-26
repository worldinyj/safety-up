# SAFETY UP — 전사 AI 안전영상 콘테스트

## 현재 제작본: 「페이지폰의 고백」 · Storyboard V2

**30초 / 5 × 6초 / Image-to-Video / 실사풍 / 16:9 / FHD MP4 (500MB 미만)**

핵심: 질문하고 다시 확인하려는 **팔로우십**, 이를 받아들여 함께 확인하는 **리더십**, 두 행동으로 드러나는 **원자력안전문화**.

- [Storyboard V2 (CURRENT)](docs/02_storyboard/STORYBOARD_30S_V2.md)
- [비주얼·캐릭터·페이지폰 고정 규칙 V2](docs/03_visual/VISUAL_BIBLE_V2.md)
- [오디오 타이밍 및 ElevenLabs 가이드 V2](docs/04_audio/AUDIO_PLAN_V2.md)
- [Grok I2V 클립별 생성 지시 V2](docs/05_generation/SHOT_PROMPTS_V2.md)
- [QC 및 인간 승인 게이트 V2](docs/06_review/QC_GATES_V2.md)
- [**Grokbot Producer 실행 인계서 V2**](docs/07_producer/PRODUCER_HANDOFF_V2.md)
- [기계판독형 샷 매니페스트](production/shot_manifest_v2.json)
- [프로젝트 상태](project/STATUS.md)
- [공모전 기준](docs/00_brief/CONTEST_REQUIREMENTS.md)
- [후속 별도 아이디어 — 「마지막 1초」](docs/08_backlog/CONCEPT_BACKLOG.md)

**Grokbot 인계 원칙:** 반드시 `feat/pagephone-confession-v1` 브랜치의 위 V2 문서와 JSON을 읽고 시작할 것. V1 문서는 초기 기획 기록이며 제작 기준이 아님. 첫 결과물은 승인용 개별 키프레임(시작/중간/마지막), 오디오 길이 분석표, 리스크 목록이다. 승인 전 I2V 다량 생성·유료 API 호출·공개 업로드 금지.

### 중요 참고 이미지
사용자가 업로드한 실제 회색 **IP PAGE PHONE** 사진 및 5컷 실사형 스토리보드 참고 시안을 원본 기준으로 한다. **이미지 바이너리는 현 시점 GitHub에 업로드되지 않았으므로**, Grokbot에 이미지 참조 파일을 별도 전달해야 한다. 예비 시각 시안은 제작용 1920×1080 개별 키프레임이 아니다. 공개 저장소에 실제 현장 사진·실제 운전정보를 올리기 전에 사용 권한/대외 공개 적합성을 검토한다.

### 진행 방식
기획/대본 승인 → 참조사진 정리·폰 모델 고정 → 첫·중간·마지막 개별 키프레임 검수 → 5×6s 영상 → ElevenLabs/음원/BGM → 최종 FHD 합성 → 30초/500MB/AI 고지 검수 → human acceptance.
