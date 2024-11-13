from selenium import webdriver
from selenium.webdriver.common.by import By


def main() -> None:
    # Keep Chrome browser open after program finishes
    chrome_options: webdriver.ChromeOptions = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver: webdriver.Chrome = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.python.org/")

    # # https://www.amazon.com/
    # price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    # price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    # print(f"The price is {price_dollar.text}.{price_cents.text}")

    # # https://www.python.org/
    # search_bar = driver.find_element(By.NAME, value="q")
    # print(search_bar.get_attribute("placeholder"))
    #
    # button = driver.find_element(By.ID, value="submit")
    # print(button.size)
    #
    # documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    # print(documentation_link.text)
    #
    # bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    # print(bug_link.text)

    # menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
    # upcoming_time = menu.find_elements(By.CSS_SELECTOR, value="time")
    # upcoming_name = menu.find_elements(By.CSS_SELECTOR, value="a")
    #
    # time_list: list[str] = [time.get_attribute("datetime").split("T")[0] for time in upcoming_time]
    # a_tag_list: list[str] = [a_tag.text for a_tag in upcoming_name]

    event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
    time_list: list[str] = [time.get_attribute("datetime").split("T")[0] for time in event_time]

    event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")
    a_tag_list: list[str] = [a_tag.text for a_tag in event_name]

    upcoming_events: dict = {i: {"time": time_list[i], "name": a_tag_list[i]} for i in range(len(time_list))}

    print(upcoming_events)

    # driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
