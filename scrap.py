from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=4b9681f1-aa53-47ad-832b-ef4b56eb3a22#')

wait = WebDriverWait(driver, 10)  # wait for a maximum of 10 seconds
table = wait.until(EC.presence_of_element_located((By.ID, 'table')))

rows = table.find_elements(By.TAG_NAME, 'tr')

data = []
for row in rows:

    cols = row.find_elements(By.TAG_NAME, 'td')
    col_data = []
    for col in cols:
        col_data.append(col.text)
    data.append(col_data)

driver.quit()
if data:

    df = pd.DataFrame(data)

    csv_file_path = 'CSV/scraped_data.csv'

    df.to_csv(csv_file_path, index=False)

    # print(f'Data written to {csv_file_path}')
else:
    print("No data scraped.")




