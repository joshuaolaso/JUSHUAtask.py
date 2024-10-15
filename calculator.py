# simple calculator

operator = input("please enter a valid operator (+ - * /): ")
num1 = float(input("please enter the first number: "))
num2 = float(input("please enter the second number: "))
 
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)  
elif operator == "*":
    result = num1 * num2
    print(result)  
elif operator == "/":
    result = num1 / num2
    print(round(result, 3)) 
else:
    print(f" {operator} is an invalid operator.....please try again!")
    