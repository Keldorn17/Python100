from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeed:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.__driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        website: str = "https://www.speedtest.net/"
        self.__driver.get(website)

        # Accept term and services
        time.sleep(1)
        accept = self.__driver.find_element(By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")
        accept.click()

        # Start Testing
        time.sleep(1)
        start_btn = self.__driver.find_element(By.CSS_SELECTOR, value=".start-text")
        start_btn.click()

        # Read Latency, Up and Down data
        time.sleep(40)
        ping = self.__driver.find_element(By.CSS_SELECTOR,
                                          value=".result-data-value.ping-speed")
        download = self.__driver.find_element(By.CSS_SELECTOR,
                                          value=".result-data-large.number.result-data-value.download-speed")
        upload = self.__driver.find_element(By.CSS_SELECTOR,
                                          value=".result-data-large.number.result-data-value.upload-speed")

        # Print date about internet speed to the console.
        print(f"Ping: {ping.text}\nDownload: {download.text}\nUpload: {upload.text}")

        # Close browser since it's not needed anymore
        self.__driver.close()
