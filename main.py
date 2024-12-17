from collision import isCorrectRect
from collision import isCollisionRect
from collision import intersectionAreaRect
from collision import intersectionAreaMultiRect
status = True
isCorrectRect_rect = [(-3.4, 1),(9.2, 10)] # <- Здесь можно заменить на свои значения для isCorrectRect
isCollisionRect_rect1 = [(-3.4, 1),(9.2, 10)] # <- Здесь можно заменить на свои значения для isCollisionRect
isCollisionRect_rect2 = [(-7.4, 0),(13.2, 12)] # <- Здесь можно заменить на свои значения для isCollisionRect
intersectionAreaRect_rect1 = [(-3, 1), (9, 10)] # <- Здесь можно заменить на свои значения для intersectionAreaRect
intersectionAreaRect_rect2 = [(-7, 0), (13, 12)] # <- Здесь можно заменить на свои значения для intersectionAreaRect
intersectionAreaMultiRect_rect = [ # <- Здесь можно заменить на свои значения для intersectionAreaMultiRect
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
while status:
    decor = "=" * 20
    print(f"{decor}{decor}")
    print("Выберите функцию, чтобы применить ее")
    print("1 - isCorrectRect")
    print("2 - isCollisionRect")
    print("3 - intersectionAreaRect")
    print("4 - intersectionAreaMultiRect")
    print("5 - Выйти из программы")
    print(decor + decor)
    a = int(input())
    print(decor + decor)
    if a == 1:
        print(isCorrectRect(isCorrectRect_rect))
    elif a == 2:
        print(isCollisionRect(isCollisionRect_rect1, isCollisionRect_rect2))
    elif a == 3:
        print(intersectionAreaRect(intersectionAreaRect_rect1, intersectionAreaRect_rect2))
    elif a == 4:
        print(intersectionAreaMultiRect(intersectionAreaMultiRect_rect))
    elif a == 5:
        status = False
    else:
        print("Введите корректное значение")