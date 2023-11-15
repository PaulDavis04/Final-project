import psycopg2
from psycopg2 import sql
import pandas as pd
df = pd.read_csv(r"CSV/skreipinti_pavadinimai.csv.")
df = df.rename({"0": "Ligos", "1": "Tuscia"}, axis='columns')
df.set_index('Ligos', inplace = True)
df.to_csv("CSV/pavadinimai_naujas.csv", index=True)

df1 = pd.read_csv("CSV/pavadinimai_naujas.csv")
df2 = pd.read_csv("CSV/naujas.csv")
df3 = pd.concat([df1, df2], axis=1)


df3['Ligos'] = df3['Ligos'].replace(['Vyrai ir moterys', 'Vyrai', 'Moterys'], ['Tam tikros infekcinės ir parazitų sukeliamos ligos',
                                                                            'Tam tikros infekcinės ir parazitų sukeliamos ligos',
                                                                            'Tam tikros infekcinės ir parazitų '
                                                                            'sukeliamos ligos'])
df3.set_index('Ligos', inplace = True)
df3.drop(df.iloc[:, 1:2], inplace=True, axis=1)
print(df3)
df3.to_csv("CSV/bendra_lentele.csv", index=True)









