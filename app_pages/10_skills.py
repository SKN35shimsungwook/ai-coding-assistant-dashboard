import pandas as pd
import streamlit as st

from utils.slides import slide_deck


def s_context_engineering() -> None:
    st.markdown(
        """
### ① 프롬프트 엔지니어링 → 컨텍스트 엔지니어링

2026년 여러 소스가 공통적으로 꼽는 최우선 역량은 "질문을 잘 던지는 능력"이 아니라
**"AI가 신뢰할 만한 결과를 내도록 입력·제약·도메인 지식·출력 기대치를 설계하는 능력"**,
즉 컨텍스트 엔지니어링입니다.
        """
    )
    df = pd.DataFrame(
        {"조건": ["컨텍스트 파일 없음", "잘 만든 컨텍스트 파일 있음"], "작업 성공률(%)": [30, 90]}
    )
    st.bar_chart(df, x="조건", y="작업 성공률(%)", horizontal=True)
    st.caption("2026년 한 연구에서 여러 코딩 에이전트를 대상으로 측정 (CLAUDE.md류 컨텍스트/스티어링 문서 유무 비교).")


def s_skill_erosion() -> None:
    st.markdown("### ② AI 보조가 실력 형성을 해칠 수 있다 — Anthropic 자체 연구")
    with st.container(horizontal=True):
        st.metric("개념 퀴즈 점수 하락", "-17%", delta_color="inverse", border=True)
        st.metric("가장 큰 격차 영역", "디버깅", border=True)
    st.markdown(
        """
Anthropic의 연구("How AI assistance impacts the formation of coding skills")는 무작위
대조 실험에서 **AI 보조를 받은 그룹이 방금 사용한 개념에 대한 퀴즈에서 17% 낮은 점수**를
받았다는 결과를 발표했습니다. 특히 **디버깅 능력** 격차가 가장 컸는데, 이는 AI 보조가
"틀린 코드를 스스로 알아채는 능력"을 특히 약화시킬 수 있음을 시사합니다.
        """
    )
    st.info(
        '"In an AI-augmented workplace, productivity gains matter, but so does the long-term '
        'development of the expertise those gains depend on." — Anthropic',
        icon=":material/format_quote:",
    )


def s_usage_pattern() -> None:
    st.markdown("### ③ '어떻게' 쓰는지가 실력을 가른다")
    df = pd.DataFrame(
        {
            "AI 활용 방식": ["개념 질문에 AI 활용 (스파링 파트너)", "코드 생성 전면 위임 (오토파일럿)"],
            "후속 평가 점수(%)": [65, 40],
        }
    )
    st.bar_chart(df, x="AI 활용 방식", y="후속 평가 점수(%)", horizontal=True)
    st.caption("2차 출처 인용 · 주니어 엔지니어 52명 대상 조사. AI를 개념 이해의 스파링 파트너로 쓴 그룹이 코드 생성을 전면 위임한 그룹보다 후속 평가에서 유의미하게 높은 점수를 받았습니다.")
    st.warning("표본이 크지 않아 일반화에는 주의가 필요하지만, 방향성 자체는 Anthropic 연구 결과와 일치합니다.", icon=":material/warning:")


def s_code_review() -> None:
    st.markdown("### ④ AI 산출물에 대한 코드리뷰 · 검증 규율")
    st.markdown(
        """
PR의 상당 비중이 AI 생성 코드로 채워지는 시대, 가장 큰 위험은 **리뷰어의 고무도장(rubber-stamp)화**입니다.
"AI가 만든 코드는 문법적으로 완벽하고 스타일도 일관되지만, 완전히 틀릴 수 있다"는 경고가
2026년 리뷰 관련 콘텐츠에서 반복적으로 등장합니다.
        """
    )
    cols = st.columns(2)
    with cols[0]:
        with st.container(border=True):
            st.markdown("**리뷰 시 우선 점검 (보안)**")
            st.markdown("하드코딩된 비밀값 · SQL 인젝션 · XSS · 인증 우회 · OWASP Top 10")
    with cols[1]:
        with st.container(border=True):
            st.markdown("**검증 도구/기법**")
            st.markdown("Property-based testing(엣지케이스 포착) · Mutation testing(테스트 자체의 유효성 검증)")


def s_domain_rag_agentic() -> None:
    st.markdown("### ⑤ 도메인 전문성 · RAG 설계 · 에이전틱 워크플로 설계")
    cols = st.columns(3)
    items = [
        ("도메인 전문성 + AI 유창성", "\"프롬프트만 잘하는 제너럴리스트\"보다 \"프롬프트도 잘하는 도메인 전문가\"가 항상 우위"),
        ("RAG 시스템 설계", "조직 고유 데이터에 AI 출력을 근거(grounding)시키는 능력 — 2026년 가장 레버리지가 큰 AI 엔지니어링 스킬로 꼽힘"),
        ("에이전틱 워크플로 설계", "서브에이전트/멀티에이전트 파이프라인, 가드레일, 인계 지점 설계 — Claude Code Subagents, Copilot Coding Agent, Kiro Hooks/Specs 등에서 요구되는 역량"),
    ]
    for col, (title, desc) in zip(cols, items):
        with col:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(desc)


def s_roadmap() -> None:
    st.markdown("### 역량 로드맵 요약")
    df = pd.DataFrame(
        {
            "역량": [
                "컨텍스트 엔지니어링",
                "AI 산출물 코드리뷰·검증",
                "보안 리뷰 규율",
                "에이전틱 워크플로 설계",
                "도메인 전문성",
                "RAG/시스템 설계",
                "기초 디버깅력 유지",
            ],
            "2026년 중요도": [95, 92, 88, 85, 90, 82, 90],
        }
    )
    st.dataframe(
        df,
        hide_index=True,
        width="stretch",
        column_config={
            "2026년 중요도": st.column_config.ProgressColumn(
                "2026년 중요도", min_value=0, max_value=100, format="%d"
            )
        },
    )
    st.success("공통 결론: \"AI 산출물에 대한 비판적 평가·검증\"은 2026년 거의 모든 출처에서 '타협 불가' 역량으로 꼽힙니다.", icon=":material/verified:")


slide_deck(
    "skills",
    [
        ("① 컨텍스트 엔지니어링", s_context_engineering),
        ("② AI 보조와 실력 형성", s_skill_erosion),
        ("③ 어떻게 쓰는지가 가른다", s_usage_pattern),
        ("④ 코드리뷰 · 검증 규율", s_code_review),
        ("⑤ 도메인 · RAG · 에이전틱 설계", s_domain_rag_agentic),
        ("역량 로드맵 요약", s_roadmap),
    ],
)
