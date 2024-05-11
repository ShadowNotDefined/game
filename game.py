import colorama
from colorama import Fore, Style
import random

colorama.init()  # Enables ANSI escape codes for colored output


# Class Definitions
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0


class Player:
    def __init__(self, name, level, exp, max_hp, hp, attack):
        self.name = name
        self.level = level
        self.exp = exp
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= (50 * (self.level ** 2)):  # Level up condition
            self.level += 1
            self.max_hp *= 1.5  # Increase maximum HP by 50% per level
            self.hp = min(self.max_hp, self.hp)  # Ensure current HP does not exceed new max HP
            self.attack *= 1.25  # Increase attack power by 25% per level
            level_up_message = "Congratulations! You have reached level" + str(self.level) + "!"
            print(level_up_message)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print("You died.")
            return False
        else:
            return True

    def is_dead(self):
        return self.hp == 0


# Game Constants
ENEMY_LIST = [Monster("Slime", 30, 5), Monster("Zombie", 40, 7), Monster("Skeleton", 50, 9)]
BASE_XP_REWARD = 10
BONUS_XP_MULTIPLIER = 10


# Function Definitions
def fight_monster(player, monster):
    print(Style.BRIGHT + Fore.BLUE + "\nA wild " + monster.name + " appeared!")
    while True:
        player_action = input("What will you do?\n1. Attack\n2. Flee\n> ").lower().strip()
        if player_action == "1":
            damage = int(round(player.attack * random.uniform(0.8,
                                                              1.2)))  # Randomized player damage calculation (80% to 120% of base attack value)
            print(Style.BRIGHT + Fore.GREEN + "\nYou attacked the " + monster.name + " for", damage, "damage!")
            monster.take_damage(damage)
            if monster.is_dead():
                print(Style.BRIGHT + Fore.RED + "\nThe " + monster.name + " has been defeated!")
                bonus_xp = int((
                                           player.attack / monster.attack) * BONUS_XP_MULTIPLIER)  # Calculate bonus experience based on relative strength
                player.gain_exp(BASE_XP_REWARD + bonus_xp)  # Award bonus experience along with base experience
                break
            else:
                print(Style.BRIGHT + Fore.RED + "\nThe " + monster.name + "'s health:", monster.health)
                damage = int(round(monster.attack * random.uniform(0.8,
                                                                   1.2)))  # Randomized monster damage calculation (80% to 120% of base attack value)
                print(Style.BRIGHT + Fore.RED + "\nThe " + monster.name + " attacks you for", damage, "damage!")
                player.take_damage(damage)
                if not player.take_damage(damage):  # Check if player died during enemy's turn
                    break
        elif player_action == "2":
            flee_chance = random.randint(1, 10)
            if flee_chance > 4:  # Successful chance to flee
                print(Style.BRIGHT + Fore.CYAN + "\nYou successfully fled the battle!")
                break
            else:
                print(Style.BRIGHT + Fore.RED + "\nYou failed to flee!")
                damage = int(round(monster.attack * random.uniform(0.8,
                                                                   1.2)))  # Randomized monster damage calculation (80% to 120% of base attack value)
                print(Style.BRIGHT + Fore.RED + "\nThe " + monster.name + " hits you for", damage, "damage!")
                player.take_damage(damage)
                if not player.take_damage(damage):  # Check if player died during enemy's turn
                    break
        else:
            print(Style.BRIGHT + Fore.MAGENTA + "\nInvalid action. Try again.")


# Main Program Loop
if __name__ == "__main__":
    player = Player("Adventurer", 1, 0, 100, 100, 10)

    while True:
        current_enemy = random.choice(ENEMY_LIST)
        fight_monster(player, current_enemy)
        if player.is_dead():
            break
