from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_cart(login_in_driver):
        
        driver = login_in_driver
        
# Hacer click en "Agregar al carrito"
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#Tambien puedo usar esta para buscar el primer elemento con css_selector en vez del id si borrasen el mismo
        #driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
        #driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click() / este esta para ver que pasaba si agregaba mas de uno /
# Espera explícita: hasta que el carrito tenga al menos un elemento visible
        wait = WebDriverWait(driver, 5)  # espera hasta 5 segundos
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))

# Verificar que haya al menos un objeto en el carrito
        cart_item = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_item.text == "1", f"Se esperaba 1 producto, pero hay {cart_item.text}"


#driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

def test_cart(login_in_driver):
    try:
        driver = login_in_driver

        driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()

        titulo_producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert contador_carrito == "1", "No se ha agregado el producto al carrito"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        titulo_producto_carrito = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
        assert titulo_producto == titulo_producto_carrito, "El producto no coincide"

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()