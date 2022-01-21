import random
from pprint import pprint


class Player:
    """
    Creates class for player
    """
    def __init__(self, name, dmg, health, luck):
        self.name = name
        self.dmg = dmg
        self.health = health
        self.luck = luck


class Enemy:
    """
    Creates base class for enemies
    """
    def __init__(self, name, dmg, health, luck):
        self.name = name
        self.dmg = dmg
        self.health = health
        self.luck = luck


class Elite(Enemy):
    """
    Create elite enemies by inherit from enemy class
    """
    def __init__(self, name, dmg, health, luck, special):
        super().__init__(name, dmg, health, luck)
        self.special = special


def create_player():
    """
    Create a character by letting the player answer some questions.
    It also sets the player attributes and making sure they
    input correct data by using a while loop.
    """
    player = Player("Test", 0, 0, 0,)
    print("You are once again led by three guards towards the iron gate…")
    print("The iron gate opens slowly, and you feel…")

    player_stats = input("""
        a) ...extra strong.
        b) ...young and athletic.
        c) ...lucky and pumped.\n""").lower()

    while player_stats != "a" and player_stats != "b" and player_stats != "c":
        print("You need to type: a, b or c...")
        print("The iron gate opens slowly, and you feel…")
        player_stats = input("""
            a) ...extra strong.
            b) …young and athletic.
            c) …lucky and pumped.\n""").lower()

    if player_stats == "a":
        player.dmg = 40
        player.health = 80
        player.luck = random.randint(3, 8)

    elif player_stats == "b":
        player.dmg = 20
        player.health = 140
        player.luck = random.randint(3, 8)

    elif player_stats == "c":
        player.dmg = 20
        player.health = 100
        player.luck = random.randint(5, 8)

    print("The guards turn to you...")
    print("\n...and you know it's time to pick a weapon...")
    print("Which one do you choose?")

    weapon = input("""
        a) Executioner's Sword.
        b) Sword and shield.
        c) Halberd.\n""").lower()

    while weapon != "a" and weapon != "b" and weapon != "c":
        print("You need to type: a, b or c...")
        print("Which one do you choose?")
        weapon = input("""
            a) Executioner's Sword.
            b) Sword and shield.
            c) Halberd.\n""").lower()

    if weapon == "a":
        player.dmg += 30

    elif weapon == "b":
        player.dmg += 10
        player.health += 20

    elif weapon == "c":
        player.dmg += 20
        player.luck += 2

    print("As you enter the arena, you hear the crowd goes wild...")
    player.name = input("What is your name?\n")
    print(f"\n{player.name.upper()}! ...echoes through the arena.\n")
    print("Your stats are:")
    pprint(vars(player))
    return player


def create_enemy():
    """
    Create an enemy and set enemy stats
    """
    enemy = Enemy("Test", 0, 0, 0,)
    elite_enemy = Elite("Test", 0, 0, 0, 0)
    enemy_first = (
            "Angry", "Big", "Aggresive", "Furious", "Crazy",
            "Creepy", "Dangerous", "Evil", "Powerful", "Scary"
        )
    enemy_last = (
            "Goblin", "Troll", "Undead", "Monster", "Orc",
            "Zombie", "Skeleton", "Cyclop", "Dragon", "Ghoul"
        )

    enemy.name = random.choice(enemy_first)+" "+random.choice(enemy_last)

    elite_enemy = random.randint(0, 10)

    if elite_enemy >= 1:
        elite_enemy = True
    else:
        elite_enemy = False

    if elite_enemy is True:
        enemy.dmg = random.randint(15, 30)
        enemy.health = random.randint(120, 200)
        enemy.luck = random.randint(3, 10)
        enemy.special = random.randint(40, 60)

        return Elite(
                enemy.name, enemy.dmg, enemy.health,
                enemy.luck, enemy.special
            )

    else:
        enemy.dmg = random.randint(1, 15)
        enemy.health = random.randint(50, 120)
        enemy.luck = random.randint(1, 6)
    return enemy


def enemy_attack():
    """
    Attack function for enemies
    """
    print(f"\n{enemy.name} rushes towards you and attacks...")
    hit = random.randint(0, 10)

    if hit <= enemy.luck:
        if hasattr(enemy, "special"):
            strike = random.randint(0, 10)
            if strike < enemy.luck:
                print("It hits you with its special attack and does...")
                player.health -= enemy.special
                print(f"{enemy.special} in damage!")
                return player.health
            else:
                print("It hits you and does...")
                player.health -= enemy.dmg
                print(f"{enemy.dmg} in damage!")
                return player.health

    else:
        print(f"{enemy.name} fumbles and misses!")


def player_attack():
    """
    Attack function for player
    """

    print("\nYou look at the enemy and decides to do a...")
    attack = input("""
        a) Fast attack.
        b) Normal attack.
        c) Charge attack.\n""").lower()

    while attack != "a" and attack != "b" and attack != "c":
        print("You need to type: a, b or c...")
        print("\nYou look at the enemy and decide to do a...")
        attack = input("""
            a) Fast attack.
            b) Normal attack.
            c) Charge attack.\n""").lower()

    if attack == "a":
        print("You raise your wepaon...")
        print(f"and attack the {enemy.name} with a fast attack!\n")

    elif attack == "b":
        print("You raise your wepaon...")
        print(f"and attack the {enemy.name} with a normal attack!\n")

    elif attack == "c":
        print("You raise your wepaon...")
        print(f"and attack the {enemy.name} with a charge attack!\n")

    hit = random.randint(0, 10)

    if hit <= player.luck:
        print("You hit it and do...")
        enemy.health -= player.dmg
        print(f"{player.dmg} in damage!")
        return enemy.health

    else:
        print("You fumble and miss!")


def battle():
    """
    Battle function
    """
    while player.health > 0 and enemy.health > 0:
        player_attack()
        print(f"\n{enemy.name}'s health is now {enemy.health}.")
        if enemy.health <= 0:
            print(f"You killed the {enemy.name}!\n")
            print("Everyone in the arena is shouting your name...")
            print(f"{player.name.upper()}!")
            print(f"Your health is now {player.health}...")
        else:
            enemy_attack()
            print(f"\nYour Health is now {player.health}.")
        if player.health <= 0:
            print("You fought your hardest...")
            print("...but it wasn't enough.")


elite_enemy = None
player = create_player()
enemy = create_enemy()
print("\nIn front of you, you can see your opponent...")
print(f"It's the {enemy.name}.")
print("\nIt's stats are:")
pprint(vars(enemy))
battle()
