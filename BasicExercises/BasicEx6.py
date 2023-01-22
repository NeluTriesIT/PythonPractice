#Iterate the given list of numbers and print only those which are divisible by 5
lista = [10 , 20, 33, 46, 55]
print("Divisible numbers by 5 are: ")
for i in range(len(lista)):
    if(lista[i] % 5 == 0):
        print(lista[i])
    