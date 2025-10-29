


from selenium.webdriver.common.by import By
from  selenium import webdriver
import pytest
import time
import driver # type: ignore

def test_login_validation(login_in_driver):
    driver = login_in_driver
    driver.find_element(By.CSS_SELECTOR,)

try:
    assert "/nventory.html" in driver.current_url,"no se rediigio al inventario"




except Exception as e:
    print(f"error en test login{e}")
    raise 
finally:
    driver.quit()