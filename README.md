# amazon-price-tracker
Scraper con Selenium que rastrea precios en Amazon y envía alertas por WhatsApp

# 🛒 Amazon Price Tracker + WhatsApp Notifier

Este proyecto es un **scraper en Python** que rastrea los precios de productos en Amazon y te notifica por **WhatsApp** cuando detecta un cambio significativo.

## ✅ Características

- 🕷️ Scraping de productos de Amazon con `Selenium`
- 📉 Detección de cambios en el precio
- 📲 Notificaciones automáticas por WhatsApp Web
- 🕑 Automatización periódica con `schedule`

## 📂 Estructura del proyecto

amazon-price-tracker/
├── scraper.py
├── notifier.py
├── main.py
├── iniciar_perfil_whatsapp.bat
├── requirements.txt
├── .gitignore
└── README.md


## ⚙️ Requisitos

- Python 3.9+
- Google Chrome instalado
- Cuenta en WhatsApp Web

Instala las dependencias:

```bash
pip install -r requirements.txt

 Librerías utilizadas
selenium

webdriver-manager

schedule

pyperclip

# Creado por Maximiliano Seligmann
