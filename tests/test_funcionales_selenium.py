import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_selenium_flow():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:5000/")

    # Función para ingresar datos y enviar
    def enviar_datos(nombre, peso):
        print(f"Enviando: {nombre}, {peso}")
        nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
        nombre_input.clear()
        nombre_input.send_keys(nombre)

        peso_input = driver.find_element(By.NAME, "peso")
        peso_input.clear()
        peso_input.send_keys(peso)

        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
        time.sleep(3)
        driver.refresh()  # Recarga la página para resetear el formulario
        time.sleep(3)

    enviar_datos("Usuario1", "100")
    enviar_datos("Usuario2", "100")
    enviar_datos("Usuario1", "90.5")
    enviar_datos("Usuario2", "105.5")

    driver.quit()
