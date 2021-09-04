# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
def dist_fut(*args):
    distances_fut = []
    for dist in distances:
        dist_funt = dist*3.28084
        distances_fut.append(dist_funt)
    return distances_fut

print(dist_fut(*distances))
