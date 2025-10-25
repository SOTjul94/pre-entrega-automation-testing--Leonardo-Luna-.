from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
   
    
    driver = webdriver.Chrome()
   #espera explicita
    wait = WebDriverWait(driver,10)
   
    #espera implicita
      
    driver.get("http://www.saucedemo.com/")
    
    driver.implicitly_wait(5)


#time.sleep(2)

#localizacion e iteracion de elementos
        
    wait.until(EC.presence_of_all_elements_located((By.ID,"user-name")))
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

#time.sleep(2)

test_login()