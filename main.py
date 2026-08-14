import calculator
import business

# Calculator
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))

# Business calculations
revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))

profit = business.calculate_profit(revenue, cost)
margin = business.calculate_profit_margin(revenue, cost)

print("Profit:", profit)
print("Profit Margin:", round(margin, 2), "%")

if profit >= 0:
    print("Status: PROFIT")
else:
    print("Status: LOSS")
