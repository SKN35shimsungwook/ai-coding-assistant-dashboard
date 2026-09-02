import streamlit as st

from utils.data import (
    API_PRICING,
    API_PRICING_NOTE,
    CAPABILITY_PROFILE,
    CAPABILITY_PROFILE_NOTE,
    SUBSCRIPTION_PRICING,
    SWE_BENCH_NOTE,
    SWE_BENCH_VERIFIED,
    TERMINAL_BENCH,
    TERMINAL_BENCH_NOTE,
)
from utils.slides import slide_deck


def s_swe_bench() -> None:
    st.markdown("### SWE-bench Verified — 실제 GitHub 이슈 해결률")
    st.bar_chart(SWE_BENCH_VERIFIED, x="모델", y="점수(%)", horizontal=True)
    st.caption(SWE_BENCH_NOTE)


def s_terminal_bench() -> None:
    st.markdown("### Terminal-Bench 2.1 — 터미널 세션 전체 완수율")
    st.bar_chart(TERMINAL_BENCH, x="모델", y="점수(%)", horizontal=True)
    st.caption(TERMINAL_BENCH_NOTE)
    st.info(
        "두 벤치마크의 순위가 서로 다릅니다 — SWE-bench는 '이슈 해결', Terminal-Bench는 "
        "'터미널 세션 완수'를 측정하므로, 무엇을 '최고'로 볼지는 작업 성격에 따라 달라집니다.",
        icon=":material/insights:",
    )


def s_api_pricing() -> None:
    st.markdown("### API 가격 비교 (백만 토큰당 $)")
    st.bar_chart(API_PRICING, x="모델", y=["Input $/M", "Output $/M"], horizontal=True, stack=False)
    st.caption(API_PRICING_NOTE)


def s_sub_pricing() -> None:
    st.markdown("### 구독 요금제 비교")
    st.dataframe(SUBSCRIPTION_PRICING, hide_index=True, width="stretch")


def s_positioning() -> None:
    st.markdown("### 철학 · 포지셔닝 매트릭스")
    cols = st.columns(2)
    quadrants = [
        ("터미널 · CLI 우선", "Claude Code", "대규모 코드베이스에서의 깊은 추론·자율 계획에 강점. 개발자와 실시간 대화형 협업."),
        ("IDE · 에디터 우선", "Cursor · GitHub Copilot", "에디터 안에서 즉각적인 시각적 피드백. 일상적 편집 흐름을 끊지 않는 데 강점."),
        ("비동기 · 클라우드 샌드박스", "OpenAI Codex · Google Jules", "작업을 맡기고 나중에 결과를 확인. 사람이 계속 지켜볼 필요가 없는 작업에 강점."),
        ("완전 자율 · 스펙 주도", "Devin · AWS Kiro", "스펙/이슈를 던지면 끝까지 알아서 완수. 검증·거버넌스 체계가 함께 요구됨."),
    ]
    for i, (title, tools, desc) in enumerate(quadrants):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(f"대표: {tools}")
                st.caption(desc)


def s_capability_profile() -> None:
    st.markdown("### 역량 프로필: 5개 축으로 보는 4개 도구")
    st.bar_chart(
        CAPABILITY_PROFILE,
        x="역량 축",
        y=["Claude Code", "OpenAI Codex", "Cursor", "GitHub Copilot"],
        horizontal=True,
        stack=False,
    )
    st.caption(CAPABILITY_PROFILE_NOTE)
    st.markdown(
        """
- **Claude Code**는 추론·계획 깊이에서, **Cursor**는 IDE 밀착도에서, **Copilot**은 생태계
  통합도에서 각각 뚜렷한 강점을 보이는 구도로 요약됩니다.
- 어느 한 축도 모든 도구가 동시에 최고점을 받지 않는다는 점이 "멀티 툴 스태킹" 트렌드의
  근거이기도 합니다.
        """
    )


def s_multi_tool() -> None:
    st.markdown("### \"승자독식\"이 아니다 — 멀티 툴 스태킹이 표준")
    with st.container(horizontal=True):
        st.metric("2~4개 도구 동시 사용", "70%", border=True)
        st.metric("표본", "개발자 15,000명", border=True)
        st.metric("조사 시점", "2026-02", border=True)
    st.markdown(
        """
2026년 2월 The Pragmatic Engineer의 개발자 15,000명 대상 조사에 따르면, **응답자의 70%가
2~4개의 AI 코딩 도구를 동시에 사용**합니다. 자주 언급되는 조합 패턴:

- **Cursor**로 일상적인 편집 + **Claude Code**(터미널)로 깊은 디버깅·아키텍처·오케스트레이션 + **Copilot**으로 상시 자동완성
- (국내 사례) "기획/화면은 Claude Code, 오래 걸리는 백엔드는 Codex"
        """
    )
    st.success("결론: '어떤 도구가 최고인가'보다 '어떤 작업에 어떤 도구를 조합할 것인가'가 더 현실적인 질문입니다.", icon=":material/handshake:")


slide_deck(
    "compare",
    [
        ("SWE-bench Verified 비교", s_swe_bench),
        ("Terminal-Bench 2.1 비교", s_terminal_bench),
        ("API 가격 비교", s_api_pricing),
        ("구독 요금제 비교", s_sub_pricing),
        ("철학 · 포지셔닝 매트릭스", s_positioning),
        ("역량 프로필: 5개 축 비교", s_capability_profile),
        ("멀티 툴 스태킹이 표준", s_multi_tool),
    ],
)
