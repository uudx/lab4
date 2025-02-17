n = int(input())
a = []
for i in range(0, n):
    if i % 2 == 0:
        a.append(i)
print(str(a).replace("[", "").replace("]", ""))
