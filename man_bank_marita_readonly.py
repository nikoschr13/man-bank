import streamlit as st

st.set_page_config(page_title="MAN Bank", page_icon="🏦", layout="centered")

CURRENCY = "CHF"

# Phase 1: fixed read-only balances for all three girls.
# Updated for:
# - Nelia spent CHF 9.90 from Spend for a baby gift.
# - Aria lent CHF 9.00 to Nelia for a Nike bottle.
# - Nelia owes Aria CHF 10.00 next month: CHF 9 repayment + CHF 1 interest.
GIRLS = [
    {
        "Name": "Marita",
        "Date": "After latest update",
        "Spend": 15.00,
        "Save": 0.00,
        "Invest": 1595.77,
        "Lesson": "When I invest more, I have less to spend today, but more choices in the future.",
        "Note": "",
    },
    {
        "Name": "Aria",
        "Date": "After latest update",
        "Spend": 7.00,
        "Save": 0.00,
        "Invest": 1433.01,
        "Lesson": "Lending money means someone owes me money back later.",
        "Note": "Aria lent CHF 9.00 to Nelia. Nelia should repay CHF 10.00 next month.",
    },
    {
        "Name": "Nelia",
        "Date": "After latest update",
        "Spend": 0.10,
        "Save": 0.00,
        "Invest": 942.46,
        "Lesson": "If I borrow money, I must pay it back later.",
        "Note": "Nelia spent CHF 9.90 on a baby gift and borrowed CHF 9.00 from Aria. She owes Aria CHF 10.00 next month.",
    },
]


def money(amount: float) -> str:
    return f"{CURRENCY} {amount:,.2f}"


def total_for(girl: dict) -> float:
    return girl["Spend"] + girl["Save"] + girl["Invest"]


st.markdown(
    """
    <style>
    .main-card {
        border: 1px solid #e6e6e6;
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.05);
        text-align: center;
    }
    .girl-name {
        font-size: 1.45rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }
    .label {
        color: #666;
        font-size: 0.95rem;
    }
    .big-balance {
        font-size: 2.35rem;
        font-weight: 800;
        margin: 0.25rem 0 0.75rem 0;
    }
    .updated {
        color: #777;
        font-size: 0.9rem;
    }
    .small-note {
        color: #777;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏦 MAN Bank")
st.caption("Read-only balances")

names = [girl["Name"] for girl in GIRLS]

try:
    selected_name = st.segmented_control(
        "Choose account",
        names,
        default="Marita",
    )
except AttributeError:
    selected_name = st.selectbox("Choose account", names, index=0)

girl = next(g for g in GIRLS if g["Name"] == selected_name)
total = total_for(girl)

st.markdown(
    f"""
    <div class="main-card">
        <div class="girl-name">{girl["Name"]}</div>
        <div class="label">Total balance</div>
        <div class="big-balance">{money(total)}</div>
        <div class="updated">Updated: {girl["Date"]}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
c1.metric("Spend", money(girl["Spend"]))
c2.metric("Save", money(girl["Save"]))
c3.metric("Invest", money(girl["Invest"]))

if girl["Note"]:
    st.warning(girl["Note"])

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
    st.info(girl["Lesson"])

st.markdown(
    '<div class="small-note">Read-only view. Balances cannot be changed from this page.</div>',
    unsafe_allow_html=True,
)
