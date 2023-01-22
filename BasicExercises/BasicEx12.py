#Calculate the income tax for the given income by adhering to the below rules
#First 10,000$  ----->   Rate = 0%
#Next 10,000$ --------> Rate = 10%
#The remaining -------> Rate = 20%
tax = 0
income = int(input("Income : "))
if income <= 10000:
    tax = 0
elif income <= 20000:
    x = income - 10000
    tax = x * 10 / 100
else :
    tax = 1000 + (income - 20000) * 20 / 100
print("Total tax to be paid: ", tax)