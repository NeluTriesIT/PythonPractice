#Write a program to remove characters from a string starting from zero up to n and return a new string.
def string_slice(cuvant, lungime):
    print('Original word: ', cuvant)
    return f"Result: {cuvant[lungime:]}"   #string slice function a[n:] a=string; n=lenght that you want to slice
a = input("Please provide a word to be sliced: ")
b = int(input("Please provide the lenght you wish to be sliced out: "))
print(string_slice(a,b))
