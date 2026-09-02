import pandas as pd
import streamlit as st

from utils.data import SWE_BENCH_NOTE, SWE_BENCH_VERIFIED, VIDEOS_KR
from utils.slides import slide_deck


def s_overview() -> None:
    st.markdown(
        """
### GPT-5.3-Codex — OpenAI의 최신 코딩 특화 모델

**2026년 2월 5일** 출시되었으며, 2026년 1월 출시된 GPT-5.2-Codex의 후속 모델입니다.
OpenAI는 GPT-5.2-Codex를 "가장 발전된 에이전틱 코딩 모델"로 소개했고, 5.3 세대에서는
다음이 개선되었다고 알려져 있습니다.
        """
    )
    with st.container(horizontal=True):
        st.metric("장시간 작업", "컨텍스트 압축 개선", border=True)
        st.metric("대규모 리팩터링", "마이그레이션 지원 강화", border=True)
        st.metric("플랫폼", "Windows 지원 강화", border=True)
        st.metric("보안", "사이버보안 역량 강화", border=True)
    st.divider()
    kr_video = VIDEOS_KR[7]
    st.markdown("**🎥 참고 영상**")
    st.video(kr_video["url"])
    st.caption(f"{kr_video['title']} · {kr_video['channel']}")


def s_lineup_pricing() -> None:
    st.markdown("### 2026년 라인업 & 참고 가격")
    df = pd.DataFrame(
        {
            "모델": ["GPT-5 (base)", "GPT-5.2-Codex", "GPT-5.3-Codex", "GPT-5.6 'Sol'/5.5", "GPT-5.6 'Terra'", "GPT-5.6 'Luna' (경량)"],
            "시점": ["2025", "2026-01", "2026-02", "2026 중반", "2026 중반", "2026 중반"],
            "포지셔닝": ["범용 기본형", "코딩 특화 1세대", "코딩 특화 2세대(최신)", "최상위 성능", "중간 티어", "저비용 대량 처리"],
        }
    )
    st.dataframe(df, hide_index=True, width="stretch")
    st.warning(
        "2026년 9월 시점의 '진짜 최신' Codex/GPT-5.x 세부 버전명은 출처마다 표기가 달라 "
        "이 리서치에서 확정하지 못했습니다 (OpenAI 공식 페이지 재확인 권장). "
        "가격도 3rd-party 집계 기준 근사치입니다.",
        icon=":material/warning:",
    )


def s_agent_style() -> None:
    st.markdown(
        """
### Codex의 에이전트 스타일: "비동기 클라우드 샌드박스"

Claude Code가 터미널에서 개발자와 실시간으로 대화하며 작업하는 스타일이라면, Codex는
**ChatGPT 구독에 번들**되어 클라우드 샌드박스에서 작업을 맡기고(fire-and-forget), 완료되면
결과를 받아보는 **비동기형 워크플로**에 강점이 있다는 평가가 많습니다.

- ChatGPT 하나의 요금제로 채팅과 에이전트를 함께 사용 가능 (OpenAI 생태계 사용자에게 유리)
- 클라우드 샌드박스에서 격리 실행 → 로컬 환경 오염 없이 여러 작업을 동시에 위임 가능
- 국내 사용자 코멘트: "오래 걸리는 백엔드 작업은 Codex에 맡기고, 그 사이 다른 도구로 화면 작업"
  이라는 패턴이 자주 언급됩니다.
        """
    )


def s_benchmark() -> None:
    st.markdown("### 벤치마크 스냅샷 (SWE-bench Verified, 2026-04)")
    st.bar_chart(SWE_BENCH_VERIFIED, x="모델", y="점수(%)", horizontal=True)
    st.caption(SWE_BENCH_NOTE)
    st.info(
        "OpenAI는 2026년 2월부터 SWE-bench Verified 점수를 공식적으로 공개하지 않아, "
        "GPT-5.3-Codex 이후 모델은 이 차트에 최신 수치를 반영하지 못했습니다.",
        icon=":material/info:",
    )


def s_positioning() -> None:
    st.markdown("### 한 줄 포지셔닝")
    with st.container(border=True):
        st.markdown(
            "**\"ChatGPT 생태계 안에서, 비동기로 많은 작업을 동시에 맡기고 싶은 사용자\"**"
        )
        st.caption(
            "OpenAI 계정/구독을 이미 쓰고 있고, 채팅과 에이전틱 코딩을 하나의 결제/컨텍스트로 "
            "묶고 싶은 팀·개인에게 특히 매력적이라는 평가가 2026년 비교 콘텐츠에서 반복적으로 등장합니다."
        )


slide_deck(
    "codex",
    [
        ("GPT-5.3-Codex 개요", s_overview),
        ("2026년 라인업 & 가격", s_lineup_pricing),
        ("에이전트 스타일: 비동기 클라우드", s_agent_style),
        ("벤치마크 스냅샷", s_benchmark),
        ("한 줄 포지셔닝", s_positioning),
    ],
)
