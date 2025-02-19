def squares(a):
    i = a
    while i > -1:
        yield i
        i-=1

for i in squares(10):
    print(i)
