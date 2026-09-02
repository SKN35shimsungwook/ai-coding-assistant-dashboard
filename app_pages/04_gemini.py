import pandas as pd
import streamlit as st

from utils.data import TOOL_DEMO_VIDEOS
from utils.slides import slide_deck


def s_lineup() -> None:
    st.markdown("### Gemini 3 모델 패밀리")
    df = pd.DataFrame(
        {
            "모델": ["Gemini 3 Pro / 3.1 Pro", "Gemini 3.7 Flash", "Gemini 3.1 Flash-Lite"],
            "포지셔닝": ["최고 성능 · 에이전틱 워크플로", "속도·비용 균형", "초저비용 대량 처리"],
            "Input $/M": [2.00, 0.75, 0.25],
            "Output $/M": [12.00, 3.75, 1.50],
        }
    )
    st.dataframe(df, hide_index=True, width="stretch")
    st.caption(
        "Gemini 3.7 Flash는 2026-08-13 도입가 기준(2027-01-01부터 2배 인상 예정). "
        "Gemini 3.1 Flash-Lite는 2026-10-16 Gemini 2.5 Flash-Lite 단종 이후 적용."
    )
    st.metric("SWE-bench Verified (Gemini 3.1 Pro, 2026-04)", "80.6%", border=True)


def s_jules() -> None:
    st.markdown(
        """
### Jules — 비동기 · 자율 · 레포 통합 에이전트

Google의 **완전 비동기 자율 코딩 에이전트**로, 저장소에 직접 통합되어 작업을 위임받으면
백그라운드에서 스스로 계획하고 실행합니다.

- Google AI 구독자에게 Gemini 3 Pro가 Jules에 통합 제공
- Ultra 티어부터 2026년 8월 롤아웃 시작, Pro 티어는 순차 확대
- Codex의 "비동기 샌드박스" 접근과 유사하게, 사람이 계속 붙어있지 않아도 되는 작업에 특화
        """
    )


def s_antigravity() -> None:
    st.markdown(
        """
### Antigravity — 에이전트 우선 개발 플랫폼

"Gemini 3 Antigravity"는 IDE라기보다 **에이전트에게 복잡한 개발 작업을 위임하는 것을
전제로 설계된 플랫폼**입니다. Gemini 3.1 Pro와 경량 Gemini 3 Flash를 함께 활용해
큰 작업은 Pro가, 반복적인 작업은 Flash가 처리하는 구조로 알려져 있으며,
"Antigravity 2.0"으로 계속 진화 중입니다.
        """
    )
    st.info("한국어 '바이브 코딩' 콘텐츠에서 Claude Code, Cursor와 함께 상위 5개 도구로 자주 언급됩니다.", icon=":material/trending_up:")


def s_demo_videos() -> None:
    st.markdown("### 실전 데모 영상: Antigravity")
    cols = st.columns(2)
    for col, v in zip(cols, TOOL_DEMO_VIDEOS["gemini"]):
        with col:
            with st.container(border=True):
                st.video(v["url"])
                st.markdown(f"**{v['title']}**")
                st.caption(v["channel"])


def s_positioning() -> None:
    st.markdown("### 한 줄 포지셔닝")
    with st.container(border=True):
        st.markdown("**\"Google 생태계 + 비동기 자율성을 원하는 팀\"**")
        st.caption(
            "Workspace/Cloud를 이미 쓰는 조직, 그리고 '사람이 지켜보지 않아도 되는' 백그라운드 "
            "작업 위임에 관심 있는 사용자에게 강점이 있다는 평가입니다."
        )
    st.warning("Gemini 3.x 세부 버전(3 Pro vs 3.1 Pro)과 벤치마크 시점이 출처마다 혼재되어 있어 참고용으로만 사용하세요.", icon=":material/warning:")


slide_deck(
    "gemini",
    [
        ("Gemini 3 모델 패밀리 & 가격", s_lineup),
        ("Jules: 비동기 자율 에이전트", s_jules),
        ("Antigravity: 에이전트 우선 플랫폼", s_antigravity),
        ("실전 데모 영상", s_demo_videos),
        ("한 줄 포지셔닝", s_positioning),
    ],
)
