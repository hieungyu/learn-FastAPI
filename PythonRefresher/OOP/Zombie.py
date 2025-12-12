from Enemy import *
import random 


class  Zombie(Enemy):
    
    def __init__(self, health_points,attack_damage):
        super().__init__(type_of_enemy='Zombie',
                        health_points=health_points,
                        attack_damage=attack_damage)

    def talk(self):
        print("*Grumbling.....*")
    
    def spread_disease(self):
        print('The zombie is trying to spread infrection !!')

    def specical_attack(self):
        did_special_attc_work = random.random() < 0.50
        if did_special_attc_work:
            self.health_points += 2 
            print("Zombie regerated 2HP!")

class Hero(Enemy):
    def __init__(self, health_points,attack_damage):
        super().__init__(type_of_enemy='Hero',
                        health_points=health_points,
                        attack_damage=attack_damage)
    def talk(self):
        print("*I'm comming.....*")
    
    def save_mn(self):
        print('Hero save the world !!')

    def specical_attack(self):
        did_special_attc_work = random.random() < 0.50
        if did_special_attc_work:
            self.health_points += 2 
            print("Zombie regerated 2HP!")