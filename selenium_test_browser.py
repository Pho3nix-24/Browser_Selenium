import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Configurar el WebDriver Firefox con opciones avanzadas
service = Service(GeckoDriverManager().install())
options = webdriver.FirefoxOptions()

# User-Agent personalizado para evitar detección de Selenium
options.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Iniciar el navegador
browser = webdriver.Firefox(service=service, options=options)

# Modificar WebDriver para evitar detección
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Abrir Google
browser.get("https://www.google.com")

# Esperar de forma aleatoria antes de interactuar
time.sleep(random.uniform(2, 5))

# Aceptamos las cookies (si aparecen)
try:
    accept_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'L2AGLb'))
    )
    accept_button.click()
except Exception as e:
    print(f"No se encontró el botón de cookies o ya fue aceptado: {e}")

# Encontrar el cuadro de búsqueda
search_box = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

# Simular movimiento del mouse antes de escribir
action = ActionChains(browser)
action.move_to_element(search_box).perform()

# Escribir la búsqueda con pausas entre letras (emulación humana)
query = "Chema Alonso"
for letter in query:
    search_box.send_keys(letter)
    time.sleep(random.uniform(0.1, 0.3))  # Pausa aleatoria entre teclas

# Presionar Enter
search_box.send_keys(Keys.ENTER)

# Esperar a que los resultados carguen
time.sleep(random.uniform(4, 7))

# Extraer los resultados de búsqueda
results = browser.find_elements(By.CSS_SELECTOR, 'div.g')

for result in results:
    try:
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        description = result.find_element(By.CSS_SELECTOR, 'div.VwiC3b').text  # Corrección de clase
        
        print(f"Titulo: {title}\nEnlace: {link}\nDescripción: {description}\n")
    
    except Exception:
        print("Un elemento no pudo ser extraído")
        continue

# Cerrar el navegador
browser.quit()
