# print('Welcome to te rollercoaster!')
# height = int(input('What is your height in cm? '))
#
# if height >= 120:
#     price = 0
#     print('You can ride the rollercoaster')
#     age = int(input('How old are you? '))
#     if age <= 12:
#         print('Child tickets are $5.')
#         price = 5
#     elif age <= 18:
#         print('Youth tickets are $8.')
#         price = 8
#     elif 45 <= age <= 55:
#         print('Everything is going to be ok. Have a free ride on us!')
#     else:
#         print('Adult tickets are $12.')
#         price = 12
#
#     wants_photo = input('Do you want to have a photo taken? Type \'y\' for Yes and \'n\' for No. ')
#     if wants_photo == 'y':
#         price += 3
#
#     print(f'Your final bill is ${price}.')
# else:
#     print('Sorry you have to grow taller before you can ride.')

# # Odd or Even
# number = int(input('Give me a number. '))
# if not number % 2:  # if number % 2 == 0:
#     print('Your number is an even number.')
# else:
#     print('Your number is an odd number.')

SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25
PEPPERONI_S = 2
PEPPERONI_ML = 3
CHEESE = 1

print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L: ').upper()
pepperoni = input('Do you want pepperoni on your pizza? Y or N: ').upper()
extra_cheese = input('Do you want extra cheese? Y or N: ').upper()
bill = 0

if size == 'S':
    if pepperoni == 'Y':
        bill = SMALL_PIZZA + PEPPERONI_S
    else:
        bill = SMALL_PIZZA
    if extra_cheese == 'Y':
        bill += CHEESE
elif size == 'M':
    if pepperoni == 'Y':
        bill = MEDIUM_PIZZA + PEPPERONI_ML
    else:
        bill = MEDIUM_PIZZA
    if extra_cheese == 'Y':
        bill += CHEESE
elif size == 'L':
    if pepperoni == 'Y':
        bill = LARGE_PIZZA + PEPPERONI_ML
    else:
        bill = LARGE_PIZZA
    if extra_cheese == 'Y':
        bill += CHEESE
else:
    print("You typed the wrong input.")

print(f'Your bill is ${bill}.')
