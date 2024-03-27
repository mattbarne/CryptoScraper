from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

# Fetches Geckodriver
try:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
except Exception as driver_error:
    print("Error occurred:", driver_error)

# Firefox optional arguments
firefox_options = Options()
firefox_options.add_argument('--headless')


# TODO: Add macro engagement for buttons on trading site
def button_engagement():
    driver.find_element(by=By.XPATH, )


# Updates URL
url = ''
coin_choice = ''


def update_url(crypto):
    global url, coin_choice
    if crypto == "Bitcoin":
        coin_choice = 'Bitcoin'
        url = "https://www.tradingview.com/symbols/BTCUSD/?exchange=BINANCE"
    elif crypto == "Ethereum":
        coin_choice = 'Ethereum'
        url = "https://www.tradingview.com/symbols/ETHUSD/?exchange=CRYPTO"
    elif crypto == "Lunc":
        coin_choice = 'Lunc'
        url = "https://www.tradingview.com/symbols/LUNCUSDT.P/?exchange=MEXC"

    driver.refresh()
    driver.get(url)


# Fetching the price class from URL
def scrape_data():
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//span[@class="last-JWoJqCpY js-symbol-last"]')))

        element = driver.find_element(By.XPATH, '//span[@class="last-JWoJqCpY js-symbol-last"]')

        crypto_price = element.text.strip()

        return crypto_price
    except Exception as scrape_error:
        print("Error occurred:", scrape_error)
