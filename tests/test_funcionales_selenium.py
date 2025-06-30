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

    # Usuario1 - 100kg
    nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
    nombre_input.clear()
    nombre_input.send_keys("Usuario1")

    peso_input = driver.find_element(By.NAME, "peso")
    peso_input.clear()
    peso_input.send_keys("100")

    driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
    time.sleep(5)

    # Usuario2 - 100kg
    nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
    nombre_input.clear()
    nombre_input.send_keys("Usuario2")

    peso_input = driver.find_element(By.NAME, "peso")
    peso_input.clear()
    peso_input.send_keys("100")

    driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
    time.sleep(5)

    # Usuario1 bajo a 90.5kg
    nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
    nombre_input.clear()
    nombre_input.send_keys("Usuario1")

    peso_input = driver.find_element(By.NAME, "peso")
    peso_input.clear()
    peso_input.send_keys("90.5")

    driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
    time.sleep(5)

    # Usuario2 subio a 105.5kg
    nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
    nombre_input.clear()
    nombre_input.send_keys("Usuario2")

    peso_input = driver.find_element(By.NAME, "peso")
    peso_input.clear()
    peso_input.send_keys("105.5")

    driver.find_element(By.XPATH, "//button[text()='Enviar']").click()
    time.sleep(5)

    driver.quit()
