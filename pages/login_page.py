from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class Loginpage:
    # url
    url="http//www.saucedemo.com/"

    _USER_IMPUT=(By.ID, "user-name")
    _PASS_INPUT=(By.ID, "password")
    _LOGIN_BUTTON=(By.ID, "login-button")

    def __init__(self,driver):
        self.driver = driver()
        self.wait = WebDriverWait(driver,10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def completar_user(self,usuario):
        input =self.wait.until(ES.visibility_of_element_located(self._USER_IMPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    def completar_pass(self,password):
        input =self.driver.find_element(self._PASS_INPUT)
        input.clear()
        input.send_keys(password)
        return self
    
    
    def hacer_clik_button(self):
        self.driver.find_element(self._LOGIN_BUTTON).CLIK()
        return self
    
    def login_completo(self,usuario,password):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_clik_button()
        return self
    
    def obtener_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-messenger- h3")))
        return div_error.text 