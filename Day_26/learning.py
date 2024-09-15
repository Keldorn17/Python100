import random
import pandas

# List Comprehension
# new_list = [new_item for item in Iterable]

numbers: list[int] = [1, 2, 3]
new_list: list[int] = [n + 1 for n in numbers]
print(new_list)

name: str = "Keldorn"
letter_list: list[str] = [letter for letter in name]
print(letter_list)

number_list: list[int] = [n * 2 for n in range(1, 5)]
print(number_list)

# Conditional List Comprehension
# new_list = [new_item for item in Iterable if test]
names: list[str] = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names: list[str] = [name for name in names if len(name) < 5]
long_names: list[str] = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)

# Dictionary Comprehension
# new_dict = {new_key: new_value for item in Iterable}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

names: list[str] = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores: dict = {student: random.randint(0, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Looping through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
