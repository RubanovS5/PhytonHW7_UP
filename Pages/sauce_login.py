from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def text(self,text):
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(text)
    def password(self,password):
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    def click(self):
        self.driver.find_element(By.XPATH,"//input[@id='login-button']").click()