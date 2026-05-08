from helpers import *

n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the Second number :"))

print("Select the operation to do on the two number")
print("Type 1 - Multiplication")
print("Type 2 - Addition")
print("Type 3 - Subtraction")
print("Type 4 - Power / exponential")
print("Type 5 - divide")
print('Type 6 - Floor division')

operator = int(input("Enter the Option from above :"))

if operator == 1:
    print(multiply(n1,n2))

elif operator == 2:
    print(add(n1,n2))

elif operator == 3:
    print(sub(n1,n2))

elif operator == 4:
    print(power(n1,n2))

elif operator == 5:
    print(divide(n1,n2))

elif operator == 6:
    print(floor(n1,n2))

else:
    print("Please select vaild Option")

