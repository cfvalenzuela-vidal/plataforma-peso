from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin UI
chrome_options.add_argument("--no-sandbox")  # Recomendado en entornos CI
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas con /dev/shm
chrome_options.add_argument("--disable-gpu")  # Opcional, para evitar errores gráficos

# Si tienes chromedriver en PATH, no es necesario poner la ruta explícita.
service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)  # Espera máxima de 10 segundos
driver.get("http://localhost:5000/")

# Usuario1 - 100kg
wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).send_keys("Usuario1")
driver.find_element(By.NAME, "peso").send_keys("100")
driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

# Usuario2 - 100kg
wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).send_keys("Usuario2")
driver.find_element(By.NAME, "peso").send_keys("100")
driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

# Usuario1 bajo a 90.5kg
wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).send_keys("Usuario1")
driver.find_element(By.NAME, "peso").send_keys("90.5")
driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

# Usuario2 subio a 105.5kg
wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).send_keys("Usuario2")
driver.find_element(By.NAME, "peso").send_keys("105.5")
driver.find_element(By.XPATH, "//button[text()='Enviar']").click()

driver.quit()
