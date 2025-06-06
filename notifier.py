from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import time


def send_whatsapp_alert(message, contact_name="Yo"):
    options = Options()

    options.add_argument("--user-data-dir=C:\\whatsapp_profile")
    options.add_argument("--profile-directory=Default")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--lang=es")

    # ⚠️ NO usar headless si estás probando visualmente
    # options.add_argument("--headless")

    print("🚀 Iniciando navegador con perfil de usuario...")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    # Esto realiza la apertura de whatsapp en tu navegador
    # luego activa el headless una vez realizado por primera vez el script
    try:
        driver.get("https://web.whatsapp.com")
        print("⌛ Esperando carga de sesión (10s)...")
        time.sleep(10)

        search_box = driver.find_element(
            By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'
        )
        search_box.click()
        search_box.send_keys(contact_name)
        time.sleep(2)

        chat = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
        chat.click()
        time.sleep(2)

        message_box = driver.find_element(
            By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'
        )

        # Usar portapapeles para pegar texto con saltos de línea
        pyperclip.copy(message)
        message_box.click()
        time.sleep(2)
        message_box.send_keys(Keys.CONTROL, "v")  # CTRL + V para pegar todo el mensaje
        time.sleep(2)

        message_box.send_keys(Keys.ENTER)  # Enviar

        print(f"✅ Mensaje enviado a: {contact_name}")

    except Exception as e:
        print(f"❌ Error al enviar mensaje: {e}")
    # en 5 segundos se cierra, puedes editar los time.sleep en funcion de cuantos segundos quieres darle
    # a tu ordenador para que realice todo
    finally:
        time.sleep(5)
        driver.quit()
