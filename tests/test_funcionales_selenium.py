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

    usuarios_a_enviar = [
        ("Usuario1_1", "100"),
        ("Usuario2_2", "100"),
        ("Usuario1_3", "90.5"),
        ("Usuario2_4", "105.5"),
    ]

    for nombre, peso in usuarios_a_enviar:
        driver.get("http://localhost:5000/")
        nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
        nombre_input.clear()
        nombre_input.send_keys(nombre)

        peso_input = driver.find_element(By.NAME, "peso")
        peso_input.clear()
        peso_input.send_keys(peso)

        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
        time.sleep(3)

        # Verificamos que el último usuario mostrado sea el esperado
        usuarios_texts = driver.find_elements(By.CSS_SELECTOR, "body p")
        if usuarios_texts:
            ultimo_usuario = usuarios_texts[-1].text
            print(f"Último usuario mostrado: {ultimo_usuario}")
            assert nombre in ultimo_usuario and peso in ultimo_usuario

    driver.quit()
