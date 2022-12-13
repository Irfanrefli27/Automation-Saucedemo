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

def actionAddCart(driver):
    #setUp
    addCart1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    addCart2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    addCart3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")

    #Call
    addCart1.click()
    time.sleep(2)
    driver.get_screenshot_as_file("add-to-cart-sauce-labs-backpack.png")
    addCart2.click()
    time.sleep(2)
    driver.get_screenshot_as_file("add-to-cart-sauce-labs-bike-light.png")
    addCart3.click()

def actionCheckout(driver):
    #setUp
    btnCart = driver.find_element(By.ID, "shopping_cart_container")
    btnCart.click()
    time.sleep(5)
    driver.get_screenshot_as_file("View Cart.png")
    btnCheckout = driver.find_element(By.ID, "btn btn_action btn_medium checkout_button")
    btnCheckout.click()
    firstName = driver.find_element(By.ID, "first-name")
    lastName = driver.find_element(By.ID, "last-name")
    zipCode = driver.find_element(By.ID, "postal-code")
    btnContinue = driver.find_element(By.ID, "continue")

    #call
    firstName.send_keys("aaaaa")
    lastName.send_keys("bbbbb")
    zipCode.send_keys("12345")
    driver.get_screenshot_as_file("Your Information.png")
    time.sleep(10)
    btnContinue.click()
    time.sleep(10)
    driver.get_screenshot_as_file("OVERVIEW.png")
    btnFinish = driver.find_element(By.ID, "finish")
    btnFinish.click()
    time.sleep(10)
    driver.get_screenshot_as_file("COMPLETE CHECKOUT.png")

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


