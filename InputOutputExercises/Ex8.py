#Write a program to use string.format() method to format the following three variables as per the expected output
totalmoney = 1000
quantity = 3
price = 450
combined = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars"
print(combined.format(quantity, totalmoney, price))
