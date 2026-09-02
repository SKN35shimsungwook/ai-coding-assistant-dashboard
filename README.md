# AI 코딩 어시스턴트 대시보드 (2026)

Claude Code, OpenAI Codex, Google Gemini/Antigravity, Cursor, GitHub Copilot, Cognition Devin, Replit Agent, AWS Kiro와 오픈웨이트 도전자(DeepSeek, GLM, Qwen, Grok)를 2026년 9월 기준으로 비교하는, 투자 설명회(피치덱) 스타일의 Streamlit 대시보드입니다.

## 담긴 내용

- **12개 세션 / 66개 슬라이드** — 각 Streamlit 페이지 안에서 슬라이드 덱처럼 이전/다음/슬라이드 이동으로 넘겨볼 수 있습니다
- **지형도**: AI 코딩 어시스턴트란 무엇인지부터, 주요 도구별 딥다이브
- **정면 비교**: SWE-bench / Terminal-Bench 벤치마크 차트, API·구독 가격 비교, 정성적 역량 프로필 차트, 2024→2026 릴리즈 타임라인과 누적 릴리즈 속도 차트, 시장·채택 동향(Stack Overflow·JetBrains 서베이, 국내 시장 동향)
- **유튜브 임베드 영상 30개**(국내 + 해외) — 모두 YouTube oEmbed로 실제 존재·재생 가능 여부를 검증한 뒤 포함했고, 리서치 과정에서 발견한 오귀속(잘못 연결된) 영상 사례도 숨기지 않고 대시보드 안에 그대로 기록했습니다
- **성장 추이 차트**(한국 Claude Code MAU, Cursor ARR) — 확인된 두 지점 사이를 보간한 것이라는 점을 명시했습니다

모든 수치는 2026년 9월에 진행한 딥리서치(웹서치 25건 이상)에서 가져왔습니다. 2차 집계 출처로만 확인된 사실은 대시보드 곳곳에 "UNVERIFIED/참고용"으로 표기해, 검증된 사실처럼 보이지 않도록 했습니다.

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 구조

```
streamlit_app.py       # 진입점, 내비게이션
app_pages/              # 세션별 파일 (00_cover.py ... 11_outlook.py)
utils/
  slides.py             # 재사용 가능한 이전/다음/점프 슬라이드 덱 컴포넌트
  data.py                # 공통 참조 데이터 (벤치마크, 가격, 타임라인, 영상)
.streamlit/config.toml   # 다크 테마
```
