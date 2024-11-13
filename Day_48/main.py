from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main() -> None:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    driver.find_element(By.CSS_SELECTOR, value=".fc-button-label").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, value="#prompt #langSelect-EN").click()
    time.sleep(5)
    cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
    while True:
        cookie.click()
        cookies_count = driver.find_element(By.CSS_SELECTOR, value="#cookies").text.split(" ")[0]
        products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked")
        cookie_prices = [prod.find_element(By.CSS_SELECTOR, value=".price").text for prod in products]
        if cookie_prices:
            max_price: int = int(cookie_prices[0])
            max_index: int = 0
            for index, i in enumerate(cookie_prices):
                if i != '' and int(i.split(" ")[0].replace(",", "")) > max_price:
                    max_price = int(i.split(" ")[0].replace(",", ""))
                    max_index = index
            cookie_to_buy_price: int = int(cookie_prices[max_index].split(" ")[0].replace(",", ""))
            if cookie_to_buy_price < int(cookies_count):
                products[max_index].click()


if __name__ == '__main__':
    main()
