operand = input("input a operandr ")
while True:
    try:
        operand = float(operand)
        break
    except:
        operand = input("try to input a operand ")
result = operand
operator = input("input a operator ")
while True:
    if operator in '/*+-':
        break
    else:
        operator = input("try to input a operator ")

while operator != '=':
    operand = input("input a operand ")
    while True:
        try:
            operand = float(operand)
            result = eval(str(result) + operator + str(operand))
            break
        except ValueError:
            operand = input("try to input a operand ")
        except ZeroDivisionError:
            operand = input("Division by ziro. Try to input a another operand ")

    operator = input("input a operator ")
    while True:
        if operator in '/*+-=':
            break
        else:
            operator = input("try to input a operator ")

print(result)
