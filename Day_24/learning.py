# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # Read
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # Write
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# Append
with open("my_file.txt", "a") as file:
    file.write("\nNew text.")
