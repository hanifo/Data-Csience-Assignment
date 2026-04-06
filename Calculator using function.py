# Function to compute calculation
def calculator():
    # input two numbers
    a = float(input())
    b = float(input())

    # perform all operations
    print("Add:", a + b)#add
    print("Sub:", a - b)#subtruct
    print("Mul:", a * b)#multiply
    print("Div:", "Error" if b == 0 else a / b)#devide

calculator()# Calling function
