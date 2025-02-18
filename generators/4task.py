def squares(a,b):
    o = []
    for i in range(a,b+1):
        o.append(i**2)
    return o

a = int(input())
b = int(input())

somelist = squares(a, b)

for i in somelist:
    print(i)
