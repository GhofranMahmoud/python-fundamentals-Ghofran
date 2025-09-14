import sys
from utils import greet_user, calculate_portfolio_value, format_currency

if __name__ == "__main__":
    # Check if arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python data_analyzer.py <name> <cash_balance>")
        sys.exit(1)
    
    # Command line arguments
    portfolio_owner = sys.argv[1]
    cash_balance = int(sys.argv[2])

    # Financial data
    stock_prices = [150.5, 320.75, 45.2]
    portfolio = {"AAPL": 10, "GOOGL": 5, "TSLA": 8}
    transaction_ids = (101, 102, 103)

    print("Starting Financial Data Analyzer Script...")
    print(f"Portfolio owner: {portfolio_owner}")
    print(f"Current cash balance: {format_currency(cash_balance)}")

    # Conditionals
    if cash_balance < 1000:
        print("Warning: Low cash balance!")
    elif 1000 <= cash_balance < 10000:
        print("Cash balance is moderate.")
    else:
        print("Cash balance is healthy.")

    # Loops
    for stock, shares in portfolio.items():
        print(f"Stock: {stock}, Shares: {shares}")

    transaction_count = 0
    while transaction_count < len(transaction_ids):
        print(f"Processing transaction ID: {transaction_ids[transaction_count]}")
        transaction_count += 1

    # Built-in functions
    for i, price in enumerate(stock_prices):
        print(f"Stock {i+1} price: {price}, ID: {id(price)}")

    for n in range(3):
        print(f"Range example: {n}")

    # --------------------------
    # String to int casting 
    # --------------------------
    cash_balance_str = sys.argv[2]          # string from command line
    cash_balance_int = int(cash_balance_str)  # cast to int
    print(f"Cash balance (string → int): {cash_balance_int}")


    # Imported functions
    print(greet_user(portfolio_owner))
    total_value = calculate_portfolio_value(portfolio, stock_prices)
    print(f"Total Portfolio Value: {format_currency(total_value)}")
