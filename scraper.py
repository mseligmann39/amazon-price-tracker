import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def scraper():

    # Configurar Selenium
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # Inicializar WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    products_data = []

    # Aqui puedes editar la URL que quieres que realice el scraping
    # pero deberas cambiar tambien lo otro, comprobando los tags html para obtener la informacion
    try:
        url = "https://www.amazon.es/s?k=zapatillas"
        driver.get(url)
        time.sleep(5)

        product_blocks = driver.find_elements(
            By.XPATH, '//div[@data-asin and @data-asin != ""]'
        )

        for product in product_blocks:
            # Obteniendo datos de detalles del producto con tags y atributos y valores
            try:
                detail = product.find_element(
                    By.CSS_SELECTOR,
                    "h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal",
                ).text.strip()
            except:
                detail = None
            # Obteniendo datos de nombre de producto con tags y atributos y valores
            try:
                name = product.find_element(
                    By.CSS_SELECTOR, "h2.a-size-mini.s-line-clamp-1"
                ).text.strip()
            except:
                name = None
            # Obteniendo datos del precio de producto con tags y atributos y valores
            try:
                price = product.find_element(
                    By.CSS_SELECTOR, "span.a-price-whole"
                ).text.strip()
            except:
                price = None

            if name and detail and price:
                products_data.append(
                    {"nombre": name, "detalle": detail, "precio": price}
                )

    finally:
        driver.quit()

    # Guardar como JSON
    json_file = "zapatillas.json" #Agrega nombre_de_carpeta\\archivo.json en caso de ser necesario
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(products_data, f, ensure_ascii=False, indent=2)
