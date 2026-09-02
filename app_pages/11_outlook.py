import streamlit as st

from utils.slides import slide_deck


def s_recap() -> None:
    st.markdown("### 지금까지 다룬 것")
    with st.container(horizontal=True):
        st.metric("도구 프로필", "10+", border=True)
        st.metric("벤치마크 리더보드", "2개", border=True)
        st.metric("타임라인 이벤트", "19개", border=True)
        st.metric("유튜브 레퍼런스", "18개", border=True)
    st.markdown(
        """
Claude·Codex·Gemini 3개 프론티어 모델사부터 Cursor·Copilot·Devin·Replit·Kiro 같은 제품
특화 도구, DeepSeek·GLM·Qwen 같은 오픈웨이트 도전자까지 — 2026년 9월 현재 AI 코딩
어시스턴트 지형은 **한 회사의 독주가 아니라 다층적 경쟁 구도**로 정리됩니다.
        """
    )


def s_three_trends() -> None:
    st.markdown("### 핵심 트렌드 3가지")
    cols = st.columns(3)
    items = [
        ("멀티 툴 스태킹이 표준", "개발자 70%가 2~4개 도구를 동시 사용. '최고의 도구' 대신 '작업별 최적 조합'을 찾는 흐름"),
        ("에이전틱 심화 + 오픈웨이트 추격", "서브에이전트·비동기 실행·스펙 주도 개발이 표준이 되는 동시에, DeepSeek·GLM 등 오픈웨이트가 벤치마크 상위권에 진입"),
        ("신뢰 격차의 지속", "채택률은 84%까지 올라갔지만 신뢰도는 29%로 하락 — '거의 맞는' 코드에 대한 검증 부담이 오히려 커짐"),
    ]
    for col, (title, desc) in zip(cols, items):
        with col:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(desc)


def s_forward() -> None:
    st.markdown("### 향후 전망")
    st.markdown(
        """
- **가격 경쟁 심화**: Cursor Composer 2.5, Gemini Flash 계열, 오픈웨이트 모델들이 "프론티어급
  성능을 훨씬 낮은 비용"으로 제공하며 가격 하단을 계속 끌어내릴 가능성
- **에이전트 오케스트레이션의 표준화**: MCP 같은 프로토콜, Hooks/Specs 같은 거버넌스 장치가
  더 널리 채택되며 "여러 에이전트를 안전하게 조합하는 법"이 다음 경쟁 축이 될 가능성
- **소유권 지형의 유동성 지속**: Windsurf 사례처럼 인수·라이선스·리브랜딩이 반복될 수 있어,
  특정 도구에 대한 조직 차원의 과도한 락인은 리스크로 작용할 수 있음
- **한국 시장의 중요도 상승**: Anthropic의 서울 오피스 개설 등, 국내가 더 이상 '해외 도구를
  뒤늦게 받아들이는' 시장이 아니라 초기 성장 시장으로 다뤄지는 신호
        """
    )


def s_conclusion() -> None:
    st.markdown("### 결론")
    with st.container(border=True):
        st.markdown(
            """
**"어떤 AI 코딩 도구를 쓸 것인가"보다 중요한 질문은 "AI가 대신해줄수록,
사람만이 할 수 있는 판단력을 어떻게 계속 키울 것인가"입니다.**

컨텍스트를 설계하고, AI 산출물을 비판적으로 검증하고, 도구를 작업 성격에 맞게 조합하는 능력 —
이 세 가지가 2026년 이후에도 변하지 않을 핵심 경쟁력으로 보입니다.
            """
        )
    st.divider()
    st.caption(
        "이 대시보드의 수치·사실관계는 2026년 9월 딥리서치(웹 검색 25건+ 및 YouTube oEmbed 검증) "
        "기반이며, 일부 가격·시장 규모·벤치마크 수치는 집계 블로그 출처로 각 페이지에 명시했습니다. "
        "실제 의사결정 전에는 각 사 공식 자료로 재확인을 권장합니다."
    )


slide_deck(
    "outlook",
    [
        ("지금까지 다룬 것", s_recap),
        ("핵심 트렌드 3가지", s_three_trends),
        ("향후 전망", s_forward),
        ("결론", s_conclusion),
    ],
)
