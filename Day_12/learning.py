enemies = "Skeleton"


def increase_enemies():
    global enemies  # Not recommended using global variables
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# # Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
# # print(potion_strength)  # NameError: not defined

# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()


print(player_health)

# There is no Block Scope in Python!
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # This could cause unexpected problems 'undefined'.This can be fixed be by pre declaring the variable.

# Global Constants 'All uppercase'
PI = 3.14159
