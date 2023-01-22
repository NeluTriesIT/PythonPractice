#Write a function to return "True" if the first and last number of a given list is same.
#If the numbers are different then return "False"

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def comparison(lista):
    x = lista[0]
    y = lista[-1]
    if(x == y):
        return True
    else:
        return False

print(f"Result for the first list is: {comparison(numbers_x)}")
print(f"Result for the second list is: {comparison(numbers_y)}")

