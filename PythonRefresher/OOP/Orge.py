from Enemy import *
import random



class Orge(Enemy):
    def __init__(self, health_points,attack_damage):
        super().__init__(type_of_enemy='Orge',
                        health_points=health_points,
                        attack_damage=attack_damage)

    def talk(self):
        print("*Orge is slamming hands all around!*")


    def specical_attack(self):
        did_special_attc_work = random.random() < 0.20
        if did_special_attc_work:
            self.attack_damage += 4 
            print("Orge gets angry and increases attack by 4")