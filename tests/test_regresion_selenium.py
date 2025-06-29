from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_registro_usuario():
    """Prueba que el registro básico funcione"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    
    try:
        # 1. Llenar formulario
        driver.find_element(By.NAME, "nombre").send_keys("Usuario1")
        driver.find_element(By.NAME, "peso").send_keys("200")
        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
        
        # Esperar a que la página se actualice
        time.sleep(2)
        
        # 2. Verificar que se registró (ajustado al formato real)
        assert "Usuario1: 200.0 kg" in driver.page_source
        print("Prueba de regresion exitosa")
        
    except Exception as e:
        print(f"Error en prueba de regresion: {str(e)}")
        print(f"Contenido actual de la página: {driver.page_source}")
        raise
    finally:
        driver.quit()

def test_actualizacion_peso():
    """Prueba que se pueda actualizar el peso"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    
    try:
        # 1. Actualizar peso de Usuario1
        driver.find_element(By.NAME, "nombre").send_keys("Usuario1")
        driver.find_element(By.NAME, "peso").send_keys("99.5")
        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
        
        # Esperar a que la página se actualice
        time.sleep(2)
        
        # 2. Verificar cambio (ajustado al formato real)
        assert "Usuario1: 99.5 kg" in driver.page_source
        print("Prueba de regresion exitosa")
        
    except Exception as e:
        print(f"Error en prueba de regresion: {str(e)}")
        print(f"Contenido actual de la página: {driver.page_source}")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_registro_usuario()
    test_actualizacion_peso()
    print("Pruebas finalizadas con exito")