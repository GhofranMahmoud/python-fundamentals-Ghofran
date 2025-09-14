def greet_user(name):
    """
    Returns a greeting message for the portfolio owner.
    """
    return f"Hello, {name}! Welcome to your Financial Data Analyzer."

def calculate_portfolio_value(portfolio, stock_prices):
    """
    Calculate total value of a stock portfolio.
    portfolio: dict of {stock_name: shares}
    stock_prices: list of stock prices corresponding to stocks in same order
    """
    total_value = 0
    for (stock, shares), price in zip(portfolio.items(), stock_prices):
        total_value += shares * price
    return total_value

def format_currency(amount):
    """
    Format a number as USD currency.
    """
    return f"${amount:,.2f}"
