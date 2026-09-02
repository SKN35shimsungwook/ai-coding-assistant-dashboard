import streamlit as st

from utils.data import TOOL_DEMO_VIDEOS, TOOL_DEMO_VIDEOS_NOTE, VIDEOS_INTL, VIDEOS_KR
from utils.slides import slide_deck


def _video_grid(videos: list[dict]) -> None:
    cols = st.columns(2)
    for i, v in enumerate(videos):
        with cols[i % 2]:
            with st.container(border=True):
                st.video(v["url"])
                st.markdown(f"**{v['title']}**")
                st.caption(v["channel"])


def s_method() -> None:
    st.markdown(
        """
### 왜, 그리고 어떻게 유튜브를 리서치했나

이 세션의 영상 30개는 검색만으로 그친 게 아니라, **YouTube oEmbed 엔드포인트로 제목·채널명을
직접 재조회**해 실제로 존재하고 현재도 접근 가능한 영상만 선별했습니다 (두 차례 리서치 패스:
1차 종합 비교 영상 18개 + 2차 도구별 데모 영상 12개). 그 과정에서 검색 결과가 암시했던 채널
귀속을 여러 건 재확인해 걸러냈습니다 — 다음 슬라이드에서 구체적인 사례를 보여드립니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("국내(한국어) 영상", "8개", border=True)
        st.metric("해외(영어) 영상", "10개", border=True)
        st.metric("도구별 데모 영상", "12개", border=True)
        st.metric("검증 방식", "oEmbed 직접 조회", border=True)


def s_kr_1() -> None:
    st.markdown("### 국내 레퍼런스 (1/2)")
    _video_grid(VIDEOS_KR[:4])


def s_kr_2() -> None:
    st.markdown("### 국내 레퍼런스 (2/2)")
    _video_grid(VIDEOS_KR[4:])


def s_intl_1() -> None:
    st.markdown("### 해외 레퍼런스 (1/2)")
    _video_grid(VIDEOS_INTL[:5])


def s_intl_2() -> None:
    st.markdown("### 해외 레퍼런스 (2/2)")
    _video_grid(VIDEOS_INTL[5:])


def s_tool_demos_1() -> None:
    st.markdown("### 도구별 데모 영상 (1/2): Gemini · Cursor · Copilot")
    for tool, label in [("gemini", "Google Gemini / Antigravity"), ("cursor", "Cursor"), ("copilot", "GitHub Copilot")]:
        st.markdown(f"**{label}**")
        _video_grid(TOOL_DEMO_VIDEOS[tool])
    st.caption(TOOL_DEMO_VIDEOS_NOTE)


def s_tool_demos_2() -> None:
    st.markdown("### 도구별 데모 영상 (2/2): Devin · Replit · Kiro")
    for tool, label in [("devin", "Cognition Devin"), ("replit", "Replit Agent"), ("kiro", "AWS Kiro")]:
        st.markdown(f"**{label}**")
        _video_grid(TOOL_DEMO_VIDEOS[tool])
    st.caption(TOOL_DEMO_VIDEOS_NOTE)


def s_verification() -> None:
    st.markdown("### 검증이 실제로 걸러낸 것들")
    st.markdown(
        "제목만 보면 유명 채널의 영상처럼 보였지만, oEmbed로 재조회하니 **실제로는 다른 채널의 "
        "영상**으로 밝혀져 제외한 사례들입니다. 검색 결과 제목만으로 출처를 단정하면 이런 오귀속이 "
        "쉽게 발생한다는 것을 보여줍니다."
    )
    cases = [
        ("\"My Claude Code Workflow for 2026\"", "IndyDevDan로 보였으나 실제로는 Ray Amjad 채널"),
        ("\"The Big Lie About the Claude Code and Cursor Leaderboard\"", "ThePrimeagen으로 보였으나 실제로는 Macro Lens 채널"),
        ("Matthew Berman 관련 검색 1건", "\"The Next New Thing\" 채널의 게스트 출연 영상이었음 (본인 채널 아님)"),
        ("AI Jason 관련 검색 2건", "각각 \"Enterprise Management 360\", \"Your Average Tech Bro\" 채널로 확인"),
        ("노마드코더 · 조코딩 등 국내 유명 채널 검색 다수", "\"AI 솔로프러너 랩\", \"편집자P\", \"짐코딩\" 등 유사 제목의 소규모 채널로 확인"),
    ]
    for claimed, actual in cases:
        with st.container(border=True):
            st.markdown(f"**검색상 추정**: {claimed}")
            st.caption(f"→ oEmbed 검증 결과: {actual}")
    st.success(
        "그래서 이 대시보드는 Fireship·조코딩·노마드코더 같은 유명 채널의 영상을 '추정'으로 끼워 "
        "넣지 않고, 실제로 검증된 30개만 싣습니다 — 완성도보다 정확도를 우선했습니다.",
        icon=":material/verified:",
    )


def s_takeaway() -> None:
    st.markdown("### 국내 vs 해외, 관점의 차이")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("**국내 콘텐츠의 결**")
            st.markdown(
                "- 입문/튜토리얼 비중이 높음 (\"설치부터\", \"왕초보 환영\")\n"
                "- 비개발자 대상 활용법(서비스 제작·판매) 강조\n"
                "- 생산성 격차·불안('바이브 코딩의 최후')에 대한 사회적 톤"
            )
    with col2:
        with st.container(border=True):
            st.markdown("**해외 콘텐츠의 결**")
            st.markdown(
                "- 압도적 다수가 **정면 비교형** (\"X vs Y vs Z\", 같은 앱 3번 만들어보기)\n"
                "- 도구의 내부 설계 철학·아키텍처 분석까지 파고드는 콘텐츠 존재\n"
                "- \"한 에이전트로는 부족하다\"처럼 멀티 에이전트 오케스트레이션을 다루는 심화 주제"
            )
    st.caption("Fireship, AI Explained 등도 2026년 AI 코딩 콘텐츠를 다루는 것은 확인되었지만, 이 주제만 다룬 개별 영상은 검증되지 않았습니다 (앞 슬라이드 참고).")


slide_deck(
    "youtube",
    [
        ("리서치 방법론", s_method),
        ("국내 레퍼런스 (1/2)", s_kr_1),
        ("국내 레퍼런스 (2/2)", s_kr_2),
        ("해외 레퍼런스 (1/2)", s_intl_1),
        ("해외 레퍼런스 (2/2)", s_intl_2),
        ("도구별 데모 (1/2)", s_tool_demos_1),
        ("도구별 데모 (2/2)", s_tool_demos_2),
        ("검증이 걸러낸 오귀속 사례", s_verification),
        ("국내 vs 해외 관점 차이", s_takeaway),
    ],
)
