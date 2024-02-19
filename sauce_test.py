from selenium import webdriver
import pytest
from Pages.sauce_login import Login
from Pages.sauce_product import Production
from Pages.sauce_personal import My_personal
from Pages.sauce_result import Sum


def test_sauce():
    browser = webdriver.Chrome()
    log = Login(browser)
    prod = Production(browser)
    personal = My_personal(browser)
    result = Sum(browser)
    log.text("standard_user")
    log.password("secret_sauce")
    log.click()
    prod.product()
    personal.first_name("Александр")
    personal.last_name("Рубанов")
    personal.postal("196784")
    personal.click()
    total_price = result.buy()
    total = 'Total: $58.29'
    assert total == total_price
  


