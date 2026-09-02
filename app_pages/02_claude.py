import pandas as pd
import streamlit as st

from utils.data import VIDEOS_KR
from utils.slides import slide_deck


def s_lineup() -> None:
    st.markdown("### Claude 모델 패밀리 (2026년 기준 최신 라인업)")
    df = pd.DataFrame(
        {
            "모델": ["Claude Opus 5", "Claude Sonnet 5", "Claude Haiku 4.5", "Claude Fable 5.1"],
            "포지셔닝": [
                "최고 지능 · 가장 어려운 에이전틱/추론 작업",
                "지능과 속도의 균형 · 코딩 기본값으로 널리 사용",
                "초저지연 · 고빈도/저비용 작업",
                "창작 · 스토리텔링 특화",
            ],
            "전형적 용도": [
                "복잡한 아키텍처 설계, 장시간 자율 에이전트 작업",
                "일상적 코딩, Claude Code의 기본 모델",
                "간단한 서브에이전트, 대량 병렬 호출",
                "콘텐츠/내러티브 생성",
            ],
        }
    )
    st.dataframe(df, hide_index=True, width="stretch")
    st.caption("모델 ID 예: claude-opus-5, claude-sonnet-5, claude-haiku-4-5-20251001, claude-fable-5-1")


def s_claude_code() -> None:
    st.markdown(
        """
### Claude Code — 터미널 네이티브 에이전트

Anthropic이 만든 CLI 기반 코딩 에이전트로, IDE 플러그인이 아니라 **터미널에서 직접
개발자와 협업**하도록 설계되었습니다. 저장소를 읽고, 계획을 세우고, 파일을 수정하고,
셸 명령을 실행하고, 테스트를 돌리고, 커밋/PR까지 만드는 전 과정을 하나의 세션에서 수행합니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("실행 위치", "터미널 / SDK / IDE 확장", border=True)
        st.metric("배포 형태", "CLI · Claude Agent SDK · 데스크톱", border=True)
        st.metric("권한 모델", "승인 기반 (Plan Mode 포함)", border=True)
    st.divider()
    kr_video = VIDEOS_KR[2]
    st.markdown("**🎥 참고 영상**")
    st.video(kr_video["url"])
    st.caption(f"{kr_video['title']} · {kr_video['channel']}")


def s_subagents() -> None:
    st.markdown(
        """
### 서브에이전트 & 병렬 작업

Claude Code는 하나의 큰 작업을 **독립된 서브에이전트**로 위임할 수 있습니다. 각
서브에이전트는 별도의 컨텍스트 창을 가지며, 조사·구현·리뷰처럼 성격이 다른 작업을 병렬로
처리한 뒤 결과만 메인 세션에 보고합니다. 이를 통해 메인 컨텍스트를 오염시키지 않고도
대규모 코드베이스 탐색이나 다각도 리서치를 수행할 수 있습니다.
        """
    )
    with st.container(border=True):
        st.markdown("**예시 워크플로**")
        st.markdown(
            "1. 탐색 서브에이전트가 코드베이스에서 관련 파일을 찾음\n"
            "2. 리서치 서브에이전트가 웹에서 최신 API 문서를 확인\n"
            "3. 메인 세션이 두 결과를 종합해 구현 계획을 세우고 실행\n"
            "4. 리뷰 서브에이전트(또는 별도 명령)가 변경 사항을 검증"
        )


def s_extensibility() -> None:
    st.markdown("### 확장성: MCP · Skills · Hooks")
    cols = st.columns(3)
    items = [
        ("MCP (Model Context Protocol)", "Anthropic이 제안한 개방형 표준. 외부 도구·데이터소스(DB, 브라우저, 사내 시스템)를 표준화된 방식으로 에이전트에 연결."),
        ("Skills", "재사용 가능한 작업 절차(플레이북)를 패키징해 필요할 때 로드. 팀·조직 단위로 워크플로를 표준화 가능."),
        ("Hooks", "특정 이벤트(툴 호출 전후 등)에 셸 명령을 실행해 검증·로깅·정책 강제를 자동화."),
    ]
    for col, (title, desc) in zip(cols, items):
        with col:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.caption(desc)


def s_persistence() -> None:
    st.markdown(
        """
### Artifacts, 메모리, 세션 지속성

- **Artifacts** — 대화 밖에서 독립적으로 렌더링/공유되는 산출물(웹앱, 문서, 시각화)을
  만들고, 실시간 협업이 필요하면 상태 저장·댓글 등 런타임 기능까지 붙일 수 있습니다.
- **파일 기반 메모리** — 세션 간 사용자 선호·프로젝트 맥락을 파일로 축적해, 다음 대화에서
  같은 설명을 반복하지 않도록 합니다.
- **백그라운드 작업 & 예약 실행** — 장시간 작업을 백그라운드로 돌리고, 완료 시 알림을 받거나
  다음 실행 시각을 스스로 예약하는 자율 루프를 구성할 수 있습니다.
        """
    )


def s_safety() -> None:
    st.markdown("### 안전장치 & 협업 모델")
    st.markdown(
        """
Claude Code는 되돌리기 어렵거나 범위가 넓은 행동(강제 푸시, 원격 삭제, 비밀 값 커밋 등)을
**기본적으로 확인 요청**하도록 설계되어 있고, 사용자가 명시적으로 자율성을 허용한 범위 안에서만
확인 없이 진행합니다. 이는 "빠르게 많은 걸 대신 해주되, 되돌릴 수 없는 결정은 사람이 승인한다"는
철학을 반영합니다.
        """
    )
    st.warning(
        "이 페이지는 Claude Code 자체의 설계·기능에 대한 1차 지식을 기반으로 작성했습니다. "
        "가격·벤치마크 등 외부 수치는 '기능·성능 비교' 세션에서 리서치 출처와 함께 다룹니다.",
        icon=":material/verified:",
    )


slide_deck(
    "claude",
    [
        ("Claude 모델 패밀리", s_lineup),
        ("Claude Code란 무엇인가", s_claude_code),
        ("서브에이전트 & 병렬 작업", s_subagents),
        ("확장성: MCP · Skills · Hooks", s_extensibility),
        ("Artifacts · 메모리 · 지속성", s_persistence),
        ("안전장치 & 협업 모델", s_safety),
    ],
)
