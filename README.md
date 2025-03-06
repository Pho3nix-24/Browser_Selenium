Browser_Selenium

Este proyecto utiliza Selenium en Python para automatizar búsquedas en Google, emulando el comportamiento humano. El código abre Google, acepta las cookies, realiza una búsqueda y extrae los enlaces y descripciones de los primeros resultados.

📌 Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

Python 3.x
Selenium
WebDriver para tu navegador (GeckoDriver para Firefox o ChromeDriver para Chrome)
WebDriver Manager

Puedes instalarlas con:
pip install selenium webdriver-manager

🚀 Instalación y Uso

1.Clona el repositorio
git clone https://github.com/Pho3nix-24/Browser_Selenium.git
cd Browser_Selenium

2.Ejecuta el script
python selenium_test_browser.py

🔍 Funcionamiento del Script

1.Inicia un navegador (Firefox o Chrome).
2.Abre Google.
3.Acepta el aviso de cookies.
4.Introduce el término de búsqueda de tu agrado, en este caso se uso: "Chema Alonso".
5.Extrae y muestra en la terminal los títulos, enlaces y descripciones de los primeros resultados.
6.Cierra el navegador.

🛠 Personalización

Puedes modificar el término de búsqueda cambiando esta línea en el código:
search_box.send_keys('Tu búsqueda aquí' + Keys.ENTER)

📝 Notas

Si Google detecta automatización, puede pedir un CAPTCHA. Para evitar bloqueos, puedes añadir tiempos de espera más largos con time.sleep(). También puedes configurar un User-Agent diferente para hacer que la solicitud parezca más humana.

📜 Licencia

Este proyecto es de uso libre para fines educativos y de experimentación en ciberseguridad.
