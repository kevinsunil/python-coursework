import pandas
import csv
#csv is a library used to work with csv files as it's difficult to tabulate the data with regular python
# with open("./weather_data.csv") as data:
#     data_list = csv.reader(data)
#     temperature = []
#     i = 0
#     for day in data_list:
#         if i == 0:
#             i += 1
#         else:
#             temperature.append(int(day[1]))
#     print(temperature)
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
data_to_dict = data.to_dict()
print(data_to_dict)
data_temp_list = data["temp"].to_list()
data_avg = sum(data_temp_list)/len(data_temp_list)
print(data_temp_list)
print(data_avg)
print(data["temp"].mean())
print(data[data.temp == data["temp"].max()])
monday = data[data.day == 'Monday']
print (monday.temp)
