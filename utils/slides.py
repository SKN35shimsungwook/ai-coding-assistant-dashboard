"""Reusable pitch-deck-style slide navigator for dashboard pages.

Each page is a sequence of "slides" (title + render callback). This gives the
whole app a consistent investor-pitch feel: one idea per screen, Prev/Next
controls, a jump menu, and a running progress bar.
"""

from __future__ import annotations

from collections.abc import Callable

import streamlit as st

Slide = tuple[str, Callable[[], None]]

TOTAL_SLIDES = 0  # populated by app_pages.registry after all pages import


def slide_deck(section_key: str, slides: list[Slide]) -> None:
    n = len(slides)
    idx_key = f"_slide_idx_{section_key}"
    if idx_key not in st.session_state:
        st.session_state[idx_key] = 0
    idx = max(0, min(st.session_state[idx_key], n - 1))

    st.progress((idx + 1) / n, text=f"슬라이드 {idx + 1} / {n}")

    title, render_fn = slides[idx]
    st.subheader(title)
    with st.container(border=True):
        render_fn()

    st.write("")
    nav_l, nav_mid, nav_r = st.columns([1, 3, 1])
    with nav_l:
        if st.button(
            "이전",
            icon=":material/arrow_back:",
            width="stretch",
            disabled=idx == 0,
            key=f"{section_key}_prev",
        ):
            st.session_state[idx_key] = idx - 1
            st.rerun()
    with nav_mid:
        labels = [f"{i + 1}. {t}" for i, (t, _) in enumerate(slides)]
        choice = st.selectbox(
            "슬라이드 이동",
            labels,
            index=idx,
            key=f"{section_key}_jump_{idx}",
            label_visibility="collapsed",
        )
        chosen_idx = labels.index(choice)
        if chosen_idx != idx:
            st.session_state[idx_key] = chosen_idx
            st.rerun()
    with nav_r:
        if st.button(
            "다음",
            icon=":material/arrow_forward:",
            width="stretch",
            disabled=idx == n - 1,
            key=f"{section_key}_next",
        ):
            st.session_state[idx_key] = idx + 1
            st.rerun()
