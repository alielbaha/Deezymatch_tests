import pandas as pd

def gen(name):
    pass

df = pd.read_csv("names.csv")

first_column = df.columns[0]


df["variations"] = df[first_column].apply(lambda name: ", ".join(gen_variations(name)))


df.to_csv("prenoms_variations.csv", index=False)

print("saved")
