from bdb import effective
import Saucedemo
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://www.saucedemo.com/ ")
    time.sleep(10)
    Saucedemo.actionLogin(driver)
    Saucedemo.actionAddCart(driver)
    Saucedemo.actionCheckout(driver)
    Saucedemo.actionLogout(driver)
    Saucedemo.actionLoginLockedOut(driver)



if __name__ == '__main__':
    main()