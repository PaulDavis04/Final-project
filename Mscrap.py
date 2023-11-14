import pandas as pd
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}

url = "https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=4b9681f1-aa53-47ad-832b-ef4b56eb3a22#/"

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
    try:
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

    except KeyError:
            continue

    print(liga, fdata1, fdata2, fdata3, fdata4, fdata5)

data = {
    # "Lytis": [lytis],
    "Liga": list2,
    "2018": list3,
    "2019": list4,
    "2020": list5,
    "2021": list6,
    "2022": list7
    }

df = pd.DataFrame(data)
print(df)

# df[""] = df[""].str.split(pat='M', n=0, expand=True)[0]
# df[""] = df[""].str.split(pat='M', n=0, expand=True)[1]
# df.drop(columns=[''], inplace=True)
# df = df.reindex(columns=['', 'Month', '', ''])
# print(df)
# df.to_csv("LIGOS.csv", index=True)