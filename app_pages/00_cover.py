import streamlit as st

st.title(":material/rocket_launch: AI 코딩 어시스턴트, 2026")
st.caption("Claude · Codex · Gemini · Cursor 외 — 지형도, 정면 비교, 그리고 개발자가 지금 키워야 할 능력")

with st.container(horizontal=True):
    st.metric("커버 대상 도구", "10+", border=True)
    st.metric("세션(챕터)", "12", border=True)
    st.metric("총 슬라이드", "66", border=True)
    st.metric("기준일", "2026-09", border=True)

st.divider()

st.subheader(":material/menu_book: 목차")

toc = [
    ("1부 · 지형도", [
        "AI 코딩 어시스턴트란 — 개념과 왜 지금인가",
        "Claude / Claude Code 딥다이브",
        "OpenAI Codex 딥다이브",
        "Google Gemini 딥다이브",
        "Cursor · Copilot · Devin 등 그 외 플레이어",
    ]),
    ("2부 · 정면 비교", [
        "기능 · 성능 · 가격 비교",
        "최신 모델 타임라인 (2024→2026)",
        "시장 & 채택 동향 (국내/해외)",
    ]),
    ("3부 · 더 보기 & 전망", [
        "유튜브 딥리서치 — 국내 · 해외 레퍼런스",
        "개발자가 키워야 할 역량 로드맵",
        "향후 전망 & 결론",
    ]),
]

cols = st.columns(3)
for col, (part, items) in zip(cols, toc):
    with col:
        with st.container(border=True):
            st.markdown(f"**{part}**")
            for item in items:
                st.markdown(f"- {item}")

st.divider()
with st.container(border=True):
    st.markdown(
        "**이 대시보드 사용법** · 왼쪽 사이드바에서 세션을 고르고, 각 페이지 하단의 "
        "**이전 / 다음 / 슬라이드 이동** 컨트롤로 발표하듯 한 장씩 넘겨보세요."
    )
