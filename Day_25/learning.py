import pandas
import csv


# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures: list[int] = []
#     for index, row in enumerate(data):
#         if index != 0:
#             temperatures.append(int(row[1]))
#
# print(data)
# print(temperatures)

# data = pandas.read_csv("weather_data.csv")
#
# # print(type(data['temp']))
# # print(type(data))
#
# print(data)
#
# data_dict: dict = data.to_dict()
# print(data_dict)
# temp_list: list = data["temp"].to_list()
# print(temp_list)
#
# # avg: float = sum(temp_list)
# # avg /= len(temp_list)
# avg: float = data["temp"].mean()
# print(f"avg temp: {avg: .2f}")
#
# max_value: int = data["temp"].max()
# print(f"max temp: {max_value}")
#
# # Get Data in Columns
# print(data.condition)
#
# # Get Data in Row
# print(data[data.temp == max_value])
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# # Create DataFrame from scratch
# data_dict: dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240914.csv")
gray_squirrels_count = len(data["Primary Fur Color"] == "Gray")
black_squirrels_count = len(data["Primary Fur Color"] == "Black")
cinnamon_squirrels_count = len(data["Primary Fur Color"] == "Cinnamon")

data_dict: dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
