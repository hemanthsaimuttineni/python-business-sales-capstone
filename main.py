import calculator
import business
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))

profit = business.calculate_profit(50000, 30000)
margin = business.calculate_profit_margin(50000, 30000)
print("Profit:", profit)
print("Profit Margin:", margin, "%")

revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))
profit = business.calculate_profit(revenue, cost)
margin = business.calculate_profit_margin(revenue, cost)
print("Profit:", profit)
print("Profit Margin:", margin, "%")