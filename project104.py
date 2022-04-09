import pandas as pd

import csv
from collections import Counter

# x = "Hhhheeeelllooooooooo"
# data2 = Counter(x)
# print(data2.items())
# print(data2.values())

data = pd.read_csv("data.csv")

height = data["Height(Inches)"].tolist()

mode_data_for_range = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0,
}

for height , occurence in height.items():
    if 50 < float(height) < 60 :
        mode_data_for_range["50-60"] += occurence

    elif 60 < float(height) < 70 :
        mode_data_for_range["60-70"] += occurence
    
    elif 70 < float(height) < 80 :
        mode_data_for_range["70-80"] += occurence 


mode_range , mode_occurence = 0 , 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1]) / 2)

print("Mode is -> " , mode )

# 50-60 : 12000
# 60-70 : 10000
# 70-80 : 3000




