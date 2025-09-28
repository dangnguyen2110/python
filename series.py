import pandas as pd

data = [100,102,104]
series = pd.Series(data)
print(series)
#0    100
#1    102
#2    104
#dtype: int64

data = [100,102,104]
series = pd.Series(data, index = ["a","b","c"])
print(series)
#dog      100
#cat      102
#mouse    104
#dtype: int64

data = [100,102,104]
series = pd.Series(data, index = ["a","b","c"])
print(series.loc["c"]) #104
series.loc["c"] = 200 #200
print(series.loc[0]) #100

data = [100,102,104,200,250]
series = pd.Series(data, index = ["a","b","c","d","e"])
print(series[series>=200])
#d    200
#e    250
#dtype: int64

calories = {"Day1":1020,"Day2":940,"Day3":1403}
series = pd.Series(calories)
print(series)
#Day1    1020
#Day2     940
#Day3    1403
#dtype: int64


