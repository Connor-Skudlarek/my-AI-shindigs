import yfinance as yf
import pandas as pd
import os

# Load the CSV file and get the list of tickers from column A
df = pd.read_csv('nasdaq_screener_1734843756953.csv')
ticker_symbols = df['Symbol'].tolist()

# Create a folder for the downloaded CSVs
download_folder = './nasdaq_historical_data_yfinance'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Function to download historical data for each ticker
def download_historical_data(ticker):
    try:
        print(f"Downloading data for {ticker}")
        data = yf.download(ticker, period="max")
        if not data.empty:
            file_path = os.path.join(download_folder, f"{ticker}.csv")
            data.to_csv(file_path)
            print(f"Data for {ticker} saved to {file_path}")
        else:
            print(f"No data available for {ticker}")
    except Exception as e:
        print(f"Failed to download data for {ticker}: {e}")

# Download data for each ticker
for ticker in ticker_symbols:
    file_path = os.path.join(download_folder, f"{ticker}.csv")
    if os.path.exists(file_path):
        print(f"File already exists for {ticker}, skipping download.")
        continue
    
    download_historical_data(ticker)
