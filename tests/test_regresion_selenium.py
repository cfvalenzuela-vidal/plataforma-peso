import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,1024")
    driver = webdriver.Chrome(options=options)
    yield driver
    os.makedirs("tests", exist_ok=True)
    driver.save_screenshot("tests/screenshot.png")
    driver.quit()

def test_flujo_completo(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:5000/")

    def ingresar_peso(nombre, peso):
        wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).clear()
        driver.find_element(By.NAME, "nombre").send_keys(nombre)
        driver.find_element(By.NAME, "peso").clear()
        driver.find_element(By.NAME, "peso").send_keys(str(peso))
        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

        peso_str = f"{peso:.1f}"  # Formato con un decimal
        esperado = f"{nombre}: {peso_str} kg"

        wait.until(lambda d: esperado in d.find_element(By.TAG_NAME, "body").text)
        texto = driver.find_element(By.TAG_NAME, "body").text
        return texto

    texto1 = ingresar_peso("Usuario1", 100)
    assert "Usuario1: 100.0 kg" in texto1

    texto2 = ingresar_peso("Usuario2", 100)
    assert "Usuario2: 100.0 kg" in texto2

    texto3 = ingresar_peso("Usuario1", 90.5)
    assert "Usuario1: 90.5 kg" in texto3

    texto4 = ingresar_peso("Usuario2", 105.5)
    assert "Usuario2: 105.5 kg" in texto4
