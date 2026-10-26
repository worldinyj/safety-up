# QC gates V2 — do not equate concept-board approval with rendered-video approval

| Gate | Acceptance rule | State |
|---|---|---|
| G0 Requirements | 30초, 16:9, FHD MP4, <500MB, AI 고지 시작/종료 | WRITTEN |
| G1 Storyboard | 사용자 원문 대사 3개 + 끝 3행 + 남녀 역할 + 모든 장면 실내 | V2 REVIEW |
| G2 Phone reference | PHOTO_REF 장치 패널/색·형태/화면/수화기/키패드·액세서리의 참조 일치 | WAIT |
| G3 Individual keyframes | 16:9 **독립 이미지** KF-OPEN/KF-MIDDLE/KF-END, 각각 인물·환경·폰 정확성 | WAIT |
| G4 Generation | 각 6.000s × 5, 캐릭터·설비 연결, 불필요한 비상경보/야외 전환 없음 | WAIT |
| G5 Audio | 호출음 첫머리, 실제 ElevenLabs 파일 검증, 2개 직원/리더 대사 원문 + 페이지폰 최종 VO 정확성 | WAIT |
| G6 Editorial | 처음/끝 AI 고지, S01 스크린 인사말, 27–30초 3행 카피, 자막 맞춤법 | WAIT |
| G7 Final compliance | video stream h264/HEVC as agreed, audio AAC, 1920×1080, 30.0±편집 프레임 오차 미만, <500MB | WAIT |
| G8 Human acceptance | 검수/브랜드·보안/권리/교육 적합성, 출품 승인 | WAIT |

## Automated QC examples
```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,r_frame_rate -of json deliverables/SAFETY_UP_PAGEPHONE_FINAL_V01.mp4
shasum -a 256 deliverables/SAFETY_UP_PAGEPHONE_FINAL_V01.mp4
```

## STOP CONDITIONS
- S02에 여성이 독립 주인공으로 바뀌거나 S03 남성 A가 다른 얼굴로 바뀐 경우.
- S05 페이지폰이 옥외에 있거나 외부 원자로/노을 전경으로 전환되는 경우.
- S01 화면에 `7.0`가 남아 인사 문구가 안 보이는 경우.
- 대사/카피 변경, 호출음보다 먼저 VO가 나오거나 엔딩 AI 고지 누락.
- 5분할 보드에서 단순 크롭한 낮은 해상도를 최종 I2V 입력으로 채택하는 경우.
- 공개 repo에 실물 원본/부서·사업소를 특정할 수 있는 기밀 또는 권리 미확인 사진 업로드.
