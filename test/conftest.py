import  pytest
from selenium import webdriver
from pages.login_page import Loginpage



@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    Loginpage(driver).abrir_pagina().login_completo("standard_user","secret_sauce")
    return driver