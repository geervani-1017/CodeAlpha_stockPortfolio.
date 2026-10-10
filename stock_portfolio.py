stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 190,
    "MSFT": 420
}

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")

for stock in stocks:
    print(stock)

total_investment = 0

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))

        price = stocks[stock_name]
        investment = price * quantity

        total_investment = total_investment + investment

        print("Stock:", stock_name)
        print("Price: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)

    else:
        print("Stock not available.")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    file.write("Total Investment: $" + str(total_investment) + "\n")

print("Portfolio saved to portfolio.txt")