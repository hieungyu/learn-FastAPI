
from Enemy import *
from Zombie import *
from Orge import *
import random

def battle(e1 : Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    print(f"Health {e1.get_type_of_enemy()}:{e1.health_points} and Health {e2.get_type_of_enemy()}: {e2.health_points}")
    while e1.health_points > 0 and e2.health_points > 0:
        
        print("---------------")

        e1.specical_attack
        e2.specical_attack
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")

        e2.attack()
        e1.health_points -= e2.attack_damage
        
        e1.attack()
        e2.health_points -= e1.attack_damage
    
        print("-------------")

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")

atck1 = random.random()
atck2 = random.random()


zombie = Zombie(10,atck1)
orge = Orge(10,atck2)

battle(zombie, orge)