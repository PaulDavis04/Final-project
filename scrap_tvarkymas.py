import pandas as pd

###nuskaitome išscrapintų reikšmių csv failą, išdropinam nereikalingus stulpelius ir eilutes###
df = pd.read_csv(r"CSV/scraped_data.csv.")
df.drop(df.iloc[:, 5:566], inplace=True, axis=1)
df.drop([0,1,2,3,4,5,6], axis=0, inplace=True)

###pakeičiame stulpelių pavadinimus###
df = df.rename({"0": "2018", "1": "2019", "2": "2020", "3": "2021", "4": "2022"}, axis='columns')

###sutvarkome nereikalingus reikšmių viduje###
df['2018'] = df['2018'].str.replace(' ', '')
df['2019'] = df['2019'].str.replace(' ', '')
df['2020'] = df['2020'].str.replace(' ', '')
df['2021'] = df['2021'].str.replace(' ', '')
df['2022'] = df['2022'].str.replace(' ', '')

###pakeičiame stulpelių pavadinimus###
df.set_index('2018', inplace = True)

###išsaugome sutvarkytą duomenų lentelę###
df.to_csv("CSV/naujas.csv", index=True)



