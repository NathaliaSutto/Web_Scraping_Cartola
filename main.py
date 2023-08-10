import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = 'https://www.cartolafcbrasil.com.br/scouts'


def clubes(team):

    driver.find_element(By.XPATH,"//select[@name='ctl00$cphMainContent$drpClubes']/option[text()='" + team + "']").click()
    time.sleep(20)

    driver.find_element(By.XPATH,"//select[@name='ctl00$cphMainContent$drpStatus']/option[text()='[TODOS]']").click()
    time.sleep(20)

    button = driver.find_element(By.XPATH, '//*[@id="ctl00_cphMainContent_btnFiltrar"]')
    driver.execute_script("arguments[0].click();", button)
    time.sleep(20)

    table_element = driver.find_element(By.XPATH, '//*[@id="ctl00_cphMainContent_gvList"]')
    table_html = table_element.get_attribute('outerHTML')

    df = pd.read_html(str(table_html))
    df = df[0]
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df.clube = team
    df.preço = df.preço / 100
    df.média = df.média / 100
    df.variação = df.variação / 100

    return df.to_csv('/Users/nathaliasutto/PycharmProjects/Scraping_CARTOLA_FC_PLUS/CARTOLA_FC.csv',
                     encoding='utf-8', sep=';')

option = Options()
option.add_argument("--headless=new")
driver = webdriver.Chrome(options=option)

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.implicitly_wait(60)  # in seconds

# insira aqui o nome do clube para extrair dados:
print(clubes('Flamengo'))

driver.quit()



