# Debugging

# def my_function():
#     for i in range(1, 20):  # fix: range(1, 21)
#         if i == 20:
#             print("You got it")
#
#
# my_function()
#
# # Describe the Problem - Write your answers as comments:
# # 1. What is the for loop doing? Loops through a range of 1 - 19
# # 2. When is the function meant to print "You got it"? When 'i' is 20
# # 3. What are your assumptions about the value of i? It will never become 20

# from random import randint
# dice_images = ['1', '2', '3', '4', '5', '6']
# dice_num = randint(1, 6)  # fix: randint(0, 5) because randint includes both ends.
# print(dice_images[dice_num])

# year = int(input("What's your year of birth?"))
#
# if 1981 < year < 1996:  # fix: <= 1996
#     print("You are a Millennial.")
# elif year > 1996:
#     print("You are a Gen Z.")

# age = int(input("How old are you? "))  # fix: using try - except ValueError
# if age > 18:
#     print(f"You an drive ate age {age}")
