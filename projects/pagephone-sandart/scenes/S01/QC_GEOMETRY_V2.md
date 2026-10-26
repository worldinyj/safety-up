# S01 V2 추가 QC — 프레임 기하학·파일 무결성

**일자:** 2026-10-26 · **판정:** TECHNICAL_PREVIEW_QC_PASS, HUMAN_ACCEPTANCE_PENDING

기존 V2 검토 패키지를 작업 환경에서 직접 확인했다. 모래 질감의 예술적 적합성, 현장 실물 페이지폰 재현, 생성 영상의 자연스러움은 자동 QC로 승인되지 않는다.

## 무결성

- ZIP: `safety_up_S01_SANDART_KEYFRAMES_REVIEW_V2.zip`
- ZIP SHA256: `4c74880649702007fc4598237c784d44a274aff7fddd479eb8857b3aa2997ebc`
- ZIP 멤버 8개. CRC 검증: PASS (오류 없음).
- 마스터: `S01_PHONE_SAND_ART_MASTER_V2.png` / 1672×941 / SHA256 `f4086a8891d7f714e7884186917cdf18c43177ff0b96b8e8a43c779da3e281cd`
- 컨택트시트: `S01_CONTACT_SHEET_SANDART_V2.jpg` / SHA256 `76186669576ad06e750aefacd8bde9ea5336a7b088b8ca989f6e3ba3ec0572b7`
- 세 프레임: 모두 1920×1080이며 매니페스트 기록과 SHA256 일치.

## 화면 기하학 연속성

방법: OpenCV ORB (nfeatures=5000), BFMatcher (ratio test 0.74), RANSAC homography(재투영 임계값 2.5px). 시작 프레임과 비교한 전체 화면 분석.

| 비교 | 좋은 특징점 매칭 | RANSAC inliers | inlier 비율 | 추정 배율 |
|---|---:|---:|---:|---:|
| F01→F02 | 3457 | 3255 | 94.16% | 약 1.035배 |
| F01→F03 | 2708 | 2535 | 93.61% | 약 1.071배 |

동일한 전화기 원본과 느린 확대 구성이 유지되었다는 확인이다. **독립 키프레임 재현 검증이나 실제 비디오 모션 검증이 아니다.**

## 제작 게이트

- [x] 3장 실존·해시·CRC 검증
- [x] 전화기 한 원본 기반의 화면 기하학 연속성 확인
- [ ] 실물 페이지폰 `IMG_9556.jpeg` 원형 대조
- [ ] 정적 프리비즈의 샌드아트 표현 감독 적합성 승인
- [ ] 네이티브 FHD 마스터 적합성 판단 (현 파일들은 1672×941 업스케일)
- [ ] 6초 실모션 샌드아트 생성 및 물리·시간 QC
- [ ] 한국어 음성 실길이·자막·효과음 후반 검수

**상태 유지:** `DIRECTOR_REVIEW_PENDING`, `LOCKED=false`. 영상 생성 및 다음 씬 잠금 승인 없음. 공개 GitHub에는 이미지 바이너리가 아닌 문서·해시만 존재한다.
