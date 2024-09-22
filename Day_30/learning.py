# # FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     # value = a_dict["none_existent_key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as e:
#     print(f"The key {e} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

# # ValueError
# a_dict = {"key": "value"}
# value = a_dict["none_existent_key"]

# # IndexError
# fruit_list = ["Appel", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

height = float(input("Height(m): "))
weight = int(input("Weight(kg): "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
