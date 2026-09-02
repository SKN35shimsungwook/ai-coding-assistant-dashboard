"""Shared reference data for the dashboard, drawn from the Sept 2026 deep-research pass.

Sources are mixed: some figures are vendor-confirmed, many are aggregator/blog
estimates that could not be independently re-verified in the research session.
Anything marked UNVERIFIED in a caption should be treated as approximate.
"""

from __future__ import annotations

import pandas as pd

# ---------------------------------------------------------------------------
# Benchmarks
# ---------------------------------------------------------------------------

SWE_BENCH_VERIFIED = pd.DataFrame(
    [
        {"모델": "Claude Opus 4.7", "회사": "Anthropic", "점수(%)": 87.6},
        {"모델": "GPT-5.3-Codex", "회사": "OpenAI", "점수(%)": 85.0},
        {"모델": "Gemini 3.1 Pro", "회사": "Google", "점수(%)": 80.6},
        {"모델": "DeepSeek V4-Pro", "회사": "DeepSeek (오픈웨이트)", "점수(%)": 80.6},
        {"모델": "Claude Opus 4.5", "회사": "Anthropic", "점수(%)": 80.9},
    ]
)
SWE_BENCH_NOTE = (
    "2026년 4월 스냅샷 (여러 2차 출처 종합). OpenAI는 2026년 2월부터 SWE-bench Verified 점수 공개를 "
    "중단해 최신 GPT-5.x/Codex와의 직접 비교가 어렵습니다. Claude Opus 5의 96~97%대 점수를 보도한 "
    "집계 사이트도 있으나 Anthropic 공식 자료로 재확인되지 않아 참고용으로만 표기합니다."
)

TERMINAL_BENCH = pd.DataFrame(
    [
        {"모델": "Grok 4.6", "회사": "xAI", "점수(%)": 88.4},
        {"모델": "GLM-5.3", "회사": "Z.ai", "점수(%)": 88.2},
        {"모델": "DeepSeek V4-Pro-0813", "회사": "DeepSeek", "점수(%)": 87.9},
        {"모델": "Qwen3.8 Max", "회사": "Alibaba", "점수(%)": 86.6},
        {"모델": "Claude Opus 4.8", "회사": "Anthropic", "점수(%)": 85.0},
        {"모델": "GLM-5.3-Flash", "회사": "Z.ai", "점수(%)": 84.3},
        {"모델": "Devin SWE-1.7*", "회사": "Cognition", "점수(%)": 81.5},
    ]
)
TERMINAL_BENCH_NOTE = (
    "2026-08-28 Terminal-Bench 2.1 리더보드 스냅샷. *Devin SWE-1.7 점수는 Cognition 자체 하네스로 "
    "측정한 벤더 발표치이며 독립 검증되지 않았습니다."
)

# ---------------------------------------------------------------------------
# Pricing
# ---------------------------------------------------------------------------

API_PRICING = pd.DataFrame(
    [
        {"모델": "Claude Sonnet 5 (출시가)", "Input $/M": 2.00, "Output $/M": 10.00},
        {"모델": "Claude Opus 4.8 (참고)", "Input $/M": 5.00, "Output $/M": 25.00},
        {"모델": "Claude Haiku 4.5", "Input $/M": 1.00, "Output $/M": 5.00},
        {"모델": "GPT-5 (base)", "Input $/M": 1.25, "Output $/M": 10.00},
        {"모델": "GPT-5.6 'Sol'/5.5", "Input $/M": 5.00, "Output $/M": 30.00},
        {"모델": "GPT-5.6 'Terra'", "Input $/M": 2.00, "Output $/M": 12.00},
        {"모델": "GPT-5.6 'Luna' (경량)", "Input $/M": 0.20, "Output $/M": 1.20},
        {"모델": "Gemini 3.1 Pro Preview", "Input $/M": 2.00, "Output $/M": 12.00},
        {"모델": "Gemini 3.7 Flash (도입가)", "Input $/M": 0.75, "Output $/M": 3.75},
        {"모델": "Gemini 3.1 Flash-Lite", "Input $/M": 0.25, "Output $/M": 1.50},
        {"모델": "Cursor Composer 2.5", "Input $/M": 0.50, "Output $/M": 2.50},
    ]
)
API_PRICING_NOTE = (
    "3rd-party 가격 집계 사이트 기준 근사치(2026년). 발표 시점/티어에 따라 달라질 수 있어 "
    "실제 계약 전 각 사 공식 가격 페이지 재확인을 권장합니다."
)

