import pandas as pd
df = pd.read_csv("data.csv",index_col="Name")

tall_pokemon = df[df["Height"] > 2]
print(tall_pokemon)