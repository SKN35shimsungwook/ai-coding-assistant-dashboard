# AI Coding Assistant Dashboard (2026)

A Streamlit "investor pitch" style dashboard comparing AI coding assistants — Claude Code, OpenAI Codex, Google Gemini/Antigravity, Cursor, GitHub Copilot, Cognition Devin, Replit Agent, AWS Kiro, and open-weight challengers (DeepSeek, GLM, Qwen, Grok) — as of September 2026.

The UI content is in Korean; this README is in English for the repo.

## What's inside

- **12 sections / 66 slides**, navigated like a slide deck (Prev / Next / jump-to-slide) inside each Streamlit page
- **Landscape**: what AI coding assistants are, a deep dive on each major tool
- **Head-to-head**: SWE-bench / Terminal-Bench benchmark charts, API & subscription pricing, a qualitative capability-profile chart, a 2024→2026 release timeline with a cumulative release-pace chart, and market/adoption data (Stack Overflow & JetBrains surveys, Korean market trends)
- **30 embedded YouTube videos** (Korean + international), each verified via YouTube's oEmbed endpoint before inclusion — misattributed videos found during research are documented in-app rather than silently dropped
- **Growth-trend charts** (Claude Code Korea MAU, Cursor ARR) built from two confirmed data points, explicitly labeled as interpolated, not measured

All figures are sourced from a September 2026 deep-research pass (25+ web searches). Facts that could only be confirmed via secondary/aggregator sources are captioned as such throughout the app rather than presented as verified.

## Running locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Structure

```
streamlit_app.py       # entry point, navigation
app_pages/              # one file per section (00_cover.py ... 11_outlook.py)
utils/
  slides.py             # reusable Prev/Next/jump slide-deck component
  data.py                # shared reference data (benchmarks, pricing, timeline, videos)
.streamlit/config.toml   # dark theme
```
