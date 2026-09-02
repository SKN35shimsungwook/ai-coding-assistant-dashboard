import pandas as pd
import streamlit as st

from utils.data import (
    CLAUDE_CODE_KR_GROWTH,
    CLAUDE_CODE_KR_GROWTH_NOTE,
    CURSOR_ARR_GROWTH,
    CURSOR_ARR_GROWTH_NOTE,
)
from utils.slides import slide_deck


def s_stackoverflow() -> None:
    st.markdown("### Stack Overflow 개발자 서베이 — 채택은 늘고, 신뢰는 줄고")
    with st.container(horizontal=True):
        st.metric("AI 도구 사용/사용 예정", "84%", border=True)
        st.metric("매일 AI 도구 사용", "51%", border=True)
        st.metric("AI 정확도 신뢰", "29%", "-11%p YoY", delta_color="inverse", border=True)
        st.metric("적극적 불신", "46%", border=True)
    st.markdown(
        """
- 가장 큰 불만(**45%**): "거의 맞는데 딱 맞지는 않는" AI 출력 — **66%**가 이런 코드를
  고치는 데 오히려 이전보다 시간을 더 쓴다고 응답
- 그럼에도 **75%**는 AI 답을 믿지 못할 때 결국 사람에게 물어본다고 응답
- 도구 인지도: ChatGPT 82%, GitHub Copilot 68%, **Cursor 18%**(첫 등장), **Claude Code 10%**(첫 등장)
        """
    )
    st.caption("출처: Stack Overflow 2025/2026 Developer Survey")


def s_market_size() -> None:
    st.markdown("### 시장 규모 & 도구별 점유율")
    st.metric("AI 코딩 어시스턴트 시장 규모 (2026 추정)", "$12.8B", "+65% YoY", border=True)
    st.caption("집계 블로그 출처 — 1차 자료로 재확인되지 않은 추정치입니다 (UNVERIFIED).")

    df = pd.DataFrame(
        {
            "도구": ["GitHub Copilot", "Cursor", "Claude Code"],
            "전문 개발자 점유율(%)": [51, 18, 10],
        }
    )
    st.bar_chart(df, x="도구", y="전문 개발자 점유율(%)", horizontal=True)
    st.markdown(
        """
- **GitHub Copilot**: 전문 개발자 점유율 67%→51%로 하락 보도(경쟁 심화), 그러나 여전히
  전체 사용자 2,000만+ 로 최대 설치 기반 유지
- **Cursor**: 2026-03 기준 연환산매출(ARR) **$2B** 돌파 (2025-11 $1B 대비 2배)
- **Claude Code**: 서베이 첫 등장에 10%, 별도 집계로는 9개월 만에 사용률 6배 성장, 글로벌
  업무 채택률 18%, **고객만족도(CSAT) 91%**로 조사 대상 중 최고 충성도
        """
    )


def s_growth() -> None:
    st.markdown("### 성장 곡선: 두 개의 급성장 스토리")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Claude Code 한국 MAU 지수**")
        st.area_chart(CLAUDE_CODE_KR_GROWTH, x="월", y="MAU 지수 (1개월 전=1.0)")
        st.caption(CLAUDE_CODE_KR_GROWTH_NOTE)
    with col2:
        st.markdown("**Cursor 연환산매출(ARR)**")
        st.line_chart(CURSOR_ARR_GROWTH, x="시점", y="ARR ($B)")
        st.caption(CURSOR_ARR_GROWTH_NOTE)
    st.info(
        "두 회사 모두 '기존 도구를 대체'하기보다 '새로운 사용층을 빠르게 흡수'하는 방식으로 "
        "성장하고 있다는 해석이 2026년 보도에서 공통적으로 등장합니다.",
        icon=":material/trending_up:",
    )


def s_jetbrains() -> None:
    st.markdown("### JetBrains 개발자 생태계 서베이 2026 (표본 10,000명+)")
    df = pd.DataFrame(
        {
            "도구": ["GitHub Copilot", "Cursor", "Claude Code"],
            "사용률(%)": [29, 18, 18],
            "'가장 좋아함' 응답률(%)": [9, 19, 46],
        }
    )
    st.dataframe(df, hide_index=True, width="stretch")
    st.info(
        "사용률은 Copilot이 가장 높지만, '가장 좋아하는 도구' 응답에서는 Claude Code가 46%로 "
        "압도적 1위 — 넓은 사용과 높은 만족도가 반드시 비례하지 않음을 보여줍니다.",
        icon=":material/favorite:",
    )


def s_korea() -> None:
    st.markdown("### 국내(한국) 동향")
    with st.container(horizontal=True):
        st.metric("Anthropic 서울(강남) 오피스", "2026년 초 개설", border=True)
        st.metric("한국 Claude Code MAU 성장", "약 6배 (4개월)", border=True)
        st.metric("'바이브 코딩' 월 검색량", "~40,000", border=True)
    st.markdown(
        """
- 한국은 Claude 사용량 기준 세계 상위 5개국 중 하나이자, 가장 활발한 Claude Code 개발자
  커뮤니티 중 하나로 언급됩니다 (출처: CIO Korea, 2026년 1~2월 보도)
- 국내 '바이브 코딩' 도구 순위에서 **Cursor, Claude Code, Antigravity, v0** 등이 상위 5개로
  자주 거론됩니다
- 한 블로그 추정(UNVERIFIED): 10인 팀의 Claude Code 팀 구독 비용이 월 ₩2백만~4백만원,
  생산성 향상 30~55% 주장, 2~3개월 내 비용 회수
        """
    )


def s_pattern() -> None:
    st.markdown("### 실사용 패턴: '자율성'을 기준으로 나뉜 시장")
    with st.container(border=True):
        st.markdown(
            "국내 커뮤니티에서 반복적으로 등장하는 구도는 **'AI가 알아서 끝까지 해주는가'**를 "
            "기준으로 한 두 그룹입니다."
        )
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**자율 · 심층 실행형**")
            st.caption("Claude Code, Codex — 복잡한 작업을 맡기고 결과를 검토")
        with col2:
            st.markdown("**보조 · 자동완성형**")
            st.caption("Copilot, Cursor Tab — 편집 흐름 속 실시간 제안")
    st.success(
        "실제 언급되는 조합: \"기획/화면은 Claude Code, 오래 걸리는 백엔드는 Codex\" — "
        "작업 성격별로 도구를 나눠 쓰는 것이 국내에서도 일반적인 패턴입니다.",
        icon=":material/insights:",
    )


slide_deck(
    "market",
    [
        ("Stack Overflow 서베이: 채택 vs 신뢰", s_stackoverflow),
        ("시장 규모 & 점유율", s_market_size),
        ("성장 곡선: 두 개의 급성장 스토리", s_growth),
        ("JetBrains 서베이: 사용률 vs 만족도", s_jetbrains),
        ("국내(한국) 동향", s_korea),
        ("실사용 패턴 사례", s_pattern),
    ],
)
