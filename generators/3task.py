def itr(n):
    a = []
    for i in range(0, n):
        if i % 3 == 0:
            if i % 4 == 0:
                a.append(i)
    return str(a).replace("[", "").replace("]", "")

print(itr(int(input())))
