import pandas as pd

df1 = pd.read_csv("pavadinimai_naujas.csv")
df2 = pd.read_csv("naujas.csv")
df3 = pd.concat([df1, df2], axis=1)


print(df3)
df3.to_csv("LENTELĖ")

# df3 = df3.drop(columns=[0])


# df3.to_csv("Ligos index")

# df = pd.read_csv(r"scraped_data.csv.")
# df = df.drop([0,1,2,3,4,5,6])
#
# # df = df.drop(columns=[1])
#
# df = df.iloc[:, 0:5]
# df = df.set_index("data", inplace=True)
# df1 = pd.read_csv(r"skreipinti_pavadinimai.csv")
# df1 = df.set_index("data", inplace=True)
# df2 = pd.concat([df,df1], axis=1)
# print(df2)

# df2.to_csv("Lentlė.csv")

# df.set_index("data", inplace=True)

# df = df.drop(labels=[], inplace=True)

# print(df)
# df["C2"] = df["C2"].str.replace('\xa0', '')

# df["data"] = df["data"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")

# df.to_csv("LIGOS.csv")