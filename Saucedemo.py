from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time

def actionLogin(driver):
    #setUp
    username = driver.find_element(By.NAME, "user-name")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.NAME, "login-button")
   
    #Call
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    driver.get_screenshot_as_file("LoginPage.png")
    btnLogin.click()
    time.sleep(10)

def actionLogout(driver):
    #setUp
    burgerMenu = driver.find_element(By.ID, "react-burger-menu-btn")
    burgerMenu.click()
    time.sleep(10)
    driver.get_screenshot_as_file("Menu Burger.png")
    btnLogout = driver.find_element(By.ID, "logout_sidebar_link")
    btnLogout.click()
    time.sleep(10)

def actionLoginLockedOut(driver):
    #setUp
    username = driver.find_element(By.NAME, "user-name")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.NAME, "login-button")
   
    #Call
    username.send_keys("locked_out_user")
    password.send_keys("secret_sauce")
    driver.get_screenshot_as_file("LoginPageLockedOut.png")
    btnLogin.click()
    time.sleep(10)


