import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 10)
    return driver


def search_google(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        box.send_keys(query)
        button = driver.wait.until(EC.element_to_be_clickable((By.NAME, "btnG")))
        button.click()
    except TimeoutException:
        print("Search field or Button not found on google.com")

if __name__ == "__main__":
    driver = init_driver()
    search_google(driver, "Python")
    time.sleep(5)
    driver.quit()