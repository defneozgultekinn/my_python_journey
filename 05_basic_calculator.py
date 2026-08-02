num1= float(input("Enter your first number: "))
operation= input("+ , - , / , * : ")
num2= float(input("Enter your second number: "))

if operation== "+":
    result = num1+num2
if operation== "-":
    result = num1 - num2
if operation== "/":
    result = num1/num2
if operation== "*":
    result = num1*num2

print(result)