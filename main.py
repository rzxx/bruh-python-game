import random
 
class Enemy():
    def __init__(self, health_, attack_, heal_):
        self.health = health_
        self.attack = attack_
        self.heal = heal_
 
class Player():
    def __init__(self, health_, attack_, heal_):
        self.health = health_
        self.attack = attack_
        self.heal = heal_
 
# 1 - at
# 2 - he
# 3 - def
print("Dark Souls 4.\n1 - атака\n2 - лечение\n3 - защита")
def Fight(player, enemy):
    while True:
        move = int(input())
        print("\n")
        try:
            enMove = random.randint(1, 3)
        except:
            print("неверный ввод!")
            continue
        if move != 1 and move != 2 and move != 3:
            print("неверный ввод!")
            continue
        if move == 1:
            print("//ты атаковал")
            if enMove != 3:
                enemy.health -= player.attack
                print("попадание", player.attack)
            else:
                print("не пробил")
        elif move == 2:
            player.health += player.heal
            print("//ты вылечился")
            print("увеличено: ", player.heal)
        else:
            print("//защита")
    
        if enMove == 1:
            print("//враг атаковал")
            if move != 3:
                print("попадание", enemy.attack)
                player.health -= enemy.attack
            else:
                print("не пробил")
        elif enMove == 2:
            print("//враг лечится")
            print("увеличено: ", enemy.heal)
            enemy.health += enemy.heal
        else:
            print("//враг защищается")
    
        print("\n//твои хп: ", player.health, "хп врага: ", enemy.health)
        print("\n")
        if player.health <= 0:
            print("поражение")
            break
        elif enemy.health <= 0:
            print("победа")
            break
 
 
 
while True:
    player = Player(100, 10, 10)
    enemy1 = Enemy(100, 100, 2)
    Fight(player, enemy1)
