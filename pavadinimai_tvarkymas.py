import pandas as pd

###nuskaitome išscrapintų pavadinimų failą, pervadiname stulpelius,
##panaikiname indekso stulpelį ir atspausdiname naują lentelę###
df = pd.read_csv(r"CSV/skreipinti_pavadinimai.csv.")
df = df.rename({"0": "Ligos", "1": "Tuscia"}, axis='columns')
df.set_index('Ligos', inplace=True)
df.to_csv("CSV/pavadinimai_naujas.csv", index=True)

###nuskaitome pavadinimų ir reikšmių lenteles, jas apjungiame į vieną, pakeičiame kelių reikšmių pavadinimus###
df1 = pd.read_csv("CSV/pavadinimai_naujas.csv")
df2 = pd.read_csv("CSV/naujas.csv")
df3 = pd.concat([df1, df2], axis=1)
df3['Ligos'] = df3['Ligos'].replace(['Vyrai ir moterys', 'Vyrai', 'Moterys'],
                                    ['Tam tikros infekcinės ir parazitų sukeliamos ligos',
                                    'Tam tikros infekcinės ir parazitų sukeliamos ligos',
                                    'Tam tikros infekcinės ir parazitų'
                                    'sukeliamos ligos'])

###pašaliname indeksų stulpelį, taip pat, kitus nereikalingus stulpelius ir atspausdiname tvarkingą lentelę###
df3.set_index('Ligos', inplace=True)
df3.drop(df.iloc[:, 1:2], inplace=True, axis=1)
print(df3)
df3.to_csv("CSV/bendra_lentele.csv", index=True)
