terra = [[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]]
power = 1
for i in terra:
    for y in i:
        if power >= y:
            power = power + y
        else:
            break
        print(y, power)
print(power)
