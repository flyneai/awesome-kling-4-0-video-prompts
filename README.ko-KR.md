<div align="center">

![Kling 4.0 프롬프트 라이브러리](assets/images/flyne-kling-cover.png)

# Awesome Kling 4.0 Prompts 한국어 가이드

영화, 제품 광고, UGC, 대화, VFX, 애니메이션, 음식, 여행, 교육 및 소셜 영상용 실전 AI 비디오 프롬프트 모음입니다.

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · **한국어** · [Español](README.es-ES.md) · [15개 언어](docs/LANGUAGES.md)

[52개 프롬프트](prompts/README.md) · [프롬프트 가이드](docs/PROMPT-GUIDE.md) · [다국어 오디오](docs/MULTILINGUAL-AUDIO.md) · [Flyne AI](docs/FLYNE.md)

</div>

<!-- brand-intro:start -->
[Flyne AI 사용하기](https://flyne.ai/model/kling-4-0/) · [X 영상과 새 연습](docs/X-VIDEOS.md) · [연습 4개](prompts/inherited-flash-exercises.md)

[Flyne AI Kling 4.0 페이지](https://flyne.ai/model/kling-4-0/)에서 제공 현황을 확인하세요. 2026년 9월 30일 기준 4.0은 출시 예정이며 양식에는 **Kling 3.0 Turbo**가 선택되어 있습니다. 생성 전에 모델을 확인하세요. Flyne AI의 안정적인 4.0 제공은 아직 검증하지 않았습니다.
<!-- brand-intro:end -->


> **모델 상태(2026-09-29):** Kling 4.0 Flash가 9월 28일 Ultra 연간 구독자를 대상으로 조기 제공되기 시작했습니다. [Kling AI 공식 발표](https://sg.linkedin.com/company/kling-ai-api)에 따르면 정식 Kling 4.0과 API 접속은 2026년 10월 출시 예정이며 정확한 날짜는 아직 없습니다. 정식 버전은 한 번에 최대 **30초** 생성할 수 있다고 발표했지만, 현재 Flash에도 같은 제한이 적용되는지는 확인되지 않았습니다. 기존 프롬프트는 5~15초로 작성되어 있습니다.

## Kling 4.0 새 기능과 이용 상태

[Kling AI 공식 X 게시물](https://x.com/Kling_ai/status/2104596718067257458)에 따르면 Flash는 Ultra 연간 구독자에게 먼저 제공되며, 정식 4.0과 API는 2026년 10월 출시 예정입니다. 정식 버전에는 단일 생성 최대 30초, 키프레임 최대 10개, 멀티모달 참조 최대 15개, 최대 4K/10-bit HDR, 스테레오 오디오와 더 폭넓은 언어·억양 지원이 발표되었습니다. **이 수치를 현재 Flash에서 검증된 한도로 해석하면 안 됩니다.** 기존 52개 프롬프트는 5~15초 기준입니다.

## X 동영상과 프롬프트 사례

**확인일: 2026-09-29.** [공식 소개 영상](https://x.com/Kling_ai/status/2104596718067257458)은 4.0 제품군의 편집 영상이며 전체 재생 시간이 Flash의 한 번 생성 길이를 증명하지 않습니다. 아래는 제작자가 직접 밝힌 테스트로, 공식 벤치마크나 이 저장소의 재현 검증이 아닙니다. 영상과 원문 프롬프트는 원본 게시물에서 확인하세요.

| 원본 게시물 | 적용해 볼 프롬프트 방식 |
|---|---|
| [Umesh: 20초 야간 고양이 추적 영상](https://x.com/umesh_ai/status/2104595267794460949) · [원문 프롬프트](https://x.com/umesh_ai/status/2104595270671724936) | 하나의 주인공, 이어지는 동선, 장소마다 한 가지 물리적 사건을 지정하고 카메라가 끊김 없이 따라가게 한다. |
| [OscarAI: 20초 애니메이션 공연과 프롬프트](https://x.com/Artedeingenio/status/2104829034299351079) | 제작자는 초기 실험에서 간결한 지시가 낫다고 보고했지만 완전한 준수는 아니었다. 주체→변화→카메라→결말 순서부터 실험한다. |
| [とすくん: 15초 날씨 변화 영상](https://x.com/tokyo_Valentine/status/2104810060811833710) · [원문 프롬프트](https://x.com/tokyo_Valentine/status/2104810064750239987) | 캐릭터 시트는 외모와 의상만 고정하고, 날씨·조명·연기의 변화 시점은 별도로 적는다. |
| [Alexandra Dekimpe: 제작 워크플로 테스트](https://x.com/HadesDesign/status/2104878440889417957) | 추상적 감정보다 눈에 보이는 미세 행동을 쓴다. ‘완료된 후에만’으로 인과를 고정하고 정확한 대사 또는 무대사를 지정한다. 개인 관찰이다. |
| [Aswin Aji Raj: 20초 힌디어 UGC](https://x.com/Aswin_Aji_Raj/status/2104867308514779222) | 전문 프롬프트는 공개되지 않았다. 화자와 정확한 문장을 지정하고 발음·립싱크·제품 주장을 검토한다. |
| [@plasm0: 3.0과 Flash 동일 프롬프트 비교](https://x.com/plasm0/status/2104597949485629557) | 같은 문장과 참조를 유지한 A/B 테스트를 하고 설정을 기록한다. 한 쌍의 결과를 정식 성능 평가로 일반화하지 않는다. |

**이 프로젝트가 새로 작성한 미검증 15초 세로 영상 연습 프롬프트**(공식 52개 레시피에는 포함되지 않으며 X 문구를 복사하지 않음):

~~~text
[주체/참조] 브랜드 없는 충전식 자전거 전조등 한 개. 무광 흑연색 본체와 호박색 스위치 하나. 이미지를 쓰면 전조등 형태만 고정한다. 영상 내내 전조등은 하나만 유지한다.
[장소/카메라] 해 질 무렵 조용한 자전거 수리점. 정비사의 두 손에서 전조등과 핸들바로 이어지는 단일 근접 추적 숏. 창문 자연광. 컷이나 순간이동 없음.
[0–4초] 꺼진 전조등을 핸들바 옆에 놓고 양손과 장착 브래킷을 함께 보여 준다.
[4–8초] 전조등을 브래킷에 끼운다. 딸깍 소리와 함께 완전히 고정된 후에만 엄지로 호박색 스위치를 누른다.
[8–12초] 불이 딱 한 번 켜져 앞바퀴와 작은 바닥 면을 비춘다. 카메라가 천천히 옆으로 움직여 빛줄기를 보여 준다.
[12–15초] 정비사는 핸들바에서 손을 뗀다. 전조등은 고정된 채로 남는다. 안정된 마지막 프레임을 유지한다.
[오디오/제약] 수리점 실내 소리, 장착 소리 한 번, 스위치 소리 한 번. 대사·음악 없음. 형태, 손의 수, 장착 위치와 조명 방향 유지. 브랜드 글자, 추가 전조등, 불필요한 점프컷 없음.
~~~

짧은 지시와 길지만 구조화된 지시를 모두 시험하고, 사용 모드·길이·참조·결과를 기록한 뒤에만 ‘테스트 완료’로 표시하세요. 독창적인 사례는 [기여 가이드](CONTRIBUTING.md)를 통해 제출할 수 있습니다.

## 포함된 내용

- 13개 제작 컬렉션과 52개의 완성형 프롬프트
- 텍스트-투-비디오, 이미지-투-비디오, 시작/종료 프레임, 피사체 참조 전략
- 초 단위 샷, 카메라, 연기, 물리, 오디오 및 오류 방지 조건
- 한국어, 중국어, 영어, 일본어, 스페인어 대화 패턴
- 영화, 제품, UGC, 액션, 애니메이션, 패션, 음악, 음식, 여행, 공간, 교육, 소셜 콘텐츠
- 참고 이미지와 새로운 Flyne AI 표지

## 기본 구조

```text
[출력] 길이, 화면비, 싱글 테이크/멀티샷, 시각적 톤
[연속성] 인물, 의상, 제품, 소품의 고정 특징
[공간] 장소, 시간, 광원, 시작 위치
[타임라인] 구간마다 하나의 주요 동작 + 하나의 카메라 의도
[연기] 시선, 호흡, 손 접촉, 감정 변화, 무게와 속도
[오디오] 화자(언어·톤·속도) + 환경음 + 동기화된 효과음
[제약] 얼굴, 손, 진행 방향, 조명, 텍스트, 로고, 원치 않는 변형
```

## 한국어 대화 예시

```text
민아 (한국어, 낮고 차분한 목소리): “종이학을 아직도 가지고 있었어?”
준 (한국어, 짧게 숨을 고른 뒤): “버릴 수가 없었어.”
민아의 대사 중에는 민아만 입을 움직이고, 준의 대사 중에는 준만 입을 움직인다.
번역, 자막, 추가 대사를 만들지 않는다. 빗소리는 두 대사 아래에서 끊기지 않는다.
```

이름, 숫자, 전문 용어의 발음과 정확한 문구는 반드시 결과에서 확인하세요. 자막은 검수 후 편집 단계에서 추가하는 편이 안전합니다.

## 추천 프롬프트

- [한국어×스페인어 기차역 재회](prompts/cinematic-and-dialogue.md#2-the-paper-crane-at-platform-seven)
- [보태니컬 음료 제품 공개](prompts/commercial-and-ugc.md#1-botanical-spark-product-reveal)
- [루프형 우산 코미디](prompts/education-documentary-social.md#3-the-infinite-umbrella-problem)
- [새벽 루프탑 타악 연주](prompts/style-and-performance.md#3-rooftop-percussion-at-dawn)

전체 목록은 [프롬프트 카탈로그](prompts/README.md)를 확인하세요.

## 독창성과 책임 있는 사용

허가 없는 인물의 얼굴·목소리, 브랜드, 캐릭터, 음악을 사용하지 마세요. 광고 문구, 교육 정보, 건축·공예·지역 문화는 게시 전에 전문가 검토가 필요합니다.

공식 근거: [Kuaishou Kling AI 3.0 발표](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be) · [Kling Video 3.0 공식 가이드](https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide)

<!-- brand-footer:start -->
<a id="flyne"></a>

## Flyne AI 사용하기

[Flyne AI Kling 4.0 페이지](https://flyne.ai/model/kling-4-0/)에서 제공 현황을 확인하세요. 2026년 9월 30일 기준 4.0은 출시 예정이며 양식에는 **Kling 3.0 Turbo**가 선택되어 있습니다. 생성 전에 모델을 확인하세요. Flyne AI의 안정적인 4.0 제공은 아직 검증하지 않았습니다.

[사용 방법](docs/FLYNE.md)

## FLAQ AI Kling 4.0 API · Kling 3.0 Std / Pro

앱에 영상 생성을 연동하려면 FLAQ AI의 Kling API를 살펴보세요.

- [Kling 4.0 API · 텍스트로 영상 만들기](https://flaq.ai/models/kuaishou/kling-4-0-text-to-video/) — 장면을 글로 설명해 광고, 소셜 영상, 스토리 아이디어를 영상으로 만드는 기능입니다.
- [Kling 4.0 API · 이미지로 영상 만들기](https://flaq.ai/models/kuaishou/kling-4-0-image-to-video/) — 참고 이미지와 동작 프롬프트를 조합해 제품 사진, 인물 사진, 일러스트에 움직임을 더하는 기능입니다.

2026년 9월 30일 확인: 두 페이지 모두 **Coming Soon(출시 예정)**으로 표시됩니다. API 모델 소개 페이지이며, 제공 시점과 매개변수, 요금은 출시 후 안내를 확인하세요.

- [Kling 3.0 Std API](https://flaq.ai/models/kuaishou/kling-3-0-std-text-to-video/) — 텍스트로 영상 생성. 비용을 줄인 초안과 여러 버전 제작에 적합합니다.
- [Kling 3.0 Pro API](https://flaq.ai/models/kuaishou/kling-3-0-pro-text-to-video/) — 화질을 중시하는 제작용입니다. 같은 프롬프트로 Std와 비교한 후 선택하세요.

[API 선택 및 연동 안내 (영어 / 중국어)](docs/FLAQ-AI.md)

## 제휴 프로그램

Flyne AI는 크리에이터, 튜토리얼 제작자와 리뷰어의 [제휴 참여](https://flyne.ai/affiliate-program/)를 환영합니다. 현재 첫 유효 유료 주문은 20%, 가입 후 60일 이내 후속 유효 주문은 10% 수수료를 제공합니다. 최신 조건을 확인하고 추천 관계를 공개하세요.
<!-- brand-footer:end -->
