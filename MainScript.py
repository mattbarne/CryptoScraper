# Imported modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

try:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
except Exception as e:
    print("Error occurred:", e)

firefox_options = Options()
firefox_options.add_argument('--headless')



def button_engagement():
    driver.find_element(by=By.XPATH, )


def scrape_data():
    try:
        while True:
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="last-JWoJqCpY js-symbol-last"]')))

            element = driver.find_element(By.XPATH, '//span[@class="last-JWoJqCpY js-symbol-last"]')

            crypto_price = element.text.strip()

            sleep_duration = 0.2
            time.sleep(sleep_duration)

            return crypto_price
    except Exception as e:
        print("Error occurred:", e)


def close_browser():
    driver.quit()

