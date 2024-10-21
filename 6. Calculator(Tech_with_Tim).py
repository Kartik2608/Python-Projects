# Text based CALCULATOR (Begginer level PYTHON_PROJECT)
# Takes the numbers and sign as input and performs the operation like the real calculator
def operand(number):
    while True:
        operand = input("Number" + str(number) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid Operand")

Number_1 = operand(1)
Number_2 = operand(2)
sign = input("Sign: ")
result = 0
if sign == "+":
    result = Number_1 + Number_2
elif sign == "*":
    result = Number_1 * Number_2
elif sign == "-":
    result = Number_1 - Number_2
elif sign == "/":
    if Number_2 != 0:
        result = Number_1 / Number_2
    else:
        print("Division by Zero.")
else:
    print("Enter a valid sign.")

print(result)