# @Author : Yulia
# @File   : set_up.py
# @Time   : 2025/8/7 23:53

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def create_driver(headless=False, driver_path=None):
    """

    Create Chrome driver and explicit wait object
    Parameters:
        headless (bool): Whether to enable headless mode, default is False.
        driver_path (str or None): ChromeDriver path, default is None to let Selenium auto-discover.
    Returns:
        driver (WebDriver): Chrome WebDriver instance
        wait (WebDriverWait): Explicit wait object, default timeout is 10 seconds.

    """
    options = Options()
    if headless:
        options.add_argument("--headless=new")  # New version headless mode, Chrome 109+
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=TranslateUI")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-domain-reliability")
    options.add_argument("--lang=en-US")
    options.add_argument("--page-load-timeout=60")

    if driver_path:
        service = Service(driver_path)
    else:
        service = Service()  # Automatically find chromedriver

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    return driver, wait
