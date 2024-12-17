from itertools import combinations
class RectCorrectError(Exception):
    pass
def isCorrectRect(spisok):
    kortezh1 = spisok[0]
    kortezh2 = spisok[1]
    if kortezh1[0] < kortezh2[0] and kortezh1[1] < kortezh2[1]:
        return True
    else:
        return False
def isCollisionRect(spisok1, spisok2):
    if not isCorrectRect(spisok1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCorrectRect(spisok2):
        raise ValueError("2й прямоугольник некорректный")
    kortezh1 = spisok1[0]
    kortezh2 = spisok1[1]
    kortezh3 = spisok2[0]
    kortezh4 = spisok2[1]
    x_1_minimalny = kortezh1[0]
    y_1_minimalny = kortezh1[1]
    x_1_maksimalny = kortezh2[0]
    y_1_maksimalny = kortezh2[1]
    x_2_minimalny = kortezh3[0]
    y_2_minimalny = kortezh3[1]
    x_2_maksimalny = kortezh4[0]
    y_2_maksimalny = kortezh4[1]
    if x_1_maksimalny < x_2_minimalny or x_1_minimalny > x_2_maksimalny or y_1_maksimalny < y_2_minimalny or y_1_minimalny > y_2_maksimalny:
        return False
    else:
        return True
def intersectionAreaRect(spisok1, spisok2):
    if not isCorrectRect(spisok1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCorrectRect(spisok2):
        raise ValueError("2й прямоугольник некорректный")
    kortezh1 = spisok1[0]
    kortezh2 = spisok1[1]
    kortezh3 = spisok2[0]
    kortezh4 = spisok2[1]
    x_1_minimalny = kortezh1[0]
    y_1_minimalny = kortezh1[1]
    x_1_maksimalny = kortezh2[0]
    y_1_maksimalny = kortezh2[1]
    x_2_minimalny = kortezh3[0]
    y_2_minimalny = kortezh3[1]
    x_2_maksimalny = kortezh4[0]
    y_2_maksimalny = kortezh4[1]
    if isCollisionRect(spisok1, spisok2):
        dlina = min(x_1_maksimalny, x_2_maksimalny) - max(x_1_minimalny, x_2_minimalny)
        shirina = min(y_1_maksimalny, y_2_maksimalny) - max(y_1_minimalny, y_2_minimalny)
        return dlina * shirina
    else:
        return 0
def intersectionAreaMultiRect(spiski):
    def get_intersection(rects):
        x1 = max(rect[0][0] for rect in rects)
        y1 = max(rect[0][1] for rect in rects)
        x2 = min(rect[1][0] for rect in rects)
        y2 = min(rect[1][1] for rect in rects)
        if x1 < x2 and y1 < y2:
            return [(x1, y1), (x2, y2)]
        return None

    def area(rect):
        if not rect:
            return 0
        width = rect[1][0] - rect[0][0]
        height = rect[1][1] - rect[0][1]
        return width * height

    try:
        isCorrectRect(spiski)
    except ValueError as e:
        print(e)
        return 0

    total_area = 0
    all_intersections = []

    for combination in combinations(spiski, 2):
        intersection = get_intersection(combination)
        if intersection:
            all_intersections.append(intersection)

    for k in range(1, len(all_intersections) + 1):
        sign = (-1) ** (k + 1)
        for combination in combinations(all_intersections, k):
            intersection = get_intersection(combination)
            total_area += sign * area(intersection)
    return total_area