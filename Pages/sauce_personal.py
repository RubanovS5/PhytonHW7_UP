from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class My_personal:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def first_name(self,f_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'first-name']"))).send_keys(f_name)

    def last_name (self,l_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'last-name']"))).send_keys(l_name)

    def postal(self,postal):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'postal-code']"))).send_keys(postal)

    def click(self):
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()