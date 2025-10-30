def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2    
def multi(n1, n2):
    return n1 * n2 
def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        print("Division is not possible")      
operations = {
    "+":add,
    "-":sub,
    "*":multi,
    "/":div,
}
def calculator():
    num1 = float(input("Enter first number : "))
    continue_calculation = True
    while continue_calculation:
        print("Addition(+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)")
        operation = input("select an operation(+,-,*,/):")
        num2 = float(input("Enter second number: "))
        result = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        print("Result:",{result})
        continue_calculation = False
calculator()

