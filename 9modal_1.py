def adder(val):
    def inner(x):
        return x + val
    print(type(inner), id(inner))
    return inner

two_adder = adder(2)
print(two_adder, id(two_adder))
print(two_adder(3)) # 5
print(two_adder(5)) # 7

three_adder = adder(3)
print(three_adder(5))   # 8
print(three_adder(-3))  # 0

print(id(two_adder) ,id(three_adder)  )
