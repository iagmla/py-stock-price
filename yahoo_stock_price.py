import sys, yfinance

def get_stock_price(
        ticker_symbol : str
    ) -> float:
    ticker = yfinance.Ticker(ticker_symbol)
    stock_price = ticker.info["currentPrice"]
    return stock_price

def main():
    ticker_symbol = sys.argv[1]
    price = get_stock_price(ticker_symbol)
    print(price)

if __name__ == "__main__":
    main()
