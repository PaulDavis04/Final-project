import pandas as pd

df = pd.read_csv(r"bendra_lentele.csv")

df_Vyrai_Moterys = df.iloc[:37,:]
df_Vyrai = df.iloc[37:74,:]
df_Moterys = df.iloc[74:111,:]


print("Shape of new dataframes - {} , {}".format(df_Vyrai_Moterys.shape, df_Vyrai.shape))
df_Vyrai_Moterys.to_csv("VYRAI_MOTERYS_lent.csv", index=False)
df_Vyrai.to_csv("VYRAI_lent.csv", index=False)
df_Moterys.to_csv("MOTERYS_lent.csv", index=False)