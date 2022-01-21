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

# Create a character by letting the player answer some questions
def player_creation():
    print("You are once again led by three guards towards the iron gate…")
    print("The iron gate opens slowly, and you feel…")

    """
    Sets the player attributes and making sure they
    input correct data by using a while loop
    """
    player_stats = input("a) ...extra strong.\nb) ...young and athletic.\nc) ...lucky and pumped.\n").lower()
    while player_stats != "a" and player_stats != "b" and player_stats != "c":
        print("You need to type: a, b or c...")
        print("The iron gate opens slowly, and you feel…")
        player_stats = input("a) ...extra strong.\nb) …young and athletic.\nc) …lucky and pumped.\n").lower()

    if player_stats == "a":
        Player.dmg = 40
        Player.health = 80
        Player.luck = random.randint(3, 8)

    elif player_stats == "b":
        Player.dmg = 20
        Player.health = 140
        Player.luck = random.randint(3, 8)

    elif player_stats == "c":
        Player.dmg = 20
        Player.health = 100
        Player.luck = random.randint(5, 8)

    print("\nThe guards turn to you, and you know it's time to pick a weapon...")
    print("Which one do you choose?")

    """
    Add to specific player attribute depending on their choice,
    and making sure they input correct data by using a while loop
    """
    weapon_choice = input("a) Executioner's Sword.\nb) Sword and shield.\nc) Halberd.\n").lower()
    while weapon_choice != "a" and weapon_choice != "b" and weapon_choice != "c":
        print("You need to type: a, b or c...")
        print("Which one do you choose?")
        weapon_choice = input("a) Executioner's Sword.\nb) Sword and shield.\nc) Halberd.\n").lower()

    if weapon_choice == "a":
        Player.dmg += 30

    elif weapon_choice == "b":
        Player.dmg += 10
        Player.health += 20

    elif weapon_choice == "c":
        Player.dmg += 20
        Player.luck += 2

    print("\nAs you enter the arena, you hear the crowd goes wild...")
    Player.name = input("What is your name?\n")
    print(f"\n{Player.name.upper()}! ...echoes through the arena.\n")
    print("Your stats are:")

    return Player(Player.name, Player.dmg, Player.health, Player.luck)


# Create an enemy and set enemy stats
def enemy_creation(elite_enemy):
    
    enemy_name_first = ("Angry", "Big", "Aggresive", "Furious", "Crazy", "Creepy", "Dangerous", "Evil", "Powerful", "Scary")
    enemy_name_last = ("Goblin", "Troll", "Undead", "Monster", "Orc", "Zombie", "Skeleton", "Cyclop", "Dragon", "Ghoul")

    Enemy.name = random.choice(enemy_name_first)+" "+random.choice(enemy_name_last)

    elite_enemy = random.randint(0, 10)

    if elite_enemy >= 7:
        elite_enemy = True
    else:
        elite_enemy = False

    if elite_enemy is True:
        Enemy.dmg = random.randint(15, 30)
        Enemy.health = random.randint(120, 200)
        Enemy.luck = random.randint(3, 10)
        Enemy.special = random.randint(40, 60)

        return Elite(Enemy.name, Enemy.dmg, Enemy.health, Enemy.luck, Enemy.special)

    else:
        Enemy.dmg = random.randint(1, 15)
        Enemy.health = random.randint(50, 120)
        Enemy.luck = random.randint(1, 6)

        return Enemy(Enemy.name, Enemy.dmg, Enemy.health, Enemy.luck)

# Attack function for enemies
def enemy_attack():
    print(f"\n{Enemy.name} rushes towards you and attacks...")
    hit = random.randint(0, 10)

    if hit <= Enemy.luck:
        print("It hits you and does...")
        Player.health -= Enemy.dmg
        print(f"{Enemy.dmg} in damage!")
        return Player.health

    else:
        print(f"{Enemy.name} fumbles and misses!")

# Attack function for player
def player_attack():
    print("\nIn front of you, you can see your opponent...")
    print(f"It's the {Enemy.name}.")
    print("\nIt's stats are:")
    pprint(vars(random_enemy))
    print("\nYou look at the enemy and decides to do a...")
    attack_choice = input("a) Fast attack.\nb) Normal attack.\nc) Charge attack.\n").lower()

    while attack_choice != "a" and attack_choice != "b" and attack_choice != "c":
        print("You need to type: a, b or c...")
        print("\nYou look at the enemy and decide to do a...")
        attack_choice = input("a) Fast attack.\nb) Normal attack.\nc) Charge attack.\n").lower()

    if attack_choice == "a":
        Player.dmg -= 10
        Player.luck += 2
        
    elif attack_choice == "b":
        Player.dmg += 5
        
    elif attack_choice == "c":
        Player.dmg += 20
        Player.luck -= 2

    print(f"\nYou raise your weapon and attack the {Enemy.name}...")
    hit = random.randint(0, 10)

    if hit <= Player.luck:
        print("You hit it and do...")
        Enemy.health -= Player.dmg
        print(f"{Player.dmg} in damage!")
        return Enemy.health

    else:
        print("You fumble and miss!")

    if attack_choice == "a":
        Player.dmg += 10
        Player.luck -= 2
        

    elif attack_choice == "b":
        Player.dmg -= 5
        
    elif attack_choice == "c":
        Player.dmg -= 20
        Player.luck += 2
        

# Battle function
def battle():

    while Player.health > 0 and Enemy.health > 0:

        player_attack()
        print(f"\n{Enemy.name}'s health is now {Enemy.health}.")
        if Enemy.health <= 0:
            print(f"You killed the {Enemy.name}!")
            print(f"Everyone in the arena is shouting your name... {Player.name.upper()}!")
            print(f"Your health is now {Player.health}")
        else:
            enemy_attack()
            print(f"\nYour Health is now {Player.health}.")
        if Player.health <= 0:
            print("You fought your hardest...")
            print("...but it wasn't enough.")
        



player_character = player_creation()
pprint(vars(player_character))
elite_enemy = None
random_enemy = enemy_creation(elite_enemy)
battle()

#battle()
#player_attack()
#print(Player.health)
#print(Enemy.health)
#pprint(vars(player_character))
