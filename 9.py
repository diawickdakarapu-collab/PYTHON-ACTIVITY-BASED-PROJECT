print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

currencies = ["USD", "EUR", "GBP"]
rates = [88, 102, 117]

budget = float(input("Enter travel budget in INR: "))

expenses = []
total_expense = 0

for i in range(len(currencies)):
    print("\nCurrency:", currencies[i])

    amount = float(input("Enter expense amount: "))

    converted = amount * rates[i]

    fee = converted * 0.02

    final_amount = converted + fee

    expenses.append(final_amount)

    total_expense += final_amount

    print("Converted Amount: Rs.", round(converted, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Final Amount: Rs.", round(final_amount, 2))

print("\nTRAVEL EXPENSE REPORT")

for i in range(len(currencies)):
    print(currencies[i], ": Rs.", round(expenses[i], 2))

print("Total Expense: Rs.", round(total_expense, 2))
print("Budget: Rs.", budget)

if total_expense <= budget:
    print("Travel is within budget")
    print("Remaining Budget: Rs.", round(budget - total_expense, 2))
else:
    print("Travel exceeds budget")
    print("Extra Amount: Rs.", round(total_expense - budget, 2))

largest = expenses.index(max(expenses))

print("Largest Expense Currency:", currencies[largest])
