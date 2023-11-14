import psycopg2
from psycopg2 import sql
import pandas as pd

df = pd.read_csv(r"skreipinti_pavadinimai.csv.")
df = df.rename({"0": "Ligos", "1": "Tuscia"}, axis='columns')
df.set_index('Ligos', inplace = True)
df.to_csv("pavadinimai_naujas.csv", index=True)

df1 = pd.read_csv("pavadinimai_naujas.csv")
df2 = pd.read_csv("naujas.csv")
df3 = pd.concat([df1, df2], axis=1)
print(df3)

df3.to_csv("bendra_lentele.csv", index=True)

# df = df.rename({"Vyrai ir moterys": "Tam tikros infekcinės ir parazitų sukeliamos ligos"}, axis='columns')
# df['C2'] = df['C2'].replace(['Vyrai ir moterys'], 'Tam tikros infekcinės ir parazitų sukeliamos ligos')
# df.to_csv("skreipinti_pavadinimai_naujas.csv", index=True)
