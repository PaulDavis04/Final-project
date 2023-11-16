from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
###sukeliame selenium, bibliotekas duomenu surinkimui is tinklalapio.
###susikeliame chrome valdiklius duomenu navigavimui tinklalapyje
### su Time turesime galimybe koreguoti valdikliams reikalinga laika duomenu surinkimui bei apdorojimui
### pandas naudosime surinktiems duomenims saugoti
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=4b9681f1-aa53-47ad-832b-ef4b56eb3a22#')
driver.maximize_window()
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

wait = WebDriverWait(driver, 10)

table = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'fluid-table-sidebar')))

rows = table.find_elements(By.TAG_NAME, "tr")

data = []
for row in rows:

    cols = row.find_elements(By.TAG_NAME, "td")
    col_data = []
    for col in cols:
        col_data.append(col.text)
    data.append(col_data)
print(data)
driver.quit()

###išsaugome surinktus duomenis###
if data:

    df = pd.DataFrame(data)

    csv_file_path = 'CSV/skreipinti_pavadinimai.csv'

    df.to_csv(csv_file_path)

    print(f'Data written to {csv_file_path}')
else:
    print("No data scraped.")
