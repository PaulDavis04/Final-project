import pandas as pd

df = pd.read_csv(r"scraped_data.csv.")
df = df.drop([0,1,2,3,4,5,6])

# df = df.drop(columns=[1])

df = df.iloc[:, 0:5]




# df.set_index("data", inplace=True)

# df = df.drop(labels=[], inplace=True)

print(df)
# df["C2"] = df["C2"].str.replace('\xa0', '')

# df["data"] = df["data"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")

df.to_csv("LIGOS.csv")