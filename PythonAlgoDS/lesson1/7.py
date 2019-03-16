def can_be_triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b

def is_equilateral_triangle(a, b, c):
    return can_be_triangle(a, b, c) and a == b and b == c

def is_isosceles_triangle(a, b, c):
    return can_be_triangle(a, b, c) and not is_equilateral_triangle(a, b, c) and (a == b or b == c or a == c)

TriangleType = { 0: "not triangle", 1: 'triangle', 2: 'equilaterat', 3: 'isosceles'}

def get_triangle_type(a, b, c):
    if not can_be_triangle(a, b, c):
        return TriangleType[0]
    if is_equilateral_triangle(a, b, c):
        return TriangleType[2]
    if is_isosceles_triangle(a, b, c):
        return TriangleType[3]
    return TriangleType[1]

try:
    a = int(input())
    b = int(input())
    c = int(input())

    print(get_triangle_type(a, b, c))

except Exception as err:
    print(err)
