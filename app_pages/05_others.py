import streamlit as st

from utils.data import TOOL_DEMO_VIDEOS
from utils.slides import slide_deck


def _demo_videos(key: str) -> None:
    st.markdown("**🎥 참고 영상**")
    cols = st.columns(2)
    for col, v in zip(cols, TOOL_DEMO_VIDEOS[key]):
        with col:
            st.video(v["url"])
            st.caption(f"{v['title']} · {v['channel']}")


def s_cursor() -> None:
    st.markdown(
        """
### Cursor — IDE 네이티브 에이전트

VS Code 포크 기반 에디터로, 에이전트가 대화창이 아니라 **에디터 안에서 직접 살아 움직이는**
경험을 제공합니다. 자체 에이전트 모델 **Composer 2.5**(2026-05 출시)는 "저비용으로
비슷한 품질"을 표방하며 $0.50 / $2.50 (input/output, $/M)로 가격이 책정되어 있습니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("Pro", "$20/mo", border=True)
        st.metric("Pro+", "$60/mo", border=True)
        st.metric("Ultra", "$200/mo", border=True)
        st.metric("Teams", "$40~120/seat", border=True)
    st.caption("2026-03 기준 $2B 연환산매출(ARR) 돌파로 보도됨 (2025-11 $1B 대비 2배 성장).")
    st.divider()
    _demo_videos("cursor")


def s_copilot() -> None:
    st.markdown(
        """
### GitHub Copilot — 가장 넓은 설치 기반

VS Code·JetBrains·GitHub.com 등 개발자가 이미 있는 곳에 그대로 들어와 있는 것이 최대 강점.
2026년 3월 **Agent Mode**가 전체 사용자로 확대되었고 (MCP 지원 포함), 이슈를 할당하면
자동으로 PR을 만드는 **Coding Agent**, 다음 편집을 예측하는 **Next Edit Suggestions**를 제공합니다.
GPT·Claude·Gemini 모델을 상황에 맞게 자동 선택하는 멀티모델 라우팅도 특징입니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("사용자 기반", "2,000만+", border=True)
        st.metric("전문 개발자 점유율", "67%→51%", delta="-16%p", delta_color="inverse", border=True)
        st.metric("가격 체계", "2026-06 'AI Credits' 종량제 전환", border=True)
    st.divider()
    _demo_videos("copilot")


def s_devin_windsurf() -> None:
    st.markdown(
        """
### Cognition — Devin & Windsurf

- **Devin**: 2026-04 요금제 전면 개편으로 진입장벽을 크게 낮췄습니다 (기존 $500/mo 단일 플랜 →
  Free/Pro $20/Max $200/Teams 구조). 2026-07 **Devin Desktop**(탭 완성·인라인 편집)과
  **Devin Cloud**(클라우드 에이전트·DeepWiki·API)로 제품이 분리되었습니다.
- **Windsurf**: 2025-07 인수전에서 OpenAI의 약 $3B 인수 딜이 무산되고, Google이 핵심 인력과
  기술을 라이선스, **Cognition이 제품·브랜드·팀을 인수**했습니다. 2026-06 **"Devin Desktop"**으로
  리브랜딩되며 Cognition의 SWE-1.x 모델과 통합되었습니다.
        """
    )
    st.caption("Devin의 SWE-1.7 모델: 자체 하네스 기준 SWE-bench Multilingual 77.8%, Terminal-Bench 2.1 81.5% (벤더 발표치).")
    st.divider()
    _demo_videos("devin")


def s_replit() -> None:
    st.markdown(
        """
### Replit Agent — 프롬프트 하나로 풀스택 앱

**Agent 3**(2025-09)는 자율 실행 시간을 이전 세대 대비 약 10배 늘렸고, DB·인증·백엔드·프론트엔드를
포함한 풀스택 앱을 프롬프트 하나로 약 35분 만에 만들어낼 수 있다고 알려져 있습니다. 스스로 테스트를
작성·실행·수정하는 루프, 재사용 가능한 "Skills", Design Mode / Fast Build Mode를 지원합니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("Core", "$20/mo (크레딧 $20 포함)", border=True)
        st.metric("Pro", "$100/mo (최대 15명)", border=True)
    st.divider()
    _demo_videos("replit")


def s_aws_kiro() -> None:
    st.markdown(
        """
### AWS: Amazon Q Developer → Kiro

AWS는 **Amazon Q Developer 신규 가입을 2026-05-15부로 중단**했고 (IDE 플러그인 지원은
2027-04-30 종료 예정), 후속 제품으로 **Kiro**를 밀고 있습니다.

Kiro는 "스펙 주도(spec-driven)" 에이전틱 IDE로, **Specs · Hooks(파일 저장/PR 오픈 등 이벤트
트리거) · Steering 파일 · 커스텀 서브에이전트 · 조합형 'Powers'**가 핵심 구성 요소입니다.
Bedrock을 통해 추론이 필요한 스펙 작업은 Claude Sonnet, 대량 생성은 Amazon Nova로 라우팅합니다.
        """
    )
    st.divider()
    _demo_videos("kiro")


def s_open_source() -> None:
    st.markdown("### 오픈소스 · 신흥 도전자들")
    cols = st.columns(2)
    items = [
        ("xAI · Grok 4.5/4.6", "2026-07 발표, $2/$6 (M당), 토큰 효율 약 2배 표방. Terminal-Bench 2.1에서 Grok 4.6이 88.4%로 1위권."),
        ("Alibaba · Qwen3.6 / Qwen Code", "오픈소스 CLI 'Qwen Code' 제공. Qwen3.6-27B가 자체 발표로 Terminal-Bench 2.0에서 'Claude Opus 4.5급'이라 주장(미검증)."),
        ("DeepSeek V4", "1M 토큰 컨텍스트, SWE-bench Verified 80.6%. 프론티어 모델 대비 약 1/30 비용의 오픈웨이트로 주목."),
        ("Z.ai · GLM-5.3", "Terminal-Bench 2.1 88.2%. GLM-5.3-Flash(320B/18B, MIT 라이선스)는 Claude Opus 4.8과 0.7점 차 근접."),
    ]
    for i, (title, desc) in enumerate(items):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(desc)
    st.warning("오픈소스 진영 벤치마크 수치 상당수는 자체 발표(vendor-reported)로, 독립 검증 기관 재확인이 필요합니다.", icon=":material/warning:")


slide_deck(
    "others",
    [
        ("Cursor: IDE 네이티브 에이전트", s_cursor),
        ("GitHub Copilot: 최대 설치 기반", s_copilot),
        ("Cognition: Devin & Windsurf", s_devin_windsurf),
        ("Replit Agent: 프롬프트로 풀스택", s_replit),
        ("AWS: Amazon Q → Kiro", s_aws_kiro),
        ("오픈소스 · 신흥 도전자", s_open_source),
    ],
)
