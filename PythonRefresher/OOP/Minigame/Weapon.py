class Weapon:
    def __init__(self,name,bonus_damage, crit_bonus = 0.0):
        self.name = name
        self.bonus_damage = bonus_damage
        self.crit_bonus = crit_bonus
    
    def __str__(self):
        return f"{self.name} (+{self.bonus_damage} dmg, + {self.crit_bonus*100:.0f} % crit)"
        