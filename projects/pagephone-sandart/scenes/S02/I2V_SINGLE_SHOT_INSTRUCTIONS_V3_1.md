# S02 V3.1 — 독립 단일 이미지 / 무음 I2V 통합 프롬프트

**이미지 생성 게이트:** 이미지 한 장을 요청했는데 설명판/멀티패널/캡션이 생성되면 즉시 REJECT. S01 고정 페이지폰 참조를 모델 입력의 image reference로 재사용하고 실제 형상/재질을 이미지끼리 대조해야 한다. 구도용 SVG/PDF는 최종 샌드아트 마스터가 아님.

## 공통 프롬프트 (영문 입력, 화면·음성 한국어만 별도 합성)
```text
ONE single cinematic 16:9 still frame. Handmade backlit sand painting
on an illuminated glass light table, warm umber grains and finger-swept
contours, matching the previously approved S01 sand-art master phone
EXACTLY in size, orientation, keypad arrangement, right auxiliary box
and plant wall arrangement. No storyboard, grid, multiple shots,
infographic, explanatory text, graphic borders, titles or captions.
Exactly one telephone handset in the depicted scene.
When a worker speaks holding the receiver, the wall cradle is EMPTY.
A visible real sand artist's hand reshapes the grains on the sand-drawing
surface whenever one person's image is transformed into another.
The artist's hand is distinct from the fictional worker's arm.
No photoreal camera footage, no floating magical morphing, no logo,
no model-generated audio. English voices prohibited; actual Korean
speech and narrated pagephone audio will be dubbed separately.
```

## Individual frame directions
- `M1`: first worker **same person as S01 closing left helmet silhouette**. Keep body/helmet/vest silhouette invariant. One receiver at ear, wall phone cradle empty. Phone cable connects physically.
- `HAND_1`: artist hand physically erases M1 and draws female figure on same sand surface.
- `F`: only one female appearance, distinct ponytail/silhouette, one handheld receiver, empty wall cradle.
- `HAND_2`: physical artist sand sweep, female replaced by visually distinct man 2.
- `M2`: second male with glasses as silhouette cue. One handheld receiver, empty cradle.
- `HAND_3`: physical sand wipe replaces worker with exact S01 wall phone; only after redraw may receiver appear back on wall cradle.
- `PHONE_VO`: exact same wall phone, one receiver on cradle. No speaking mouth or employee present.

## Critical S01→S02 pickup — 6.00–6.34 sec
The previous S01 frame has the only handset hanging on the wall.
S02 must visibly show M1 **taking that single handset off the cradle**.
Once it is held at the ear, the cradle must be empty. No jump cut to
a second duplicated receiver. Do not start the direct M1 speech before
the handset is visibly at the ear (unless real measured audio requires
an explicitly approved time adjustment).

## Sound (separate, Korean only)
- 6.34–7.37 M1: 네, 알겠습니다.
- 7.67–8.54 F: 확인했습니다.
- 8.84–9.74 M2: 진행하겠습니다.
- 9.95–11.94 PAGEPHONE offscreen VO: 그보다 반가운 말이 있죠.
- Sand hand swipes: 7.37–7.67, 8.54–8.84, 9.74–10.12.
- 9.95 VO overlaps the last visual redrawing as an **intentional audio lead**; no actor mouth must move during it.

Actual voice files have not been created or measured; all timecodes are conditional.
