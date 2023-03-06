def operation(n1,n2,operator):
  
    if operator=='add':
        result = float(n1) + float(n2)
    elif operator=='subtract':
        result = float(n1) - float(n2)
    elif operator=='multiply':
        result = float(n1) * float(n2)
    elif operator=='divide':
        result = float(n1)/float(n2)
    elif operator=='power':
        result = float(n1)**float(n2)
    
    print(f'{n1} {operator} {num2} is {result}')

#############SIMPLE CALCULATOR########################
while True:
    print("Enter number 1:")
    num1 = input()
    print("Choose an operator (add/subtract/multiply/divide/power):")
    sign = input()
    print("Enter number 2:")
    num2 = input()
    operation(num1,num2,sign.lower())

    print('Do you want to continue (Y/N):')
    char = input

    if char=='n' or char=='N':
        break