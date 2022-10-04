import pandas as pd
import streamlit as st
import yfinance as yt

tesla = yt.Ticker('TSLA')
apple = yt.Ticker('AAPL')

st.write(""" # Stock Price Analysis """)


tickersymbol = 'tsla'
tickerData = yt.Ticker(tickersymbol)
tickerOf = tickerData.history(period='1d', start='2019-5-30', end='2022-10-4')

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)

tesla.calendar
tesla.dividends
tesla.major_holders
tesla.actions
tesla.analysis
tesla.balance_sheet
tesla.cashflow
tesla.earnings
tesla.earnings_history
tesla.financials
