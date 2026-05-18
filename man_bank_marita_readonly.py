import streamlit as st
import pandas as pd
import json
from pathlib import Path

st.set_page_config(page_title="MAN Bank — Marita", page_icon="🏦", layout="centered")

CURRENCY = "CHF"
DATA_FILE = Path("bank_of_dad_data.json")


def money(x: float) -> str:
    return f"{CURRENCY} {x:,.2f}"


DEFAULT_MARITA = {
    "Child": "Marita",
    "Age": 11,
    "Spend": 15.00,
    "Save": 0.00,
    "Invest / Bank": 1595.77,
    "Date": "1 May",
}


def load_marita():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)

            current_date = data.get("current_date", DEFAULT_MARITA["Date"])
            for row in data.get("current_balances", []):
                if row.get("Child") == "Marita":
                    marita = dict(row)
                    marita["Date"] = current_date
                    return marita
        except Exception:
            pass

    return DEFAULT_MARITA


marita = load_marita()
total = marita["Spend"] + marita["Save"] + marita["Invest / Bank"]

st.title("🏦 MAN Bank")
st.caption("Marita's balance")

st.markdown(
    """
    <style>
    .main-card {
        border: 1px solid #e6e6e6;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .big-balance {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0.2rem 0 0.6rem 0;
    }
    .small-label {
        color: #666;
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("### Marita")
st.markdown(f'<div class="small-label">Total balance</div><div class="big-balance">{money(total)}</div>', unsafe_allow_html=True)
st.write(f"Updated: **{marita['Date']}**")
st.markdown("</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.metric("Spend", money(marita["Spend"]))
c2.metric("Save", money(marita["Save"]))
c3.metric("Invest", money(marita["Invest / Bank"]))

st.divider()

with st.expander("What does this mean?"):
    st.markdown(
        """
        **Spend**  
        Money I can use for small things.

        **Save**  
        Money for a bigger goal.

        **Invest**  
        Future money. This stays in MAN Bank and grows over time.
        """
    )

with st.expander("Money lesson"):
    st.info("When I invest more, I have less to spend today, but more choices in the future.")

st.caption("Read-only view. Marita cannot change balances from this page.")
