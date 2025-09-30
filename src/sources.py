import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_premarket_movers(max_pages=5):
    url = "https://stockanalysis.com/markets/premarket/gainers/"
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    wait = WebDriverWait(driver, 10)
    tickers = set()
    try:
        driver.get(url)
        for _ in range(max_pages):
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody")))
            rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            for row in rows:
                tds = row.find_elements(By.TAG_NAME, "td")
                if tds:
                    t = tds[0].text.strip()
                    if 1 <= len(t) <= 5 and t.isupper():
                        tickers.add(t)
            try:
                btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Next")))
                btn.click()
                time.sleep(1.5)
            except:
                break
    finally:
        driver.quit()
    return sorted(tickers)
