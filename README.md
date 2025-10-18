# Panel_de_control_invernadero-inteligente
Sistema interactivo para el monitoreo y control ambiental de un invernadero mediante Flask, SQLite y voz en español/inglés.
README.md (cópialo al archivo README.md en tu repositorio)
# 🌿🌿 Panel de Control - Invernadero Inteligente🌿🌿

<img width="1200" height="900" alt="image" src="https://github.com/user-attachments/assets/74633702-b5ed-4d5a-8ff0-1124f4c32936" />

**Invernadero Inteligente** es una aplicación web para monitorear variables ambientales (temperatura, humedad y pH). Permite **Crear, Leer, Actualizar y Eliminar (CRUD)** lecturas almacenadas en SQLite y genera un **reporte visual y hablado** en español e inglés que clasifica el estado de cada variable.

---

## 🚀 Características principales

- CRUD completo: Crear, Listar, Actualizar y Eliminar lecturas.
- Almacenamiento local con **SQLite** (`inventory.db`).
- Interfaz web atractiva y responsiva (estilo invernadero).
- Reporte automático que clasifica temperatura/humedad/pH (Baja / Normal / Alta / Ácido / Básico).
- Síntesis de voz en español e inglés (Web Speech API).
- Fácil despliegue local (solo Python + Flask).

---

## 📁 Estructura del proyecto



invernadero_inteligente/
├── server.py # Servidor Flask (punto de entrada)
├── database.py # Inicializa SQLite
├── inventory.db # (se crea automáticamente)
├── templates/
│ └── index.html
├── static/
│ └── (opcional: CSS, JS adicionales)
└── README.md


---

## ⚙️ Requisitos

Python 3.8 o superior
- SQLite3 (incluido por defecto con Python)
- Librería fastmcp instalada:
 pip install fastmcp

Instalar dependencias:
```bash
pip install flask

▶️ Ejecutar localmente

1. Inicializa la DB (si no existe):
python database.py
2. Ejecuta el servidor:
python server.py
3. Abre en el navegador:
http://127.0.0.1:8000

📸 Capturas finales

pantalla_inicio.png

pantalla_crear.png

pantalla_listar.png

pantalla_reporte.png

📦 Empaquetar y compartir

Comprime la carpeta en mcp_crud_inventory.zip.

Súbelo a Google Drive y comparte el enlace público.

Agrega el enlace en la wiki o en la página del repositorio.
