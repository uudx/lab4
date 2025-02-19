from math import radians

def toRad(a):
    return radians(a)

a = float(input("Input degree: "))

print(f"Output radian: {toRad(a)}")
