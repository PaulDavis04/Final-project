import pandas as pd

df = pd.read_csv(r"bendra_lentele.csv")

df_Vyrai_Moterys = df.iloc[:37,:]
df_Vyrai = df.iloc[37:74,:]
df_Moterys = df.iloc[74:111,:]


print("Shape of new dataframes - {} , {}".format(df_Vyrai_Moterys.shape, df_Vyrai.shape))
df_Vyrai_Moterys.to_csv("Vyrai_Moterys.csv", index=False)
df_Vyrai.to_csv("Vyrai.csv", index=False)
df_Moterys.to_csv("Moterys.csv", index=False)