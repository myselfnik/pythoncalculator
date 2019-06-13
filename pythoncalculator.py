   
"""here we are defining function"""

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y
    
def divide(x,y):
    return x / y

def power(x,y):
    return pow(x,y)

"""now we will take inputs from the user"""

print("Select the operations")
print("1. Add")
print("2. Substraction")
print("3. Multiply")
print("4. Divide")
print("5. Power")

choice = input("Enter choice(1/2/3/4/5)")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))
    
elif choice == '2':
    print(num1, "-", num2, "=", substract(num1,num2))
    
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))
    
elif choice == '5':
    print(num1, "**", num2, "=", power(num1,num2))
    
else:
    print("invalid input please try again")
