# add two numbers 50+50 and 100-10
print((50+50) + (100-10))

# 30+*6, 6^6, 6**6, 6+6+6+6+6+6
# I'm not sure what the first one is because it's invalid syntax
print(f'Bitwise XOR: 6^6 = {6^6}. 0b110 ^ 0b110 = 0b000')
print(f'6 to the 6th power = {6**6}')
print(f'6+6+6+6+6+6 = {6+6+6+6+6+6}')

print('Hello World')
print('Hello World : 10')


# calculate the monthly payment of a loan with principle P, yearly interest R, and paid in L months
def calcLoanPayment(P, R, L):
    # for this formula, R is 1.__ (interest)
    # Loan Amortization formula: (R**L) * (R-1) /
    #                             (R**L) - 1       * P
    R = ((R / 12) * 0.01) + 1
    dividend = (R ** L) * (R - 1)
    divisor = (R ** L) - 1
    payment = P * (dividend / divisor)
    # round up if not integer
    if not payment.is_integer():
        payment = int(payment + 1)
    return payment


pment = calcLoanPayment(800000, 6, 103)
print(f'Monthly payment: {pment}\nTotal Paid: {pment * 103}')
