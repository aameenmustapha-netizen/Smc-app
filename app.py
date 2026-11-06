import streamlit as st
import pandas as pd

st.set_page_config(page_title="SMC Trading App", layout="wide")
st.title("📈 SMC Trading App")
st.write("Smart Money Concepts - Bias, Entry & Risk Calculator")

st.sidebar.header("Market Bias")
bias = st.sidebar.selectbox("Daily Bias", ["Bullish", "Bearish", "Ranging"])
pair = st.sidebar.selectbox("Pair", ["XAUUSD (Gold)", "EURUSD", "GBPUSD", "BTCUSD", "US30"])
st.sidebar.write(f"Pair: {pair} | Bias: {bias}")

tab1, tab2, tab3 = st.tabs(["📊 Bias Checker", "🎯 Entry Calculator", "⚖️ Risk Calculator"])

with tab1:
    st.subheader("Bias Checker")
    st.write(f"Current Bias for {pair}: **{bias}**")
    if bias == "Bullish":
        st.success("Look for BUY entries only. Wait for price to sweep lows into Demand / FVG, then CHoCH up.")
    elif bias == "Bearish":
        st.error("Look for SELL entries only. Wait for price to sweep highs into Supply / FVG, then CHoCH down.")
    else:
        st.warning("Ranging - Trade range highs to lows. Avoid chasing in the middle.")
    st.markdown("**SMC Checklist:**\n- [ ] Liquidity Sweep?\n- [ ] CHoCH / BOS?\n- [ ] FVG / Order Block?\n- [ ] Entry in Discount / Premium?")

with tab2:
    st.subheader("Entry Calculator")
    entry = st.number_input("Entry Price", value=2650.0)
    sl = st.number_input("Stop Loss Price", value=2640.0)
    tp = st.number_input("Take Profit Price", value=2680.0)
    if entry != sl:
        rr = abs(tp - entry) / abs(entry - sl)
        st.metric("Risk : Reward", f"1 : {rr:.2f}")
        if rr >= 2:
            st.success("Good Setup - RR is 2R or more ✅")
        else:
            st.warning("Low RR - Wait for better entry")

with tab3:
    st.subheader("Risk Calculator")
    balance = st.number_input("Account Balance ($)", value=1000.0)
    risk_pct = st.slider("Risk % per trade", 0.5, 5.0, 1.0)
    risk_money = balance * risk_pct / 100
    st.metric("You Risk", f"${risk_money:.2f}")
    st.write(f"If you lose this trade, you lose ${risk_money:.2f}. If you win 2R, you make ${risk_money*2:.2f}")

st.markdown("---")
st.caption("Built for SMC traders | Educational only - not financial advice")
