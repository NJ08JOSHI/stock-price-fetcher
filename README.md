# Stock Price Checker

This project is a simple online stock price app built with Python + Streamlit + Yahoo Finance.

## Features
- Enter a stock symbol such as `AAPL`, `MSFT`, or `GOOG`
- View the latest close price
- See recent price trend in a chart

## Run locally

1. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Start the app
   ```bash
   streamlit run app.py
   ```

## Run online

This app can be deployed to free hosting services such as:
- Streamlit Cloud
- Render
- PythonAnywhere

### Streamlit Cloud
1. Push this repo to GitHub
2. Open https://share.streamlit.io/
3. Select the repo and branch
4. Set the main file to `app.py`
5. Deploy

## Example
default input: `AAPL`

The app will show the latest closing price and a small chart of the last 5 days.
