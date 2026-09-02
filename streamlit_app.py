import streamlit as st

st.set_page_config(
    page_title="AI 코딩 어시스턴트 2026 — 사업 설명회",
    page_icon=":material/rocket_launch:",
    layout="wide",
)

if "deck_progress" not in st.session_state:
    st.session_state.deck_progress = {}

pages = st.navigation(
    {
        "": [
            st.Page("app_pages/00_cover.py", title="표지 & 목차", icon=":material/home:"),
        ],
        "1부 · 지형도": [
            st.Page("app_pages/01_intro.py", title="AI 코딩 어시스턴트란", icon=":material/travel_explore:"),
            st.Page("app_pages/02_claude.py", title="Claude / Claude Code", icon=":material/auto_awesome:"),
            st.Page("app_pages/03_codex.py", title="OpenAI Codex", icon=":material/smart_toy:"),
            st.Page("app_pages/04_gemini.py", title="Google Gemini", icon=":material/diamond:"),
            st.Page("app_pages/05_others.py", title="그 외 플레이어들", icon=":material/apps:"),
        ],
        "2부 · 정면 비교": [
            st.Page("app_pages/06_compare.py", title="기능·성능 비교", icon=":material/balance:"),
            st.Page("app_pages/07_timeline.py", title="모델 타임라인", icon=":material/timeline:"),
            st.Page("app_pages/08_market.py", title="시장 & 채택 동향", icon=":material/monitoring:"),
        ],
        "3부 · 더 보기 & 전망": [
            st.Page("app_pages/09_youtube.py", title="유튜브 딥리서치", icon=":material/play_circle:"),
            st.Page("app_pages/10_skills.py", title="키워야 할 역량", icon=":material/fitness_center:"),
            st.Page("app_pages/11_outlook.py", title="전망 & 결론", icon=":material/flag:"),
        ],
    },
    position="sidebar",
)

with st.sidebar:
    st.caption("AI CODING ASSISTANTS · 2026")
    st.progress(1.0, text="총 66개 슬라이드 · 12개 세션")
    st.caption("직접 만든 리서치 대시보드 · Streamlit")

pages.run()
