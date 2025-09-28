import pandas as pd
df = pd.read_csv("data.csv")

#SELECTION BY COLUMN
print(df["Name"]) #Actually a serie

print(df["Name"].to_string()) #Print all name. BE CAREFUL WITH BIG DATA!!!

print(df[["Name","Height","Weight"]])


#SELECTION BY ROW
print(df.loc[0]) #print the first row

df = pd.read_csv("data.csv",index_col="Name") #change the label to name
print(df.loc["Mewtwo"]) #search easier with name instead of number

df = pd.read_csv("data.csv",index_col="Name")
print(df.loc["Mewtwo",["Height","Weight"]]) #print the exact needed data

df = pd.read_csv("data.csv",index_col="Name")
print(df.loc["Pikachu":"Mewtwo",["Height","Weight"]]) #print range of row

print(df.iloc[:11]) #print first 11 rows
print(df.iloc[:11,:3]) #print first 11 rows & first 3 columns

#POKEMON GAME
df = pd.read_csv("data.csv",index_col="Name")
pokemon = input("What is your favorite pokemon: ")
try:
    print(df.loc[pokemon])
except:
    print(f"{pokemon} not found")
