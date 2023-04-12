#Display numbers from a list that satisfy the following conditions:
""" -The number must be divisible by 5
    -If the number is greater than 150, then skip it and move to the next number
    -If the number is greater than 500, then stop the loop (expected output 75 150 145)
"""
numbers = [12, 75, 150, 180, 145, 525, 50]
for a in numbers:
    if(a % 5 == 0):
        if(a <= 150):
            print(a)
        elif (a > 150 and a < 500):
            continue
        else:
            break