SUBSCRIPTION_PRICING = pd.DataFrame(
    [
        {"도구": "Claude Code / Claude.ai", "무료": "있음", "엔트리": "Pro (~$20/mo)", "미들": "—", "최상위(개인)": "Max", "팀/기업": "Enterprise"},
        {"도구": "Cursor", "무료": "있음", "엔트리": "Pro $20/mo", "미들": "Pro+ $60/mo", "최상위(개인)": "Ultra $200/mo", "팀/기업": "Teams $40~120/seat"},
        {"도구": "GitHub Copilot", "무료": "있음", "엔트리": "Pro $10/mo", "미들": "Pro+ $39/mo", "최상위(개인)": "Max $100/mo", "팀/기업": "Biz $19 · Ent $39/user"},
        {"도구": "Devin (Cognition)", "무료": "있음($0)", "엔트리": "Pro $20/mo", "미들": "—", "최상위(개인)": "Max $200/mo", "팀/기업": "Teams $80+$40/seat"},
        {"도구": "Replit Agent", "무료": "제한적", "엔트리": "Core $20/mo", "미들": "—", "최상위(개인)": "Pro $100/mo", "팀/기업": "Enterprise 별도 협의"},
    ]
)

# ---------------------------------------------------------------------------
# Growth trends (confirmed endpoints, interpolated between them for a readable curve)
# ---------------------------------------------------------------------------

CLAUDE_CODE_KR_GROWTH = pd.DataFrame(
    {
        "월": ["1개월 전", "2개월 전", "3개월 전", "4개월 전(현재)"],
        "MAU 지수 (1개월 전=1.0)": [1.0, 2.0, 3.6, 6.0],
    }
)
CLAUDE_CODE_KR_GROWTH_NOTE = (
    "확인된 사실은 시작점(1.0)과 4개월 후 '약 6배'라는 두 지점뿐입니다. 중간 지점은 매끄러운 "
    "곡선을 보여주기 위한 등비 보간(interpolation)이며 실측 월별 수치가 아닙니다. "
    "(출처: CIO Korea, 2026년 1~2월 보도)"
)

CURSOR_ARR_GROWTH = pd.DataFrame(
    {
        "시점": ["2025-11", "2026-01", "2026-03"],
        "ARR ($B)": [1.0, 1.5, 2.0],
    }
)
CURSOR_ARR_GROWTH_NOTE = (
    "확인된 사실은 2025-11 $1B와 2026-03 $2B 두 지점입니다. 2026-01 값은 두 지점 사이의 "
    "선형 보간 추정치로, 실제 월별 공시 수치가 아닙니다. (출처: 블룸버그 인용 집계 기사)"
)

# ---------------------------------------------------------------------------
# Qualitative capability profile (subjective synthesis, NOT a benchmark score)
# ---------------------------------------------------------------------------

CAPABILITY_PROFILE = pd.DataFrame(
    {
        "역량 축": ["추론·계획 깊이", "자율 실행력", "생태계 통합도", "비용 효율", "IDE 밀착도"],
        "Claude Code": [95, 90, 70, 55, 60],
        "OpenAI Codex": [88, 85, 90, 65, 55],
        "Cursor": [80, 82, 75, 80, 98],
        "GitHub Copilot": [70, 65, 98, 75, 90],
    }
)
CAPABILITY_PROFILE_NOTE = (
    "이 세션의 리서치 내용을 종합한 정성적(qualitative) 인상 점수이며, 공식 벤치마크가 아닙니다. "
    "0~100은 상대적 비교를 위한 편의상의 척도입니다."
)

# ---------------------------------------------------------------------------
# Model release timeline (2024 - Sept 2026)
# ---------------------------------------------------------------------------

