import psycopg2
from psycopg2 import sql
import pandas as pd

df = pd.read_csv(r"skreipinti_pavadinimai.csv.")

df.to_csv("pavadinimai_naujas.csv", index=True)

# df = df.rename({"Vyrai ir moterys": "Tam tikros infekcinės ir parazitų sukeliamos ligos"}, axis='columns')
# df['C2'] = df['C2'].replace(['Vyrai ir moterys'], 'Tam tikros infekcinės ir parazitų sukeliamos ligos')
df.to_csv("skreipinti_pavadinimai_naujas.csv", index=True)