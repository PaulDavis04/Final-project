import pandas as pd

df = pd.read_csv(r"C:\Users\pauli\OneDrive\Dokumentai\GitHub\Final-project\LIGOS.csv")
#
# df = df.rename(columns={"Suply":"Supply"})

df = df.drop([0,2,3,4,5,6,8])
df.set_index("column_name", inplace=True)
df = df.drop(labels=your_dict.keys(), inplace=True)


# df["Name"] = df["Name"].str.lstrip("")
# df["Price"] = df["Price"].str.lstrip("€")
# df["Market cap"] = df["Market cap"].str.lstrip("€")
# df["Volume (24)"] = df["Volume (24)"].str.lstrip("€")

df.to_csv("LIGOS_redaguotas1.csv", index=False)