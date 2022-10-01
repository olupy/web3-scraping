import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Step 1: Create a session and load the page
PATH = 'C:/Users/biodun/downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(executable_path=PATH)
project_details = []
for i in range(81,101):
    if i == 1:
        driver.get("https://coincarp.com/fundraising")
    else:
        driver.get(f"https://coincarp.com/fundraising/pn_{i}.html")

    # Wait for the page to fully load
    driver.implicitly_wait(5)

    # Step 2: Parse HTML code and grab tables with Beautiful Soup
    soup = BeautifulSoup(driver.page_source, 'lxml')

    tables = soup.find_all('table')

    # Step 3: Read tables with Pandas read_html()
    dfs = pd.read_html(str(tables))
    df = pd.concat(dfs)
    df.to_csv(f'item{i}.csv')
          

driver.close()

