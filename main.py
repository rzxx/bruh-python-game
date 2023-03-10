import random
 
hp1 = 100
hp2 = 100
at1 = 10
at2 = 100
 
# 1 - at
# 2 - he
# 3 - def
print("Dark Souls 4.\n1 - атака\n2 - лечение\n3 - защита")
while True:
    move = int(input())
    print("\n")
    enMove = random.randint(1, 3)
    if move == 1:
        print("//ты атаковал")
        if enMove != 3:
            hp2 -= at1
            print("попадание", at1)
        else:
            print("не пробил")
    elif move == 2:
        hp1 += 10
        print("//ты вылечился")
        print("увеличено: ", 10)
    else:
        print("//защита")
 
    if enMove == 1:
        print("//враг атаковал")
        if move != 3:
            print("попадание", at2)
            hp1 -= at2
        else:
            print("не пробил")
    elif enMove == 2:
        print("//враг лечится")
        print("увеличено: ", 2)
        hp2 += 2
    else:
        print("//враг защищается")
 
    print("\n//твои хп: ", hp1, "хп врага: ", hp2)
    print("\n")
    if hp1 <= 0:
        print("поражение")
        print("\nновая игра\n\n")
        hp1 = 100
        hp2 = 100
        continue
    elif hp2 <= 0:
        print("победа")
        break
 
