# # Squaring Numbers
# # You are going to write a List Comprehension to create a new list called squared_numbers.
# # This new list should contain every number in the list numbers but each number should be squared.
# # e.g.
# # 4 * 4 = 16
# # 4 squared equals 16.
# # **DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop.
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)

# # Filtering Even Numbers
# # In this list comprehension exercise you will practice using list comprehension to
# # filter out the even numbers from a series of numbers.
# # First, use list comprehension to convert the list_of_strings to a list of integers called numbers.
# # Then use list comprehension again to create a new list called result.
# # This new list should only contain the even numbers from the list numbers.
# # Again, try to use Python's List Comprehension instead of a Loop.
#
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(item) for item in list_of_strings]
# result = [item for item in numbers if item % 2 == 0]
# print(result)

# # Data Overlap
# # 💪 This exercise is HARD 💪
# # Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# # You are going to create a list called result which contains the numbers that are common in both files.
# # e.g. if file1.txt contained:
# # 1
# # 2
# # 3
# # and file2.txt contained:
# # 2
# # 3
# # 4
# # result = [2, 3]
# # IMPORTANT:  The output should be a list of integers and not strings!
# # Try to use List Comprehension instead of a Loop.
#
#
# with open("file1.txt") as file:
#     file1 = file.readlines()
#
# with open("file2.txt") as file:
#     file2 = file.readlines()
#
# result = [int(item) for item in file1 if item in file2]
#
# print(result)

# # Dictionary Comprehension 1
# # You are going to use Dictionary Comprehension to create a dictionary called result that
# # takes each word in the given sentence and calculates the number of letters in each word.
# # Try Googling to find out how to convert a sentence into a list of words.  *
# # *Do NOT** Create a dictionary directly.
# # Try to use Dictionary Comprehension instead of a Loop.
# # To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word.
# # Note that "Swallow?" therefore has a length of 8.
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each
# temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f
# Celsius to Fahrenheit chart
# **Do NOT** Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (celsius * 9 / 5) + 32 for (day, celsius) in weather_c.items()}

print(weather_f)
