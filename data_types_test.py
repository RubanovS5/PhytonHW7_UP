from selenium import webdriver
import pytest
from Pages.find_element_input import Input_field


def test_types():
    browser = webdriver.Chrome()
    data_types = Input_field(browser)
    data_types.first_name("Иван")
    data_types.last_name("Петров")
    data_types.address("Ленина, 55-3")
    data_types.zip_code("")
    data_types.city("Москва")
    data_types.country("Россия")
    data_types.mail("test@skypro.com")
    data_types.phone("+7985899998787")
    data_types.job("QA")
    data_types.company("SkyPro")
    data_types.button()
    green_rgba = "rgba(209, 231, 221, 1)"
    red_rgba = "rgba(248, 215, 218, 1)"
    assert data_types.colour_first_name() == green_rgba
    assert data_types.colour_last_name() == green_rgba
    assert data_types.colour_address() == green_rgba
    assert data_types.colour_zip_code() == red_rgba
    assert data_types.colour_city() == green_rgba
    assert data_types.colour_country() == green_rgba
    assert data_types.colour_mail() == green_rgba
    assert data_types.colour_phone() == green_rgba
    assert data_types.colour_job() == green_rgba
    assert data_types.colour_company() == green_rgba

    