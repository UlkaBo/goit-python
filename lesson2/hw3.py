num = input("input a number ")
while True:
    try:
        num = float(num)
        break
    except:
        num = input("try to input a number ")
rez = num
op = input("input a operand ")
while True:
    if op in '/*+-':
        break
    else:
        op = input("try to input a operand ")

while op != '=':
    num = input("input a number ")
    while True:
        try:
            num = float(num)
            rez = eval(str(rez) + op + str(num))
            break
        except ValueError:
            num = input("try to input a number ")
        except ZeroDivisionError:
            num = input("Division by ziro. Try to input a another number ")

    op = input("input a operand ")
    while True:
        if op in '/*+-=':
            break
        else:
            op = input("try to input a operand ")

print(rez)
