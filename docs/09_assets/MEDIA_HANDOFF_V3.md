# Grokbot 미디어 인계 V3

이 문서는 **GitHub 저장소와 로컬 미디어 자산을 일치시키기 위한 실무 런북**입니다.

## 다운로드할 비공개 인계 패키지
채팅 대화의 다운로드 첨부: `safety_up_grokbot_media_handoff_v3.zip` (약 6.2MB)  
SHA256 `f19f1ae4d8e7413392559337b437dc1cd94042aea9d6928ec1f7516c1f40e21d`.

ZIP에는 다음이 들어 있음:
- `assets/reference/IMG_9556.jpeg`: 실제 페이지폰 사진 (원본).
- `assets/reference/IMG_9558.jpeg`: 감독 지정 석양 원전 엔딩 카피 사진 (원본).
- `assets/previs/S01_FIRST_PREVIS_V3.jpg` ... `S05_LAST_PREVIS_V3.jpg`: 총 15장 프리비즈. 정확한 영상 입력 이미지가 아닌 **연출 참고용**.
- `assets/previs/ALL_15_KEYFRAMES_CONTACT_SHEET_V3.jpg`: 콘택트 시트.
- `production/handoff_file_checksums_v3.json`: 각 파일의 SHA256.
- `READ_ME_FIRST.txt`: 인계 설명.

## Grokbot이 로컬에서 시작하는 방법 (macOS / zsh)
```bash
git clone https://github.com/worldinyj/safety-up.git ~/Projects/safety-up  # 이미 있으면 clone 생략
cd ~/Projects/safety-up || exit 1
git fetch origin
git switch feat/pagephone-confession-v1
git pull --ff-only origin feat/pagephone-confession-v1
unzip -o ~/Downloads/safety_up_grokbot_media_handoff_v3.zip -d .
python3 scripts/verify_media_v3.py
```

**중요**: 인계 ZIP은 GitHub에 직접 존재하지 않습니다. ChatGPT에서 받은 ZIP을 본인 다운로드 폴더에 놓아야 위 명령을 실행할 수 있습니다. GitHub 작업 브랜치에는 텍스트/매니페스트/검증 스크립트만 저장되어 있습니다.

## 품질 구분
15장 JPG는 픽셀 캔버스가 1920×1080이어도 보드 내 원본 컷이 약 300×225였으므로 **네이티브 FHD가 아닙니다**. 15장 모두 새로 생성된 원본 품질 독립 이미지가 확보되기 전에는 I2V 영상 생성에 투입하지 마십시오.

## 작업 기준
- `A` 표지는 대문자 A 한 글자, 음성은 **알파**, ‘대시’ 발화 금지.
- 페이지폰은 실내에 부착된 원본 모델 그대로.
- S02에서 여성은 **단 한 컷**. S03 남성 작업자, S04 남성 리더.
- S05 24–27초 실내 함께 확인, 27–30초 지정 엔딩 이미지 별도 편집 전환.
- 음성/음악/고지/문구는 **후반 편집**에서 삽입.

## 보안
이 저장소는 공개 상태입니다. 이 ZIP은 **로컬 전용 인계**이고, 사용자 제공 원본 사진·프리비즈를 공개 원격 저장소에 바로 `git add -f`하지 마십시오. 사내 정보보안 및 사용권리 확인 후에만 배포할 수 있습니다.
