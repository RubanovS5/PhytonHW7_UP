from Pages.numbers_calculator import Numbers
from selenium import webdriver
import pytest


def test_form():
    browser = webdriver.Chrome()
    calculator = Numbers(browser)
    calculator.id_delay('45')
    calculator.actions_calculator()
    calculator.action_result()
    to_be = calculator.action_result()
    as_is = calculator.search_answers()
    assert as_is == to_be


