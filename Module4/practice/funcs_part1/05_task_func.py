# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def distance(x1, y1, x2, y2):
    ab = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return ab

def can_triangle(p1, p2, p3):
    p1p2 = distance(*p1, *p2)
    p2p3 = distance(*p2, *p3)
    p3p1 = distance(*p3, *p1)
    return p1p2 + p2p3 > p3p1 and p2p3 + p3p1 > p1p2 and p1p2 + p3p1 > p2p3

def perim(p1, p2, p3):
    if can_triangle(p1, p2, p3):
        per = distance(*p1, *p2)+distance(*p2, *p3)+distance(*p3, *p1)
        s = (per * (per - distance(*p1, *p2)) * (per - distance(*p2, *p3)) * (per - distance(*p3, *p1)))**0.5
        return per, s

# Пример вызова функции
print(perim((10, 12), (14, 18), (12, 12)))

# Не забудьте протестировать вашу функцию
