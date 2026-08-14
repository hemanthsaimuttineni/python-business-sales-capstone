def calculate_profit(revenue, cost):
    return revenue - cost


def calculate_profit_margin(revenue, cost):
    profit = revenue - cost
    return (profit / revenue) * 100


if __name__ == "__main__":
    revenue = float(input("Enter revenue: "))
    cost = float(input("Enter cost: "))

    profit = calculate_profit(revenue, cost)
    margin = calculate_profit_margin(revenue, cost)

    print("Profit:", profit)
    print("Profit Margin:", margin, "%")