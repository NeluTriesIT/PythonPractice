#Iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

print(f"Current Number 0 Previous Number 0 Sum: 0 ")
for i in range(1,10):
    print(f"Current Number {i} Previous Number {i - 1} Sum: {i + (i - 1) }")

