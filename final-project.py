import pandas as pd
import matplotlib.pyplot as plt

###sudarome meniu, kuriame galima išsirinkti norimą funkciją###

def rodyti_meniu():

    print("\n---------------------------Meniu------------------------------------------")
    print("1.Peržiūrėti 5 dažniausius 5 metų suaugusiųjų susirgimų vidurkius")
    print("2.Peržiūrėti 5 rečiausius 5 metų suaugusiųjų susirgimų vidurkius")
    print("3.Spausdinti grafiką: Vidutinis sergančiųjų tam tikra liga 5 metų laikotarpyje skaičius")
    print("4.Spausdinti grafiką: TOP3 vyrų dažniausių ir rečiausių susirgimų 5 metų vidurkiai")
    print("5.Spausdinti grafiką: TOP3 moterų dažniausių ir rečiausių susirgimų 5 metų vidurkiai")
    print("6.Spausdinti grafiką: Vidutinis vyrų ir moterų, sergančiųjų tam tikra liga 5 metų laikotarpyje,"
        "skaičiaus palyginimas")
    print("7.Išeiti")

###išrenkame 5 dažniausiai tarp vyrų ir moterų pasitaikančius susirgimus (pagal 5 metų vidurkį)##

def perziureti_5_dazniausius():

    df_vm = pd.read_csv(r"CSV/VMlent_mean.csv")
    trys_didziausi_sk = df_vm.sort_values(by="mean", ascending=False).head(5)
    print(trys_didziausi_sk)
    return

###išrenkame 5 rečiausiai tarp vyrų ir moterų pasitaikančius susirgimus (pagal 5 metų vidurkį)###

def perziureti_5_reciausius():
    df_vm = pd.read_csv(r"CSV/VMlent_mean.csv")
    trys_maziausi_sk = df_vm.sort_values(by="mean").head(5)
    print(trys_maziausi_sk)
    return

###atspausdiname grafiką, parodantį vidutinį 5 metų laikotarpio vyrų ir moterų sergamumą tam tikra liga###

def vidutinis_serganciuju():

    vm_susirgimai = pd.read_csv(r"CSV/VMlent_mean.csv")
    ligos = vm_susirgimai["Ligos"]
    reiksmes = vm_susirgimai["mean"]

    plt.fig = plt.figure(figsize=(20, 15))
    plt.bar(ligos, reiksmes, color='limegreen')
    plt.xlabel("Ligos")
    plt.ylabel("Ligų vidurkiai")
    plt.title("Vidutinis sergančiųjų tam tikra liga 5 metų laikotarpyje skaičius")
    plt.xticks(rotation=20, ha="right")
    plt.show()
    return

###atspausdiname grafiką su 3 dažniausiai ir rečiausiai pasitaikančiomis vyrų ligomis###

def top3_vyru_dazniausu():

    df_v = pd.read_csv("CSV/Vlent_mean.csv")
    trys_didziausi_sk = df_v.sort_values(by="mean", ascending=False).head(3)
    trys_maziausi_sk = df_v.sort_values(by="mean").head(3)

    plt.fig = plt.figure(figsize=(12, 8))
    plt.bar(trys_didziausi_sk["Ligos"], trys_didziausi_sk["mean"], color='grey')
    plt.bar(trys_maziausi_sk["Ligos"], trys_maziausi_sk["mean"], color='royalblue')
    plt.xlabel('Ligos')
    plt.ylabel('Susirgimų skaičius')
    plt.title('TOP3 vyrų dažniausių ir rečiausių susirgimų 5 metų vidurkiai')
    plt.xticks(rotation=5, ha='right')
    plt.show()
    return

###atspausdiname grafiką su 3 dažniausiai ir rečiausiai pasitaikančiomis moterų ligomis###

def top3_moteru_dazniausiu():

    df_m = pd.read_csv("CSV/Mlent_mean.csv")
    trys_didziausi_sk = df_m.sort_values(by="mean", ascending=False).head(3)
    trys_maziausi_sk = df_m.sort_values(by="mean").head(3)

    plt.fig = plt.figure(figsize=(12, 8))
    plt.bar(trys_didziausi_sk["Ligos"], trys_didziausi_sk["mean"], color='indigo')
    plt.bar(trys_maziausi_sk["Ligos"], trys_maziausi_sk["mean"], color='violet')
    plt.xlabel('Ligos')
    plt.ylabel('Susirgimų skaičius')
    plt.title('TOP3 moterų dažniausių ir rečiausių susirgimų 5 metų vidurkiai')
    plt.xticks(rotation=5, ha='right')
    plt.show()
    return

###atspausdiname grafiką, kuris palygina vyrų ir moterų sergamumo vidurkį per 5 metus###

def vidutinis_vyru_ir_moteru():

    v_susirgimai = pd.read_csv(r"CSV/Vlent_mean.csv")
    m_susirgimai = pd.read_csv(r"CSV/Mlent_mean.csv")

    vligos = v_susirgimai["Ligos"]
    vreiksmes = v_susirgimai["mean"]
    mligos = m_susirgimai["Ligos"]
    mreiksmes = m_susirgimai["mean"]

    plt.fig = plt.figure(figsize=(20, 15))
    plt.plot(vligos, vreiksmes, color='blue')
    plt.plot(mligos, mreiksmes, color='red')
    plt.xlabel("Ligos")
    plt.ylabel("Ligų vidurkiai")
    plt.title("Vidutinis vyrų ir moterų, sergančiųjų tam tikra liga 5 metų laikotarpyje, skaičiaus palyginimas")
    plt.xticks(rotation=20, ha='right')
    plt.show()
    return

###sudarome funkciją, kad veiktų mūsų meniu###

def main():

    while True:
        rodyti_meniu()
        pasirinkimas = input("Pasirinkite norimą funkciją (1-7):->>")
        if pasirinkimas == "1":
            perziureti_5_dazniausius()
        elif pasirinkimas == "2":
            perziureti_5_reciausius()
        elif pasirinkimas == "3":
            vidutinis_serganciuju()
        elif pasirinkimas == "4":
            top3_vyru_dazniausu()
        elif pasirinkimas == "5":
            top3_moteru_dazniausiu()
        elif pasirinkimas == "6":
            vidutinis_vyru_ir_moteru()
        elif pasirinkimas == "7":
            print("Išejote iš programos")
            break
        else:
            print("Neteisingas pasirinkimas. Prašome pasirinkti nuo 1 iki 7 !!!")


main()
