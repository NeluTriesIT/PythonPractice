#Create a single list containing the odd numbers from the first one and the even numbers from the second one.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result = []
for x in list1:
    if(x % 2 != 0):
        result.append(x)
for y in list2:
    if(y % 2 == 0):
        result.append(y)
print(result)
