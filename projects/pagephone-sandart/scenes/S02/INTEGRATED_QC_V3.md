# S02 V3 통합 QC 요약

**현재 판정:** `DESIGN_STUDY_ACCEPTABLE / SAND_ART_MASTER_FAIL / I2V_BLOCKED`

| 항목 | 판정 | 근거 |
|---|---|---|
| 정리된 8개 장면 | PASS | F00 S01 원본 + 신규 7개 SVG 렌더 |
| 신규 컷 독립 1920×1080 | PASS_RESOLUTION | 각 신규 컷 원본 도형을 1920×1080에서 렌더, 이전 200px 시트 크롭 재활용 안 함 |
| S01 시작 연결 | PASS_IMAGE_ANCHOR | 마지막 원본 이미지 사본 그대로 포함 |
| 전화기/수화기 구성 신규 컷 내부 | PASS_DESIGN | 인물 컷 수화기는 손의 1개, 거치대는 빈 상태 |
| S01과 전화기 동일 형상·화풍 | **FAIL** | 신규 SVG는 별도 도안 |
| 손 3개 전환 컷 | PASS_STATIC | 각각 별도 정지 이미지, 영상 동작 검수 아님 |
| 실제 모래 움직임 | NOT_TESTED | I2V 없음 |
| 샌드아트 수작업 그림 품질 | **FAIL** | 선화/벡터 느낌 강함 |
| 화자·한국어 대사 원문 | PASS_TEXT | 원문 불변 |
| 나레이션·직접 대사 타임코드 | PROVISIONAL | 0.30/0.30/0.35초 손 전환, 무음·입모양·음원 실측 불완전 |
| 오디오 실제 생성·검수 | NOT_TESTED | WAV/MP3 없음 |
| 영상 생성 | NOT_TESTED | MP4 없음 |
| 감독 최종 승인 | NOT_GRANTED | `LOCKED=false` |

후속: S01과 동일한 샌드아트 재질로 각 인물 독립 생성 → 정확한 페이지폰 일치 → 실제 손 스윕 모션 → 한국어 파일 실측 → 감독 검수.
