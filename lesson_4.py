from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10, 15, 20])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes_list):
        plus_damage = randint(1, 5)
        for hero in heroes_list:
            if hero.health > 0 and type(hero) != Witcher:
                hero.damage += plus_damage


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, 0, 'REVIVE')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health == 0 and self.health > 0:
                hero.health = self.health
                self.health = 0
                print(f'Witcher {self.name} revived {hero.name} by giving him own life({hero.health}hp).')


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STEALING_HP')

    def apply_super_power(self, boss, heroes_list):
        if round_number % 2 == 1:
            hp_amount = randint(1, 20)
            chosen_hero = choice(heroes_list)
            boss.health -= hp_amount
            chosen_hero.health += hp_amount
            print(f'Hacker {self.name} stole {hp_amount} hp from the BOSS and gave it to {chosen_hero.name}')


class Gambler(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'GAMBLING')

    def apply_super_power(self, boss, heroes_list):
        all_heroes_dead = True
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                all_heroes_dead = False
                break
        if all_heroes_dead:
            pass
        else:
            dice_1 = randint(1, 6)
            dice_2 = randint(1, 6)
            if dice_1 == dice_2:
                boss.health -= dice_1 * dice_2
                print(f'Gambler {self.name} did {dice_1 * dice_2} of damage to the BOSS')
            else:
                chosen_hero = choice(heroes_list)
                while chosen_hero.health == 0 or chosen_hero == self:
                    chosen_hero = choice(heroes_list)
                chosen_hero.health -= dice_1 + dice_2
                print(f'Gambler {self.name} did {dice_1 + dice_2} of damage '
                      f'to his own teammate {chosen_hero.name}')


class Avenger(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'DEFENCE_TEAM')

    def apply_super_power(self, boss, heroes_list):
        global if_boss_attack
        if_do = randint(1, 100)
        if if_do < 20:
            if_boss_attack = False
            print(f'Avenger {self.name} created a defense for the entire team for the next round')
        else:
            if_boss_attack = True


round_number = 0
if_boss_attack = True


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    if if_boss_attack:
        boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)


def start_game():
    boss = Boss(name='Minotavr', health=1500, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=15)
    magic = Magic(name='Alice', health=270, damage=5)
    berserk = Berserk(name='Guts', health=220, damage=10)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=5)
    witcher = Witcher(name='Julia', health=350)
    hacker = Hacker(name='Ego', health=110, damage=10)
    gambler = Gambler(name='Marat', health=100, damage=1)
    avenger = Avenger(name='Aqua', health=120, damage=10)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, hacker, gambler, avenger]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()