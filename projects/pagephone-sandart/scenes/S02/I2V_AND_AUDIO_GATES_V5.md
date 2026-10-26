# S02 V5 I2V·한국어 음성 후반 인계

**현재는 구현 가이드, 실행 승인 아님.** 실제 샌드아트 제작용 I2V는 독립 고해상도 이미지와 전화기 픽업 물리 장면 승인 이후 사용한다.

1. S01 종료 전화기 정확한 레퍼런스 유지. 06.00–06.34 유일한 수화기가 거치대에서 분리되어 첫 남성 귀로 이동. **그 순간 벽 거치대는 비어 있음**. 다른 수화기 생성 금지.
2. 06.34–07.37 남성1 한국어 `네, 알겠습니다.`. 남성1은 S01 마지막 안전모 실루엣과 동일 인물.
3. 07.37–07.67 실제 작가의 손이 모래를 쓸어 첫 남성을 지우고 여성 형상 그리기. **손의 픽셀 이동만으로는 불합격**.
4. 07.67–08.54 여성 `확인했습니다.`; 08.54–08.84 작가 손으로 남성2 재형성.
5. 08.84–09.74 남성2 `진행하겠습니다.`; 09.74–10.12 손으로 지우고 원래 페이지폰 복귀.
6. 09.95–11.94 화면 밖 페이지폰 VO `그보다 반가운 말이 있죠.` (손 전환에 0.17초 선행). 인물 립싱크 없음.
7. 각 마이크로샷 **무음 생성**. 실측된 ElevenLabs 한국어 녹음과 효과음·BGM은 후반에 넣고 말 시작·끝/손동작 시간 재검수.

**공통 비주얼:** Single 16:9 handcrafted backlit sand-light-table painting, warm amber/umber grains, one consistent wall-mounted industrial pagephone with exact S01 keypad/screen/right junction box, visible sand artist hand performing actual granular erasure and redraw during transitions. No montage boards or captions, no photoreal film, no vector cartoon, no duplicate handset, no spontaneous morph, no generated voices, no English, no logos.

**Negative:** storyboard panel, infographic, captions, duplicate handset, wall receiver hanging while someone holds another, telephone keypad mutation, perspective flip, extra workers, magical sand transition without hand contact, generated speech/music.
