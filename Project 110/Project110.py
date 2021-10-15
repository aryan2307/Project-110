import statistics as stats
import pandas as pd
import csv
import random as rd
import plotly.figure_factory as ff

df = pd.read_csv(r"C:/Users/Admin/Downloads/Project 110/data.csv")
time = df["reading_time"].tolist()

mean = stats.mean(time)
std = stats.stdev(time)
meanList = []

for i in range(0, 100):
    dataSet = []
    for i in range(0, 30):
        rand_ind = rd.randint(0, len(time)-1)
        value = time[rand_ind]
        dataSet.append(value)
    m = stats.mean(dataSet)
    meanList.append(m)

print(len(meanList))
print(meanList)

finalMean = stats.mean(meanList)
print(finalMean)
print(mean)
print(std)

fig = ff.create_distplot([meanList], ["Means of Samples"], show_hist=False)
fig.show()