def s(h, a, b) -> float:
    return ((a+b)/2)*h

h = int(input("Height: ")) 
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print(f"Expected Output: {s(h,a,b)}")
