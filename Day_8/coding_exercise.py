# TODO Life in Weeks
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# **Warning** The function must be called life_in_weeks for the tests to pass.
# Also, the output must have the same punctuation and spelling as the example. Including the full stop!


def life_in_weeks(current_age: int) -> None:
    years_left = 90 - current_age
    weeks_left = years_left * 52.143
    print(f'You have {int(weeks_left)} weeks left.')


life_in_weeks(20)


# Love Calculator
# 💪 This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53

def calculate_love_score(lover_name_1: str, lover_name_2: str) -> None:
    name_combined: str = lover_name_1 + lover_name_2
    true_found: int = 0
    love_found: int = 0
    for letter in name_combined:
        if letter.lower() in 'true':
            true_found += 1
        if letter.lower() in 'love':
            love_found += 1
    print(f'Love Score {true_found}{love_found}')


calculate_love_score('Kanye West', 'Kim Kardashian')