TIMELINE = pd.DataFrame(
    [
        {"날짜": "2024-06", "회사": "Anthropic", "이벤트": "Claude 3.5 Sonnet — 코딩 벤치마크 급상승, 업계 기준선 재설정"},
        {"날짜": "2025-05", "회사": "Anthropic", "이벤트": "Claude Code CLI 정식 출시 (터미널 네이티브 에이전트)"},
        {"날짜": "2025-07", "회사": "Cognition / Google / OpenAI", "이벤트": "Windsurf 인수전 — OpenAI 딜 무산, Google이 인력·기술 라이선스, Cognition이 제품·브랜드 인수"},
        {"날짜": "2025-09", "회사": "Replit", "이벤트": "Replit Agent 3 — 자율 실행시간 10배 확장"},
        {"날짜": "2026-01", "회사": "OpenAI", "이벤트": "GPT-5.2-Codex 출시"},
        {"날짜": "2026-02", "회사": "OpenAI", "이벤트": "GPT-5.3-Codex 출시 · SWE-bench Verified 점수 공개 중단"},
        {"날짜": "2026-03", "회사": "GitHub", "이벤트": "Copilot Agent Mode 전체 사용자 확대 (VS Code/JetBrains, MCP 지원)"},
        {"날짜": "2026-04", "회사": "DeepSeek", "이벤트": "DeepSeek V4 (Pro/Flash) 출시 — 오픈웨이트로 프론티어급 근접 성능"},
        {"날짜": "2026-04", "회사": "Cognition", "이벤트": "Devin 요금제 전면 개편 (기존 $500/mo → $20~$200/mo 대중화)"},
        {"날짜": "2026-05", "회사": "Cursor", "이벤트": "Composer 2.5 출시 — 자체 에이전트 모델, 저비용 고성능 표방"},
        {"날짜": "2026-05", "회사": "AWS", "이벤트": "Amazon Q Developer 신규 가입 중단 발표 → Kiro로 전환 유도"},
        {"날짜": "2026-06", "회사": "Anthropic", "이벤트": "Claude Sonnet 5 출시 (Claude.ai 기본 모델 교체)"},
        {"날짜": "2026-06", "회사": "GitHub", "이벤트": "Copilot, 'AI Credits' 종량제 가격 체계로 전환"},
        {"날짜": "2026-06", "회사": "Cognition", "이벤트": "Windsurf → 'Devin Desktop'으로 리브랜딩"},
        {"날짜": "2026-07", "회사": "Anthropic", "이벤트": "Claude Opus 5 출시 (100만 토큰 컨텍스트)"},
        {"날짜": "2026-07", "회사": "xAI", "이벤트": "Grok 4.5 발표"},
        {"날짜": "2026-07", "회사": "Cognition", "이벤트": "Devin Desktop / Devin Cloud로 제품 이원화"},
        {"날짜": "2026-08", "회사": "Google", "이벤트": "Gemini 3.7 Flash 출시"},
        {"날짜": "2026-08", "회사": "Z.ai / DeepSeek / xAI", "이벤트": "Terminal-Bench 2.1 리더보드 — 오픈웨이트 모델들이 상위권 대거 진입"},
    ]
)

# ---------------------------------------------------------------------------
# YouTube deep-research results (verified via oEmbed lookups)
# ---------------------------------------------------------------------------

VIDEOS_KR = [
    {
        "title": "똑같이 클로드코드를 쓰는데 격차가 벌어지는 충격적인 이유",
        "channel": "실용주의 개발",
        "url": "https://www.youtube.com/watch?v=sHtM3CVZ07w",
    },
    {
        "title": "[2026 튜토리얼] 100시간 아끼는 바이브코딩 입문 가이드 (클로드코드 + 안티그래비티)",
        "channel": "시현의 모험 Sihyun Adventure",
        "url": "https://www.youtube.com/watch?v=km3aogD7wtI",
    },
    {
        "title": "설치부터 알려드립니다 (왕초보 환영) | 클로드 코드의 모~든 기초",
        "channel": "코딩알려주는누나",
        "url": "https://www.youtube.com/watch?v=Rq4ot7EOL08",
    },
    {
        "title": "2026 클로드코워크 사용법? 60대도 10분만에 마스터(클로드코드)",
        "channel": "라이프핵커,자충",
        "url": "https://www.youtube.com/watch?v=DZ_B3VizOnc",
    },
    {
        "title": "비개발자를 위한 클로드 코드(Claude Code) 입문 — AI 서비스 만들어 배포·판매하기",
        "channel": "AI 겸임교수 이종범",
        "url": "https://www.youtube.com/watch?v=HyMgKcuhE-s",
    },
    {
        "title": "2026 클로드(Claude) 사용법 30분 총정리 — 무료로 시작해서 업무 자동화까지",
        "channel": "AI 겸임교수 이종범",
        "url": "https://www.youtube.com/watch?v=WCgHcAjiY1s",
    },
    {
        "title": "바이브 코딩의 최후, AI가 개발자의 밥을 망치고 있다 — Vibe Coding is OVER EP.4",
        "channel": "투이컨설팅-투이톡",
        "url": "https://www.youtube.com/watch?v=qHf4j1v92TU",
    },
    {
        "title": "Codex 2026 기초 가이드 | 핵심 기능 설명, 실습까지 바로 따라하세요",
        "channel": "이동훈의 루트AI",
        "url": "https://www.youtube.com/watch?v=iupJvraoVow",
    },
]

