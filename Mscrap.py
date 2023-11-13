import pandas as pd
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}

url = "https://osp.stat.gov.lt/analysis-portlet/services/api/v1/data/generate/table/hash/4b9681f1-aa53-47ad-832b-ef4b56eb3a22"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    json_data = response.json()
    ilgis = len(response.json()["data"]['itemMatrix'])
    # print(ilgis)
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

for i in range(ilgis):
    # lytis = response.json()["data"]['sidebar'][i]['name']
    liga = response.json()["data"]['sidebar'][0]['captions'][i]['name']
    data1 = response.json()["data"]['itemMatrix'][i][0]['value']
    data2 = response.json()["data"]['itemMatrix'][i][1]['value']
    data3 = response.json()["data"]['itemMatrix'][i][2]['value']
    data4 = response.json()["data"]['itemMatrix'][i][3]['value']
    data5 = response.json()["data"]['itemMatrix'][i][4]['value']
    fdata1 = data1.replace(u'\xa0', '')
    fdata2 = data2.replace(u'\xa0', '')
    fdata3 = data3.replace(u'\xa0', '')
    fdata4 = data4.replace(u'\xa0', '')
    fdata5 = data5.replace(u'\xa0', '')
    # list1.append(lytis)
    list2.append(liga)
    list3.append(fdata1)
    list4.append(fdata2)
    list5.append(fdata3)
    list6.append(fdata4)
    list7.append(fdata5)

    print(liga, fdata1, fdata2, fdata3, fdata4, fdata5)
else:
    print('Error while fetching JSON:', response.status_code)

data = {
    # "Lytis": [lytis],
    "Liga": [liga],
    "2018": [fdata1],
    "2019": [fdata2],
    "2020": [fdata3],
    "2021": [fdata4],
    "2022": [fdata5]
    }

df = pd.DataFrame(data)
print(df)

# df.to_csv("Bandymas.csv", index=True)
# print(df)
# #