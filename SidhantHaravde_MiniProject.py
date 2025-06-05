
# Function for Addition
def addition(a,b):
    sum = int(a) + int(b)
    return sum

# Function for Subtraction
def subtaction(a,b):
    difference = int(a) - int(b)
    return difference
    

# Function for Multiplication
def multiplication(a,b):
    product = int(a)*int(b)
    return product
    
# Function for Division
def division(a,b):
    division = int(a)/int(b)
    return division
    
# Function for Factorial
def factorial(a):
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result

#  Function for GCD
def GCD(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
  
# Function for Least Common Multiple  
def LCM(a, b):
    return abs(a * b) // GCD(a, b)

# While Loop for MultiFunction Calculator
while True:
    # User Interface
    print("Hello, Weclcome to Multifunction Calculator")
    print("What do you want?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. GCD")
    print("6. LCM")
    print("7. Factorial")
    print("8. Exit")
    # Value inputed for user
    value = input("Choose an option:")
    
    # If Value is 1 do addition
    if value == '1':
        value1 = input("What is the first value:")
        value2 = input("What is the second value:")
        print("This is the value: ", addition(value1,value2))
    
    # If Value is 2 do subtraction
    if value == '2':
        value1 = input("What is the first value:")
        value2 = input("What is the second value:")
        print("This is the value: ", subtaction(value1,value2))
        
    # If Value is 3 do multiplication
    if value == '3':
        value1 = input("What is the first value:")
        value2 = input("What is the second value:")
        print("This is the value: ", multiplication(value1,value2))
    
    # If Value is 4 do division
    if value == '4':
        value1 = input("What is the first value:")
        value2 = input("What is the second value:")
        print("This is the value: ", division(value1,value2))

    # If Value is 7 find the factorial     
    if value == '7':
        value1 = input("What is the value for the factorial: ")
        print("This is the value", factorial(int(value1)))

    # If Value is 5 find the Greatest Common Factor     
    if value == '5':
        value1 = input("What is the first value:")
        value2 = input("What is the second value:")
        print("This is the value: ", GCD(int(value1), int(value2)))
    
    # If Value is 6 find the Least Common Multiple     
    if value == '6':
        value1 = input("What is the first value:")
        value2 = input("What is the second value:")
        print("This is the value: ", LCM(int(value1), int(value2)))
        
    # If Value is 8 end the function    
    if value == '8':
        break
        print("Have a nice day")
    
    # If User prints invalid function
    else:
        print("Print a valid value")
        

        
    