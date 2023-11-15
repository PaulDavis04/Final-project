import pandas as pd

df = pd.read_csv(r"bendra_lentele.csv")

df_Vyrai_Moterys = df.iloc[:37,:]
df_Vyrai = df.iloc[37:74,:]
df_Moterys = df.iloc[74:111,:]

df_Vyrai_Moterys.drop([33], axis=0, inplace=True)
df_Vyrai.drop([69,70], axis=0, inplace=True)
df_Moterys.drop([106,107], axis=0, inplace=True)

print("Shape of new dataframes - {} , {}".format(df_Vyrai_Moterys.shape, df_Vyrai.shape))
df_Vyrai_Moterys.to_csv("VYRAI_MOTERYS_lent.csv", index=False)
df_Vyrai.to_csv("VYRAI_lent.csv", index=False)
df_Moterys.to_csv("MOTERYS_lent.csv", index=False)

#vidutinis serganciuju tam tikra liga penkiu metu laikotarpyje skaicius
df_vm = pd.read_csv("VYRAI_MOTERYS_lent.csv")
df_vm['mean'] = df_vm.iloc[:, 2:7].mean(axis=1)
df_vm.to_csv("VMlent_mean.csv", index=False)

#vidutinis VYRU serganciuju tam tikra liga penkiu metu laikotarpyje skaicius
df_v = pd.read_csv("VYRAI_lent.csv")
df_v['mean'] = df_v.iloc[:, 2:7].mean(axis=1)
df_v.to_csv("Vlent_mean.csv", index=False)

#vidutinis MOTERU serganciuju tam tikra liga penkiu metu laikotarpyje skaicius
df_m = pd.read_csv("MOTERYS_lent.csv")
df_m['mean'] = df_m.iloc[:, 2:7].mean(axis=1)
df_m.to_csv("Mlent_mean.csv", index=False)