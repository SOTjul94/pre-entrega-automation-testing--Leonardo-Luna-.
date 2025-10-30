from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.parametraze  ("standard_user", "secret_sauce"),(

    ("locked_out_user", "secret_sauce"),

    ("problem_user", "secret_sauce"),

    ("performance_glitch_user", "secret_sauce"),

def test_login():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        assert "/inventory.html" in driver.current_url, "No se redoirigio correctamente"
        print("Login exitoso y valido")
    except Exception as e:
        print(f"Error en test login: {e}")
        raise
    finally:
        driver.quit()