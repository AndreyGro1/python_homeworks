import math

def square(side_length):
    area = side_length * side_length
    return math.ceil(area)


side = 4.5  
area = square(side)


print(f"Площадь квадрата со стороной {side}: {area}")
