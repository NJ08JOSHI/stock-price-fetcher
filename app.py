import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Price Checker", page_icon="📈")
st.title("📈 Stock Price Checker")

symbol = st.text_input("Enter stock symbol", value="AAPL").strip().upper()

if symbol:
    try:
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="5d")

        if history.empty:
            st.error(f"No data found for '{symbol}'. Please check the stock symbol.")
        else:
            latest_close = history["Close"].iloc[-1]
            previous_close = history["Close"].iloc[-2] if len(history) > 1 else latest_close

            change = latest_close - previous_close
            change_percent = (change / previous_close) * 100 if previous_close else 0

            st.metric(
                label=f"{symbol} Latest Close",
                value=f"${latest_close:.2f}",
                delta=f"{change:.2f} ({change_percent:.2f}%)",
            )

            st.subheader("Recent trend")
            st.line_chart(history["Close"])
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
