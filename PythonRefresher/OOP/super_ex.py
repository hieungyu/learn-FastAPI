import random

# =========================
# 1. VŨ KHÍ
# =========================
class Weapon:
    def __init__(self, name, bonus_damage, crit_bonus=0.0):
        self.name = name
        self.bonus_damage = bonus_damage       # + thêm damage
        self.crit_bonus = crit_bonus           # + thêm tỉ lệ chí mạng

    def __str__(self):
        return f"{self.name} (+{self.bonus_damage} dmg, +{self.crit_bonus*100:.0f}% crit)"


# =========================
# 2. NHÂN VẬT CƠ BẢN (CHA)
# =========================
class Character:
    def __init__(self, name, health_points, attack_damage, crit_chance=0.1, weapon: Weapon | None = None):
        self.name = name
        self.max_health = health_points
        self.health_points = health_points
        self.base_attack_damage = attack_damage
        self.crit_chance = crit_chance    # 0.1 = 10%
        self.weapon = weapon

    def is_alive(self):
        return self.health_points > 0

    def talk(self):
        print(f"{self.name}: ...")

    @property
    def attack_damage(self):
        """Damage thực tế = base + bonus vũ khí"""
        if self.weapon:
            return self.base_attack_damage + self.weapon.bonus_damage
        return self.base_attack_damage

    @property
    def total_crit_chance(self):
        if self.weapon:
            return self.crit_chance + self.weapon.crit_bonus
        return self.crit_chance

    def take_damage(self, amount):
        self.health_points = max(0, self.health_points - amount)
        print(f"{self.name} mất {amount} HP (còn {self.health_points}/{self.max_health})")

    def basic_attack(self, target: "Character"):
        """Đánh thường: có thể chí mạng"""
        dmg = self.attack_damage
        is_crit = random.random() < self.total_crit_chance

        if is_crit:
            dmg = int(dmg * 2)
            print(f"🔥 CHÍ MẠNG! {self.name} gây {dmg} damage lên {target.name}!")
        else:
            print(f"{self.name} tấn công {target.name} gây {dmg} damage.")

        target.take_damage(dmg)


# =========================
# 3. HERO
# =========================
class Hero(Character):
    def __init__(self, name, health_points, attack_damage, crit_chance=0.2, weapon: Weapon | None = None):
        super().__init__(name, health_points, attack_damage, crit_chance, weapon)

    def talk(self):
        print(f"{self.name}: Vì công lý!!!")

    def skill_power_strike(self, target: Character):
        """
        Skill: Power Strike
        - Gây 1.5x damage
        - Không crit, nhưng damage to
        """
        dmg = int(self.attack_damage * 1.5)
        print(f"💥 {self.name} dùng skill POWER STRIKE lên {target.name}, gây {dmg} damage!")
        target.take_damage(dmg)


# =========================
# 4. ENEMY + CÁC LOẠI QUÁI
# =========================
class Enemy(Character):
    def __init__(self, name, health_points, attack_damage, crit_chance=0.05, weapon: Weapon | None = None):
        super().__init__(name, health_points, attack_damage, crit_chance, weapon)

    def special_attack(self, target: Character):
        """
        Mặc định Enemy không có skill
        -> Các class con sẽ override
        """
        print(f"{self.name} cố gắng dùng skill đặc biệt... nhưng chẳng có gì xảy ra.")


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__("Zombie", health_points, attack_damage, crit_chance=0.1)

    def talk(self):
        print("Zombie: Braaaainsss...")

    def special_attack(self, target: Character):
        """
        Skill: Regenerate
        - 50% cơ hội hồi 3 HP
        """
        if random.random() < 0.5:
            heal = 3
            self.health_points = min(self.max_health, self.health_points + heal)
            print(f"🧟 Zombie tự hồi {heal} HP! ({self.health_points}/{self.max_health})")
        else:
            print("Zombie cố hồi máu nhưng thất bại...")


class Orge(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__("Orge", health_points, attack_damage, crit_chance=0.05)

    def talk(self):
        print("Orge: UGGHHH! SMASH!")

    def special_attack(self, target: Character):
        """
        Skill: Heavy Smash
        - 40% cơ hội gây 2x damage
        """
        if random.random() < 0.4:
            dmg = self.attack_damage * 2
            print(f"💣 Orge dùng HEAVY SMASH lên {target.name}, gây {dmg} damage!")
            target.take_damage(dmg)
        else:
            print("Orge vung chùy hụt... Không gây được damage.")


# =========================
# 5. HÀM BATTLE TURN-BASED
# =========================
def battle(hero: Hero, enemy: Enemy):
    print("======== TRẬN CHIẾN BẮT ĐẦU ========")
    hero.talk()
    enemy.talk()
    print(f"{hero.name}: {hero.health_points} HP | {enemy.name}: {enemy.health_points} HP\n")

    turn = 1
    while hero.is_alive() and enemy.is_alive():
        print(f"\n----- TURN {turn} -----")

        # HERO HÀNH ĐỘNG
        # VD: 3 turn thì 1 turn dùng skill, còn lại đánh thường
        if turn % 3 == 0:
            hero.skill_power_strike(enemy)
        else:
            hero.basic_attack(enemy)

        if not enemy.is_alive():
            print(f"\n🏆 {hero.name} đã đánh bại {enemy.name}!")
            break

        # ENEMY HÀNH ĐỘNG
        # Cho enemy có 50% dùng skill, 50% đánh thường
        if random.random() < 0.5:
            enemy.special_attack(hero)
        else:
            enemy.basic_attack(hero)

        if not hero.is_alive():
            print(f"\n💀 {hero.name} đã bị hạ gục bởi {enemy.name}...")
            break

        turn += 1

    print("\n======== TRẬN CHIẾN KẾT THÚC ========")


# =========================
# 6. DEMO
# =========================
if __name__ == "__main__":
    # Tạo vũ khí cho hero
    sword = Weapon("Iron Sword", bonus_damage=3, crit_bonus=0.1)

    # Tạo hero
    hero = Hero(name="Hieu", health_points=25, attack_damage=4, crit_chance=0.2, weapon=sword)

    # Tạo quái (bạn có thể đổi Zombie <-> Orge thử)
    enemy = Orge(health_points=30, attack_damage=5)
    # enemy = Zombie(health_points=20, attack_damage=3)

    # Bắt đầu trận
    battle(hero, enemy)
