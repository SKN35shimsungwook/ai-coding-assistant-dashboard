import pandas as pd
import streamlit as st

from utils.data import TIMELINE
from utils.slides import slide_deck


def _render_events(df) -> None:
    for _, row in df.iterrows():
        with st.container(border=True):
            c1, c2 = st.columns([1, 4])
            with c1:
                st.markdown(f"**{row['날짜']}**")
                st.caption(row["회사"])
            with c2:
                st.markdown(row["이벤트"])


def s_foundation() -> None:
    st.markdown("### 기반을 다진 시기 (2024 ~ 2025년 상반기)")
    _render_events(TIMELINE[TIMELINE["날짜"] < "2025-09"])


def s_h2_2025() -> None:
    st.markdown("### 에이전트 대중화의 시작 (2025년 하반기)")
    _render_events(TIMELINE[(TIMELINE["날짜"] >= "2025-09") & (TIMELINE["날짜"] < "2026-01")])


def s_h1_2026() -> None:
    st.markdown("### 릴리즈 러시 (2026년 상반기)")
    _render_events(TIMELINE[(TIMELINE["날짜"] >= "2026-01") & (TIMELINE["날짜"] < "2026-07")])


def s_h2_2026() -> None:
    st.markdown("### 최전선 (2026년 하반기, 현재까지)")
    _render_events(TIMELINE[TIMELINE["날짜"] >= "2026-07"])


def s_pace() -> None:
    st.markdown("### 릴리즈 속도, 숫자로 보기")
    quarter = pd.to_datetime(TIMELINE["날짜"], format="%Y-%m").dt.to_period("Q").astype(str)
    counts = quarter.value_counts().sort_index()
    cumulative = pd.DataFrame(
        {"분기": counts.index, "누적 주요 이벤트 수": counts.cumsum().values}
    )
    st.area_chart(cumulative, x="분기", y="누적 주요 이벤트 수")
    st.caption("이 대시보드가 추적한 19개 주요 이벤트를 분기별로 누적 집계한 것으로, 업계 전체 발표 건수가 아니라 이 타임라인 표본 기준입니다.")
    st.info("곡선의 기울기가 갈수록 가팔라지는 것 자체가 '릴리즈 주기 단축'을 시각적으로 보여줍니다.", icon=":material/speed:")


def s_insight() -> None:
    st.markdown("### 타임라인이 보여주는 3가지 패턴")
    with st.container(horizontal=True):
        with st.container(border=True):
            st.markdown("**① 릴리즈 주기 단축**")
            st.caption("주요 모델 세대 교체 간격이 2024년 반년 단위 → 2026년 분기~월 단위로 빨라짐")
        with st.container(border=True):
            st.markdown("**② 소유권 재편**")
            st.caption("Windsurf 인수전(OpenAI 무산→Google 라이선스→Cognition 인수), AWS Q Developer→Kiro 전환처럼 지형 자체가 유동적")
        with st.container(border=True):
            st.markdown("**③ 오픈웨이트의 추격**")
            st.caption("2026년 하반기 Terminal-Bench 2.1 상위권에 DeepSeek·GLM·Qwen 등 오픈웨이트 모델이 대거 진입")


slide_deck(
    "timeline",
    [
        ("기반을 다진 시기 (2024~2025 상반기)", s_foundation),
        ("에이전트 대중화 (2025 하반기)", s_h2_2025),
        ("릴리즈 러시 (2026 상반기)", s_h1_2026),
        ("최전선 (2026 하반기)", s_h2_2026),
        ("릴리즈 속도, 숫자로 보기", s_pace),
        ("타임라인이 보여주는 3가지 패턴", s_insight),
    ],
)
