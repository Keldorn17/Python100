from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
import random
import time
from dotenv import load_dotenv
import os

load_dotenv(".env")


def human_like_typing(element: WebElement, text: str) -> None:
    for char in text:
        element.send_keys(char)
        time.sleep(random.randint(5, 10) / 100)


def login(driver: WebDriver) -> None:
    accept_cookies(driver)
    email = driver.find_element(By.ID, value="username")
    human_like_typing(email, os.getenv("EMAIL"))
    password = driver.find_element(By.ID, value="password")
    human_like_typing(password, os.getenv("PASSWORD"))
    sign_in = driver.find_element(By.CSS_SELECTOR, value='.login__form_action_container button')
    sign_in.click()


def accept_cookies(driver: WebDriver) -> None:
    time.sleep(2)
    try:
        accept = driver.find_element(By.CSS_SELECTOR, value="[action-type=ACCEPT]")
        accept.click()
    except NoSuchElementException:
        print("NoSuchElementException")


def search_for_job(driver: WebDriver, job_text: str) -> None:
    time.sleep(2)
    search_icon = driver.find_element(By.CSS_SELECTOR, value="#global-nav-search button")
    search_icon.click()
    search = driver.find_element(By.CSS_SELECTOR, value="#global-nav-search input")
    human_like_typing(search, job_text)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, value="See all job results in United Kingdom").click()


def main() -> None:
    website: str = "https://www.linkedin.com/login/en"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(website)

    login(driver)
    search_for_job(driver, "python developer")


if __name__ == '__main__':
    main()
