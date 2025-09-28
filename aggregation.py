import pandas as pd

df = pd.read_csv("data.csv")
print(df.mean(numeric_only=True)) #sum(),min(),max(),count(),

#No           75.500000
#Height        1.200000
#Weight       46.231333
#Legendary     0.026667
#dtype: float64

print(df["Height"].mean())  #mean of the height column

group = df.groupby("Type1")
print(group["Height"].mean()) #average height for each type