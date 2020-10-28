
try:
    num1 = input("Enter the first number ")
    inum1 = int(num1)
except:
    print("You have entered a string, so please enter number again")
    num1 = input("Enter the first number ")
    inum1 = int(num1)


try:
    num2 = input("Enter the second number")
    inum2 = int(num2)
except:
    print("You have entered a string, so please enter number again")
    num2 = input("Enter the second number ")
    inum2 = int(num2)

total = inum1 + inum2

print("Sum of two numbers is:")
print(total)
