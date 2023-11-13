import requests
import json
import psycopg2
import pandas as pd
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    'value': 'application/json, text/plain, */*',
    'accept': 'application/json, text/plain, */*',
    'cookie': '_ga=GA1.2.1272715160.1699462284; _gid=GA1.2.1647336826.1699462284; _ga_E8WJ6X0RYN=GS1.2.1699471615.3.0.1699471615.60.0.0; _ga_162SQ74LLR=GS1.2.1699471697.2.1.1699471698.0.0.0'
}
url = "https://osp.stat.gov.lt/analysis-portlet/services/api/v1/data/generate/table/hash/4b9681f1-aa53-47ad-832b-ef4b56eb3a22"
page = requests.get(url, headers=headers)
print(data)
data = page.json()

df = pd.DataFrame(data)
print(df)
df.to_csv("Ligos_redaguotas2.csv", index=True)