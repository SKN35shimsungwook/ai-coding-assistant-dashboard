import pandas as pd
import streamlit as st

from utils.slides import slide_deck


def s_definition() -> None:
    st.markdown(
        """
**AI 코딩 어시스턴트**란 대형언어모델(LLM)을 기반으로 코드 작성·수정·테스트·디버깅·
배포까지의 개발 워크플로를 보조하거나 대신 수행하는 도구를 말합니다.

2021년 GitHub Copilot의 "한 줄 자동완성"에서 출발해, 2026년 현재는 터미널/IDE에서
스스로 파일을 읽고 계획을 세우고 명령을 실행하며 PR까지 올리는 **에이전틱(agentic) 코딩**
도구로 진화했습니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("자동완성 시대", "2021~2022", border=True)
        st.metric("챗 기반 시대", "2022~2023", border=True)
        st.metric("에이전틱 시대", "2024~현재", border=True)


def s_evolution() -> None:
    df = pd.DataFrame(
        {
            "단계": ["자동완성", "챗 어시스턴트", "코드베이스 인지", "에이전틱 실행", "멀티에이전트 오케스트레이션"],
            "특징": [
                "한 줄/한 블록 제안 (Copilot 초기)",
                "대화창에서 질문·설명·리팩터링 제안",
                "레포 전체 맥락을 읽고 답변 (RAG/긴 컨텍스트)",
                "직접 파일 수정, 명령 실행, 테스트, 커밋까지 수행",
                "여러 서브에이전트가 계획을 나눠 병렬로 작업",
            ],
            "대표 시점": ["2021", "2022–2023", "2023–2024", "2024–2025", "2025–2026"],
        }
    )
    st.dataframe(df, hide_index=True, width="stretch")
    st.caption("현재 Claude Code, Codex CLI, Cursor Agent, Devin 등은 대부분 '에이전틱 실행' 이상 단계에 있습니다.")


def s_vibe_coding() -> None:
    st.markdown(
        """
### "바이브 코딩(Vibe Coding)"

2025년부터 널리 쓰인 표현으로, 개발자가 **세부 문법보다 의도와 결과에 집중**하고
AI 에이전트가 실제 구현을 담당하는 개발 방식을 뜻합니다. Andrej Karpathy가 2025년 초
소셜미디어에서 이 표현을 대중화한 것으로 알려져 있습니다.

- 장점: 프로토타이핑 속도, 비전공자의 진입장벽 완화, 반복 작업 자동화
- 위험: 검증 없는 수용(review 부재), 보안/성능 이해 결핍, "동작하지만 이해 못하는 코드"
        """
    )
    st.info("이 대시보드의 3부 '키워야 할 역량'에서 바이브 코딩 시대에 오히려 더 중요해진 스킬을 다룹니다.", icon=":material/lightbulb:")


def s_why_now() -> None:
    st.markdown("### 왜 2026년이 변곡점인가")
    with st.container(horizontal=True):
        with st.container(border=True):
            st.markdown("**긴 컨텍스트 + 저비용 추론**")
            st.caption("레포 전체를 한 번에 읽고, 반복 호출 비용이 크게 낮아짐")
        with st.container(border=True):
            st.markdown("**도구 사용(Tool Use)의 성숙**")
            st.caption("파일시스템·터미널·브라우저·MCP 표준화로 '실행형' 에이전트가 보편화")
        with st.container(border=True):
            st.markdown("**검증 루프의 자동화**")
            st.caption("테스트 실행 → 실패 확인 → 자가 수정까지 폐루프 작업이 가능해짐")


def s_map() -> None:
    st.markdown("### 이 대시보드가 다루는 도구 지도")
    groups = {
        "빅테크 · 프론티어 모델사": ["Anthropic (Claude / Claude Code)", "OpenAI (Codex / ChatGPT)", "Google (Gemini / Antigravity / Jules)"],
        "IDE·에디터 특화": ["Cursor", "Windsurf (Codeium)", "GitHub Copilot"],
        "완전 자율 에이전트": ["Cognition Devin", "Replit Agent", "Amazon Q Developer / Kiro"],
        "오픈소스 · 신흥 주자": ["오픈소스 코딩 모델 (Qwen, DeepSeek 등)", "xAI Grok Code 계열"],
    }
    cols = st.columns(2)
    for i, (group, items) in enumerate(groups.items()):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{group}**")
                for it in items:
                    st.markdown(f"- {it}")
    st.caption("세부 최신 스펙과 출처는 다음 세션들(Claude / Codex / Gemini / 그 외)에서 다룹니다.")


slide_deck(
    "intro",
    [
        ("AI 코딩 어시스턴트란", s_definition),
        ("진화의 역사: 자동완성 → 에이전트", s_evolution),
        ("바이브 코딩이란 무엇인가", s_vibe_coding),
        ("왜 지금이 변곡점인가", s_why_now),
        ("이 대시보드가 다루는 도구 지도", s_map),
    ],
)
