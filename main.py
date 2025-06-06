import json
from notifier import send_whatsapp_alert
from scraper import scraper

# Formatea el json para crear bloques de 10 productos para enviar a whatsapp y que no llegue al limite
def generar_mensajes(productos, por_bloque=10):
    def formatear_producto(p, index=None):
        encabezado = f"🔹 Producto {index + 1}" if index is not None else "🔹 Producto"
        return (
            f"{encabezado}:\n"
            f"📦 {p.get('nombre') or 'Sin nombre'}\n"
            f"📘 {p.get('detalle') or 'Sin detalle'}\n"
            f"💰 {p.get('precio') or 'Sin precio'}\n"
        )

    mensajes = []
    total = len(productos)

    for i in range(0, total, por_bloque):
        bloque = productos[i : i + por_bloque]
        cuerpo = "\n".join(
            formatear_producto(p, i + idx) for idx, p in enumerate(bloque)
        )
        encabezado = f"📢 Amazon Best Sellers (parte {i // por_bloque + 1}/{-(-total // por_bloque)})\n\n"
        mensajes.append(encabezado + cuerpo)

    return mensajes

# Llamando a la funcion scraper que crea el json para luego enviar
scraper()

# Cargar productos
with open("test\\zapatillas.json", encoding="utf-8") as f:
    productos = json.load(f)

# Generar mensajes
mensajes = generar_mensajes(productos, por_bloque=10)

# Enviar por WhatsApp
for msg in mensajes:
    send_whatsapp_alert(msg, contact_name="Yo")  # Cambia "Yo" según tu a que contacto quieras enviar esto
