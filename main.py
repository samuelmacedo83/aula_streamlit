import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Set page title
st.title("Stock History App")

# Create a sidebar section for user input
st.sidebar.title("User Input")
ticker_symbol = st.sidebar.text_input("Enter the stock symbol", value='AAPL', max_chars=8)

# Retrieve stock data using yfinance
data = yf.download(ticker_symbol, start="2020-01-01", end="2023-06-24")

# Display the stock data in a dataframe
st.subheader("Stock History")
st.dataframe(data)

# Plot the closing price using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Closing Price'))
fig.update_layout(title=f"{ticker_symbol} Stock Price", xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig)