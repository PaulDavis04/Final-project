import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# df_vm = pd.read_csv("VYRAI_MOTERYS_lent.csv")

##vidutinis serganciuju tam tikra liga penkiu metu laikotarpyje skaicius
# df_vm['mean'] = df_vm.iloc[:, 2:7].mean(axis=1)
#
# df_vm.to_csv("VMlent_mean.csv", index=False)
#
###trys didziausi ir maziausi susirgimu skaiciai
# trys_didziausi_sk = df_vm.sort_values(by="mean",ascending=False).head(3)
# trys_maziausi_sk = df_vm.sort_values(by="mean").head(3)

# print("DataFrame:")
# print(trys_didziausi_sk)
# print(trys_maziausi_sk)
#########################################
# df_v = pd.read_csv("VYRAI_lent.csv")
#
# ##vidutinis VYRU serganciuju tam tikra liga penkiu metu laikotarpyje skaicius
# df_v['mean'] = df_v.iloc[:, 2:7].mean(axis=1)
#
# df_v.to_csv("Vlent_mean.csv", index=False)
#
# ##trys didziausi ir maziausi VYRU susirgimu skaiciai
# trys_didziausi_sk = df_v.sort_values(by="mean",ascending=False).head(3)
# trys_maziausi_sk = df_v.sort_values(by="mean").head(3)
#
# print("DataFrame:")
# print(trys_didziausi_sk)
# print(trys_maziausi_sk)
#
# result = df_v.dtypes
# print("Output:")
# print(result)
##########################################

# df_m = pd.read_csv("MOTERYS_lent.csv")
#
# ##vidutinis MOTERU serganciuju tam tikra liga penkiu metu laikotarpyje skaicius
# df_m['mean'] = df_m.iloc[:, 2:7].mean(axis=1)
#
# df_m.to_csv("Mlent_mean.csv", index=False)
#
# ##trys didziausi ir maziausi MOTERU susirgimu skaiciai
# trys_didziausi_sk = df_m.sort_values(by="mean",ascending=False).head(3)
# trys_maziausi_sk = df_m.sort_values(by="mean").head(3)
#
# print("DataFrame:")
# print(trys_didziausi_sk)
# print(trys_maziausi_sk)
#
# result = df_m.dtypes
# print("Output:")
# print(result)
##########################################






# pardavimu_sumos_vidurkis_pagal_imone.to_csv("pardavimai pagal data.csv", index=False)

# print(pardavimu_sumos_vidurkis_pagal_imone)




# vidurkis = data.mean()
# print(df_vm)
# print(df_vm.mean())

##--daznaiusiai ir reciausiai pasitaikancios ligos pagal metus



# data = pd.Series(data=vertinimas, index=knygos)




# # vertinimas = [4.9, 4.2, 4.3, 3.8, 4.5]
# # .
# # print(f"vidutinis knygu ivertinimas: {vidurkis}")


# ## # print(data)
# # knygos = ["Haris Poteris", "Alchemikas", "Mazasis princas", "Mobis Dikas", "Don Kichotas"]
# # std_nuokrypis = data.std().round(2)
# #
# # auksciausias_ivertinimas = data.idmax()
# # print(f"auksciausia ivertinima turinti knyga: {auksciausias_ivertinimas}")

# skaiciai = [10,20,30,40
#
# suma = sum(skaiciai)
#
#
# vidurkis = suma /len(skaiciai)
#
#
#
#
# sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0