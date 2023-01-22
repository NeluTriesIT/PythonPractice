#Write a program to check if the given number is a palindrome number.
#palindrome= the number is the same after reverse.

def palindrome(x):
    y = "".join(reversed(x))  #How to reverse a string(built in function)
    if(int(x) == int(y)):
        print("Yes, palindrome it is!")
    else:
        print("Nope, not palindrome")

x = input("Give us a number for the palindrome checker")
palindrome(x)