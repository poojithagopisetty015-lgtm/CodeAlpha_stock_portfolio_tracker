# File Name: stock_portfolio_tracker.py

# STOCK PORTFOLIO TRACKER

# Available stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

# User portfolio
portfolio = {}

while True:

    print("\n" + "=" * 45)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. View Total Investment")
    print("4. View Available Stocks")
    print("5. Save Portfolio")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # ADD STOCK
    if choice == "1":

        print("\nAvailable Stocks:")

        for stock, price in stock_prices.items():
            print(f"{stock} : ${price}")

        stock_name = input("\nEnter stock name: ").upper()

        if stock_name in stock_prices:

            quantity = int(input("Enter quantity: "))

            if stock_name in portfolio:
                portfolio[stock_name] += quantity
            else:
                portfolio[stock_name] = quantity

            print(f"\n✅ {stock_name} added successfully!")

        else:
            print("\n❌ Stock not available!")

    # VIEW PORTFOLIO
    elif choice == "2":

        if len(portfolio) == 0:
            print("\n📂 Portfolio is empty!")

        else:
            print("\nYOUR PORTFOLIO")
            print("-" * 45)

            for stock, quantity in portfolio.items():

                price = stock_prices[stock]
                investment = price * quantity

                print(
                    f"{stock} | Quantity: {quantity} | "
                    f"Price: ${price} | "
                    f"Investment: ${investment}"
                )

    # VIEW TOTAL INVESTMENT
    elif choice == "3":

        total = 0

        for stock, quantity in portfolio.items():
            total += stock_prices[stock] * quantity

        print(f"\n💰 Total Investment Value: ${total}")

    # VIEW AVAILABLE STOCKS
    elif choice == "4":

        print("\nAVAILABLE STOCKS")
        print("-" * 30)

        for stock, price in stock_prices.items():
            print(f"{stock} : ${price}")

    # SAVE PORTFOLIO
    elif choice == "5":

        with open("portfolio_summary.txt", "w") as file:

            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 35 + "\n")

            total = 0

            for stock, quantity in portfolio.items():

                price = stock_prices[stock]
                investment = price * quantity
                total += investment

                file.write(
                    f"{stock} | Quantity: {quantity} | "
                    f"Investment: ${investment}\n"
                )

            file.write(f"\nTotal Investment Value: ${total}")

        print("\n📁 Portfolio saved successfully!")

    # EXIT
    elif choice == "6":

        print("\n👋 Exiting Program...")
        break

    else:
        print("\n❌ Invalid choice! Please try again.")