VIDEOS_INTL = [
    {
        "title": "Claude Code vs Codex vs Cursor (an honest comparison)",
        "channel": "Theo - t3gg",
        "url": "https://www.youtube.com/watch?v=JMYspR42HFM",
    },
    {
        "title": "Cursor 3 vs Claude Code vs Codex — Who Actually Wins in 2026",
        "channel": "DEEPTECH AI LABS",
        "url": "https://www.youtube.com/watch?v=w8woebE5y94",
    },
    {
        "title": "Cursor vs Claude Code vs Codex (I Built the Same App 3 Times)",
        "channel": "Jan Marshal",
        "url": "https://www.youtube.com/watch?v=OnCep-HlMzI",
    },
    {
        "title": "Claude Code vs Codex vs Cursor: which one comes out on top?",
        "channel": "No Code MBA",
        "url": "https://www.youtube.com/watch?v=3EiHbGchA28",
    },
    {
        "title": "Codex vs Claude Code vs Cursor vs Antigravity (My Honest Review)",
        "channel": "Build Great Products",
        "url": "https://www.youtube.com/watch?v=3dj9m90tbY8",
    },
    {
        "title": "Cursor vs Codex vs Claude vs Zed vs Anti-Gravity (I Tested Them All)",
        "channel": "Your Average Tech Bro",
        "url": "https://www.youtube.com/watch?v=pJylXFAC87A",
    },
    {
        "title": "Claude Code & Cursor built the same app. There's a clear winner.",
        "channel": "Philipp Lackner",
        "url": "https://www.youtube.com/watch?v=aRNVncOYd5c",
    },
    {
        "title": "why claude, codex and cursor switched primitives (github take note)",
        "channel": "Syntax",
        "url": "https://www.youtube.com/watch?v=5He3_Lin5gE",
    },
    {
        "title": "One Agent Is NOT ENOUGH: Agentic Coding BEYOND Claude Code",
        "channel": "IndyDevDan",
        "url": "https://www.youtube.com/watch?v=M30gp1315Y4",
    },
    {
        "title": "Codex Full Course 2026: The NEW Best AI Coding Tool",
        "channel": "Riley Brown",
        "url": "https://www.youtube.com/watch?v=KXIdYEdOPys",
    },
]

# ---------------------------------------------------------------------------
# Tool-specific demo videos (2nd research pass) — one pair per tool, oEmbed-verified
# ---------------------------------------------------------------------------

TOOL_DEMO_VIDEOS = {
    "gemini": [
        {
            "title": "Gemini 3 is THE building Agent! Demos, Hands on with Anti Gravity",
            "channel": "MattVidPro",
            "url": "https://www.youtube.com/watch?v=3j-uF7poStI",
        },
        {
            "title": "Run Gemini 3 + Claude in One Free IDE (Antigravity Tutorial 2026)",
            "channel": "AyyazTech",
            "url": "https://www.youtube.com/watch?v=W1gLEoCqMbg",
        },
    ],
    "cursor": [
        {
            "title": "Cursor Composer 2.5 Just Dropped, And It's Incredible",
            "channel": "Build Great Products",
            "url": "https://www.youtube.com/watch?v=mdt2_CMJHfw",
        },
        {
            "title": "I Tested NEW Composer 2.5. Wow. (Updated LLM Benchmark)",
            "channel": "AI Coding Daily",
            "url": "https://www.youtube.com/watch?v=f7PGu8u-pvU",
        },
    ],
    "copilot": [
        {
            "title": "How to Use GitHub Copilot Agent Mode (Full Guide 2026)",
            "channel": "AI Mastery",
            "url": "https://www.youtube.com/watch?v=G7YWl598Ji4",
        },
        {
            "title": "How to Use GitHub Copilot Agent Mode - Visual Studio 2026 | Tips & Tutorial",
            "channel": "Codeless Developer",
            "url": "https://www.youtube.com/watch?v=wBgNflnfIEA",
        },
    ],
    "devin": [
        {
            "title": "Devin Desktop Full Tour: One Place to Manage Every Coding Agent",
            "channel": "Cognition",
            "url": "https://www.youtube.com/watch?v=bS_L25u4lZ0",
        },
        {
            "title": "Introducing Devin Desktop",
            "channel": "Cognition",
            "url": "https://www.youtube.com/watch?v=EmC1YbL981w",
        },
    ],
    "replit": [
        {
            "title": "Replit Agent 3 First Look",
            "channel": "Replit",
            "url": "https://www.youtube.com/watch?v=IcxplP6IlXY",
        },
        {
            "title": "I Tested Replit's Agent 3 – Can This AI Agent Really Build a Usable App?",
            "channel": "Sonny Sangha",
            "url": "https://www.youtube.com/watch?v=KHFUtD9go1E",
        },
    ],
    "kiro": [
        {
            "title": "AWS Kiro Crash Course 2026 | Agentic AI IDE Full Tutorial",
            "channel": "The AI Reporter",
            "url": "https://www.youtube.com/watch?v=2YYtBnCUq9A",
        },
        {
            "title": "AWS Kiro Explained: Build Your First AI App with Amazon's New AI IDE (2026)",
            "channel": "Coding Hives",
            "url": "https://www.youtube.com/watch?v=LicOYks7l58",
        },
    ],
}

TOOL_DEMO_VIDEOS_NOTE = (
    "Devin·Replit 항목의 첫 영상은 각각 Cognition, Replit 공식 채널에서 직접 확인된 영상입니다."
)
