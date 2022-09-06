import math

a = float(input("первое число "))

deist = input("действие ")

b = float(input("второе число "))

if deist == "+":
    c = a + b
    print("результат равен " + str(c))

elif deist == "-":
    c = a - b
    print("результат равен " + str(c))

elif deist == "*":
    c = a * b
    print("результат равен " + str(c))

elif deist == "/":
    c = a / b
    print("результат равен " + str(c))

elif deist == "a^2":
    c = a**2
    print("результат равен " + str(c))

elif deist == "b^2":
    c = b**2
    print("результат равен " + str(c))

elif deist == "sqrt a":
    c = math.sqrt(a)
    print("результат равен " + str(c))

elif deist == "sqrt b":
    c = math.sqrt(b)
    print("результат равен " + str(c))

else:
    print("неверная команда!")