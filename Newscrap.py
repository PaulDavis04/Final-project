import requests

url = "https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=810a4f0b-7a3b-4f23-b843-73236956dba6"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()

    print(json_data)
else:
    print('Error while fetching JSON:', response.status_code)