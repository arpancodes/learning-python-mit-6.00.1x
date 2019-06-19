
def balanceChecker(balance, annualInterestRate, monthlyPaymentRate, month=1):
    monthlyInterestRate = annualInterestRate / 12.0
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    UpdatedBalance = monthlyUnpaidBalance + \
        (monthlyInterestRate * monthlyUnpaidBalance)
    if month == 12:
        return round(UpdatedBalance, 2)
    else:
        month += 1
        return balanceChecker(UpdatedBalance, annualInterestRate, monthlyPaymentRate, month)
    # Monthly interest rate= (Annual interest rate) / 12.0
    # Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print(balanceChecker(balance, annualInterestRate, monthlyPaymentRate))

# Test Case 2
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

print(balanceChecker(balance, annualInterestRate, monthlyPaymentRate))
