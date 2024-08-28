print("---CSV---")

# import csv

# weather_data = []
# with open("weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":                
#             temperatures.append(int(row[1]))
#             print(row)

# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])

# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "players": ["Lebron", "Curry", "Schenk"],
#     "ppg": [32.3, 29.7, 82.1]
# }

#data = pandas.DataFrame(data_dict)
#data.to_csv("players_ppg.csv")

players_data = pandas.read_csv("players_ppg.csv")
#Column
print(players_data.ppg)
#Row
print(players_data[players_data.players == "Lebron"])
