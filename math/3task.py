from math import tan, pi

def s(s, l) -> float:
    return (s/4)*(l**2)*(1/(tan(pi/s)))

print(s(4, 25))
