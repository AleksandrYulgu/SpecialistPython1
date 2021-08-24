# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def circle_in_circle(x1, y1, x2, y2, r1, r2):
    return distance(x1, y1, x2, y2) + r1 < r2 or distance(x1, y1, x2, y2) + r2 < r1

print(circle_in_circle(3, 4, 4, 6, 12, 9))
