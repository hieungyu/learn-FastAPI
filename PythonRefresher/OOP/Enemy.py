class Enemy:
    # type_of_enemy: str
    # health_points: int = 10
    # attack_damage: int = 2

    '''
    Goal: Show Inheritance
    - Implement Zombie object
    - Explain Superclass / super()
    - Override talk function
    - Create SpreadDisease that Parent does not have
    - Create Ogre class
    - Implement Smash
    '''


    # Using parameters constructor
    def __init__(self, type_of_enemy, health_points = 10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy # double underscore nghĩa là sẽ khóa cái biến đó từ public thành private
        # self.type_of_enemy =  type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        
    def talk(self):
        print(f'I am a New generation Hero {self.__type_of_enemy}. Nhao vo day kiem com ne !!!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you. ')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def specical_attack(self):
        print("Enemy has no special attack.")

    def get_type_of_enemy(self):
        return self.__type_of_enemy