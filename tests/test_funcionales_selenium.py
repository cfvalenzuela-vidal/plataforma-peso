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

    # Función helper para ingresar datos
    def ingresar_peso(nombre, peso):
        wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).clear()
        driver.find_element(By.NAME, "nombre").send_keys(nombre)
        driver.find_element(By.NAME, "peso").clear()
        driver.find_element(By.NAME, "peso").send_keys(str(peso))
        driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

        # Esperamos que aparezca el resultado actualizado, asumiendo que
        # aparece en un elemento con id 'resultado' (ajusta si tu app usa otro selector)
        wait.until(EC.text_to_be_present_in_element((By.ID, "resultado"), f"{nombre}: {peso}"))

        # Obtener el texto para la validación
        texto = driver.find_element(By.ID, "resultado").text
        return texto

    # Usuario1 - 100kg
    texto1 = ingresar_peso("Usuario1", 100)
    assert f"Usuario1: 100" in texto1

    # Usuario2 - 100kg
    texto2 = ingresar_peso("Usuario2", 100)
    assert f"Usuario2: 100" in texto2

    # Usuario1 baja a 90.5kg
    texto3 = ingresar_peso("Usuario1", 90.5)
    assert f"Usuario1: 90.5" in texto3

    # Usuario2 sube a 105.5kg
    texto4 = ingresar_peso("Usuario2", 105.5)
    assert f"Usuario2: 105.5" in texto4


