# SAFETY UP — 「페이지폰의 고백」

**CURRENT = V3 / 2026-10-26 / Grokbot production preparation**

- 30초, 16:9, 1920×1080 FHD, MP4, 500MB 이하
- 실사풍, 6초 편집 슬롯 × 5, **시작/중간/끝 총 15개 프레임 목표**
- 등장: S02 일상응답 한 꼭지에만 여성 1명; S03 남성 현장 작업자 A; S04 남성 리더 B.
- 외관: 채팅 첨부 실제 회색 **IP PAGE PHONE**을 동일 기종으로 유지.
- **밸브 표지: `A` 한 글자. 음성: “알파 밸브 한 번 더 확인하겠습니다.”** (21, -A, '대시 알파' 전부 폐기)
- 페이지폰 자기소개: 화면에 “안녕하세요. / 전 페이지폰입니다.”
- S05 첫 3초: 실내 작업자+리더 공동확인. **마지막 3초: 사용자가 승인한 석양 원전 전경 카피 화면**. 야외에 페이지폰을 설치하지 않음.
- 맨 앞 페이지폰 호출음; ElevenLabs 내레이션/대사, BGM 후반 삽입.
- 영상의 시작과 종료에 **AI 제작 고지**.

## Grokbot 최신 읽기 순서 (반드시 V3를 사용)
1. [Storyboard V3](docs/02_storyboard/STORYBOARD_30S_V3.md)
2. [Visual Bible V3](docs/03_visual/VISUAL_BIBLE_V3.md)
3. [15-frame Continuity Plan](docs/03_visual/FRAME_CONTINUITY_V3.md)
4. [Audio V3](docs/04_audio/AUDIO_PLAN_V3.md)
5. [Grok I2V Prompts V3](docs/05_generation/SHOT_PROMPTS_V3.md)
6. [Quality Gates V3](docs/06_review/QC_GATES_V3.md)
7. [Producer Handoff V3](docs/07_producer/PRODUCER_HANDOFF_V3.md)
8. [Shot Manifest V3](production/shot_manifest_v3.json)
9. [Project Status](project/STATUS.md)

## 중요한 원본 참조
- `IMG_9556.jpeg` 실물 페이지폰, SHA256 `b8129ec0bf9398143497a95943403da2b4a0bbbafdf0c2498bcb9ec125187d06`
- `IMG_9558.jpeg` 사용자가 확정한 엔딩 카피 구도, SHA256 `acb0082813415387a8c5f0aabe7e4e7ab73245072b9fd0fe1f1ffef99664b60a`
- **현재 공개 GitHub 저장소에는 두 사진의 바이너리가 없음**. 챗 첨부를 모델이 자동 받는다고 가정하지 말고, 로컬 복사·사내 공개 적합성 점검을 거친 별도 전달이 필요.

## 승인 상태
**스토리보드 및 개별 프레임 작업 지시서는 V3 확정.** 실사 이미지 생성 중 생산용 15개 독립 16:9 마스터는 **아직 QC/LOCK 완료 아님**. 기존 AI 생성 15분할 보드를 분리한 파일은 **검토용 프리뷰**, 제작용 원본을 대신하지 않는다.
V1/V2는 이전 판본·기록이고 향후 자동 영상 생성 기준이 아니다. 최종 30초 영상은 생성·출품되지 않았다.
