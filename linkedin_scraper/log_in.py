# @Author : Yulia
# @File   : log_in.py
# @Time   : 2025/8/8 1:34

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pickle
import os

COOKIE_PATH = "linkedin_cookies.pkl"

def get_cookies():
    """
    Log in LinkedIn manually to save cookies to local storage
    """
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # optional
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-features=TranslateUI")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-domain-reliability")

    service = Service("./chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.linkedin.com")
    input("Please press enter in terminal to continue...")

    with open(COOKIE_PATH, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    print("✅ Cookies saved")
    driver.quit()


def log_in_with_cookies(driver):
    """
    Use saved cookies to achieve password-free access to specified pages.

    :parameter:
        driver: Selenium webdriver instance
        url: The URL of the page accessed after logging in, default is the LinkedIn homepage feed.
    """
    driver.get("https://www.linkedin.com")
    with open(COOKIE_PATH, "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            # Fix the sameSite attribute to prevent errors.
            if "sameSite" in cookie and cookie["sameSite"] == "None":
                cookie["sameSite"] = "Strict"
            driver.add_cookie(cookie)
    driver.get("https://www.linkedin.com/feed/")
