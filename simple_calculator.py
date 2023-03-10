def operation(n1,n2,operator):
  
    if operator=='add':
        result = float(n1) + float(n2)
    elif operator=='subtract':
        result = float(n1) - float(n2)
    elif operator=='multiply':
        result = float(n1) * float(n2)
    elif operator=='divide':
       try:
            result = float(n1)/float(n2)
       except ZeroDivisionError:
            print("Cannot divide zero , the second number cannot be zero in divide operation")
            return
    elif operator=='power':
        result = float(n1)**float(n2)
    
    print(f'{n1} {operator} {num2} is {result}')

#############SIMPLE CALCULATOR########################
while True:
    try:
        num1 = input("Enter number 1:")
        sign = input("Choose an operator (add/subtract/multiply/divide/power):")
        num2 = input("Enter number 2:")
        operation(num1,num2,sign.lower())
    except ValueError:
        print("Invalid value. Please enter valid value.")
    except:
        print("There is error!")

    char = input('Do you want to continue (Y/N):')
    if char=='n' or char=='N':
        break
