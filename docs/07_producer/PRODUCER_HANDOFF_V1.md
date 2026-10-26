# Grokbot 제작팀 Producer 전달용 작업 명령 — Draft V1

## 임무
SAFETY UP 원자력안전문화 30초 AI 영상 프로젝트 「페이지폰의 고백」 제작계획을 작성한다. 본 지시서는 **스토리보드 승인 이후 사용할 프로듀서 핸드오프**이며, 곧바로 영상 생성/원격 지출을 승인하지 않는다.

## R&R
- Producer: 샷별 타임라인·예산·승인 기록·자산 인계·버전 통제.
- Writer: 사용자 지정 대사를 한 글자도 변경하지 않고 6초 × 5 시나리오 적합성 재검토.
- Visual Director: 첨부된 페이지폰 참조 사진 기준 Device Lock; 인물/장소/광량 일관성.
- Shot Director(Visual Director 내부 역할): 3개 중점 keyframe와 5개 clip I2V movement 명세.
- Audio/Editor: ElevenLabs 음성·효과음·Google 음악 도구(실제 제품명 확인)·자막 편집.
- QC: 실물 외형, 타임라인, lipsync, 관련 대사, 엔딩 카피, 시작/종료 AI 고지, 출품규격 검증.

## 반드시 읽을 문서
README.md / docs/01_concept/CONCEPT_V1.md / docs/02_storyboard/STORYBOARD_30S_V1.md /
docs/03_visual/VISUAL_BIBLE_V1.md / docs/04_audio/AUDIO_PLAN_V1.md /
docs/05_generation/SHOT_PROMPTS_V1.md / docs/06_review/QC_GATES_V1.md

## 단계
1. 대본·발음·보이스 길이 예측, 사용자 승인 요청.
2. 원본 장치 사진에서 스크린샷 외곽·모아레 제거한 16:9 사진기반 디바이스 마스터 생성; 검수.
3. 최소 3장의 각기 독립된 I2V용 1920×1080 **Opening / Valve-21 / Joint-verification** keyframes 확보; 승인.
4. 6초 × 5개 영상 생성. 클립별 변형·얼굴·디바이스 변화 QC.
5. ElevenLabs, 효과음, BGM, 카피 후반 삽입 → FHD MP4 렌더.
6. sha256, duration, resolution, filesize, audio tracks, compliance score 검수.
7. 제출 버전 Human acceptance 이후 태그.

## 금지
- 실물과 다른 전화기 교체, 만화 얼굴 부착, 무단 자막, 가상 사고 과장.
- 원본 참조 사진 또는 회사·설비 상세의 공개 저장소 무심사 업로드.
- 승인 전 자동 생성·결제·게시·출품.
