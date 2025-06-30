import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get("http://localhost:5000/")

    # Enviar datos y verificar redirección (status 200)
    for nombre, peso in [("Usuario1", "80"), ("Usuario2", "90")]:
        nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
        nombre_input.clear()
        nombre_input.send_keys(nombre)

        peso_input = driver.find_element(By.NAME, "peso")
        peso_input.clear()
        peso_input.send_keys(peso)

        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

        # Esperar a que la página se recargue tras redireccionar (post-redirect-get)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        time.sleep(1)

    driver.quit()
