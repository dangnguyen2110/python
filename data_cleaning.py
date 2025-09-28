import pandas as pd
df = pd.read_csv("data.csv")

#1. Drop irrelevant column
df = df.drop(columns="Legendary")
print(df)

#2. Handle missing data
df = df.dropna(subset=["Type2"]) #drop rows that missing value
df = df.fillna({"Type":"None"})
print(df)

#3. Fix inconsistent value
df["Type1"] = df["Type1"].replace({"Grass":"GRASS"}) 

#4. Standarized text
df["Name"] = df["Name"].str.lower() #turn all name into lowercase

#5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool)
print(df.to_string()) #Chang 1,0 to True, False

#6. Remove duplicate value
df = df.drop_duplicates()
print(df.to_string())