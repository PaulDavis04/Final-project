import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rodyti_meniu():
    print("\n---------------------------Meniu------------------------------------------")
    print("1.Peržiūrėti 5 dažniausius 5 metų suaugusiųjų susirgimų vidurkius")
    print("2.Peržiūrėti 5 rečiausius 5 metų suaugusiųjų susirgimų vidurkius")
    print("3.Spausdinti grafiką: Vidutinis sergančiųjų tam tikra liga 5 metų laikotarpyje skaičius")
    print("4.Spausdinti grafiką: TOP3 vyrų dažniausių ir rečiausių susirgimų 5 metų vidurkiai")
    print("5.Spausdinti grafiką: TOP3 moterų dažniausių ir rečiausių susirgimų 5 metų vidurkiai")
    print("6.Spausdinti grafiką: Vidutinis vyrų ir moterų, sergančiųjų tam tikra liga 5 metų laikotarpyje, skaičiaus palyginimas")
    print("7.Išeiti")

def Peržiūrėti_5_dažniausius():
    df_vm = pd.read_csv(r"CSV/VMlent_mean.csv")
    trys_didziausi_sk = df_vm.sort_values(by="mean", ascending=False).head(5)
    print(trys_didziausi_sk)
    return

def Peržiūrėti_5_rečiausius():
    df_vm = pd.read_csv(r"CSV/VMlent_mean.csv")
    trys_maziausi_sk = df_vm.sort_values(by="mean").head(5)
    print(trys_maziausi_sk)
    return

def Vidutinis_serganciųjų():
    VM_susirgimai = pd.read_csv(r"CSV/VMlent_mean.csv")
    ligos = VM_susirgimai["Ligos"]
    reiksmes = VM_susirgimai["mean"]

    fig = plt.figure(figsize=(20, 15))
    plt.bar(ligos, reiksmes, color='maroon')
    plt.xlabel("Ligos")
    plt.ylabel("Ligų vidurkiai")
    plt.title("Susirgimų vidurkiai")
    plt.xticks(rotation=20, ha="right")
    plt.show()
    return

def TOP3_vyrų_dažniausių():
    df_v = pd.read_csv("CSV/Vlent_mean.csv")
    trys_didziausi_sk = df_v.sort_values(by="mean",ascending=False).head(3)
    trys_maziausi_sk = df_v.sort_values(by="mean").head(3)

    fig = plt.figure(figsize=(12, 8))
    plt.bar(trys_didziausi_sk["Ligos"], trys_didziausi_sk["mean"])
    plt.bar(trys_maziausi_sk["Ligos"], trys_maziausi_sk["mean"])
    plt.xlabel('Ligos')
    plt.ylabel('Susirgimų skaičius')
    plt.title('Trys didžiausi ir mažiausi vyrų susirgimų skaičiai')
    plt.xticks(rotation=5, ha='right')
    plt.show()

    return
def TOP3_moterų_dažniausių():
    df_m = pd.read_csv("CSV/Mlent_mean.csv")
    trys_didziausi_sk = df_m.sort_values(by="mean", ascending=False).head(3)
    trys_maziausi_sk = df_m.sort_values(by="mean").head(3)

    fig = plt.figure(figsize=(12, 8))
    plt.bar(trys_didziausi_sk["Ligos"], trys_didziausi_sk["mean"])
    plt.bar(trys_maziausi_sk["Ligos"], trys_maziausi_sk["mean"])
    plt.xlabel('Ligos')
    plt.ylabel('Susirgimų skaičius')
    plt.title('Top trys didžiausių ir mažiausių moterų susirgimų per 5 metus skaičių vidurkis ')
    plt.xticks(rotation=5, ha='right')
    plt.show()

    return
def Vidutinis_vyrų_ir_moterų():
    V_susirgimai = pd.read_csv(r"CSV/Vlent_mean.csv")
    M_susirgimai = pd.read_csv(r"CSV/Mlent_mean.csv")

    Vligos = V_susirgimai["Ligos"]
    Vreiksmes = V_susirgimai["mean"]
    Mligos = M_susirgimai["Ligos"]
    Mreiksmes = M_susirgimai["mean"]

    fig = plt.figure(figsize=(20, 15))
    plt.plot(Vligos, Vreiksmes, color='blue')
    plt.plot(Mligos, Mreiksmes, color='red')
    plt.xlabel("Ligos")
    plt.ylabel("Ligų vidurkiai")
    plt.title("Susirgimų vidurkiai")
    plt.xticks(rotation=20, ha='right')
    plt.show()

    return
def main():

    while True:
        rodyti_meniu()
        pasirinkimas = input("Pasirinkite norimą funkciją (1-7):->>")
        if pasirinkimas == "1":
            Peržiūrėti_5_dažniausius()
        elif pasirinkimas == "2":
            Peržiūrėti_5_rečiausius()
        elif pasirinkimas == "3":
            Vidutinis_serganciųjų()
        elif pasirinkimas == "4":
            TOP3_vyrų_dažniausių()
        elif pasirinkimas == "5":
            TOP3_moterų_dažniausių()
        elif pasirinkimas == "6":
            Vidutinis_vyrų_ir_moterų()
        elif pasirinkimas == "7":
            print("Išejote iš programos")
            break
        else:
            print("Neteisingas pasirinkimas. Prašome pasirinkti nuo 1 iki 7 !!!")

main()

