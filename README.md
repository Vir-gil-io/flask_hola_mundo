# 📘 Documentación del código Flask – Buscador de Lugares
Este proyecto es una aplicación web desarrollada con Flask que permite buscar lugares utilizando la API pública de OpenStreetMap (Nominatim) y mostrar los resultados en un mapa interactivo.
A continuación se explica detalladamente el funcionamiento de cada parte del código para comprender cómo trabaja Flask y cómo se integran las peticiones a una API externa.

---

## 📦 Importación de librerías

```python
from flask import Flask, render_template, request
import requests
```
**from flask import Flask, render_template, request**

Esta línea importa componentes esenciales del framework Flask:

- **Flask:**
Es la clase principal del framework. Se utiliza para crear la instancia de la aplicación web.
A partir de este objeto se definen rutas, se manejan peticiones HTTP y se ejecuta el servidor.

- **render_template:**
Función que permite renderizar archivos HTML ubicados en la carpeta templates.
Utiliza el motor de plantillas Jinja2, lo que permite insertar variables y lógica desde Python dentro del HTML.

- **request:**
Es un objeto especial de Flask que permite acceder a la información de las peticiones HTTP entrantes, como:
-- Datos enviados desde formularios
  - Datos enviados desde formularios.
  - Método de la petición (GET o POST).
  - Parámetros de la URL.
  - Cabeceras HTTP.

**import requests**

Se importa la librería externa requests, que se utiliza para realizar peticiones HTTP salientes desde Python hacia servicios externos.

📌 Es importante no confundir:

- **request** (Flask): maneja peticiones que llegan al servidor.
- **requests** (librería): se usa para enviar peticiones a otras APIs (en este caso, Nominatim).

---

## 🚀 Creación de la aplicación Flask

```python
app = Flask(__name__)
```
- Se crea una instancia de la clase Flask, la cual representa la aplicación web.
- **__name__** es una variable especial de Python que contiene el nombre del módulo actual.
- Flask utiliza este valor para:
  - Determinar la ruta base del proyecto.
  - Localizar las carpetas **templates** y **static**

En resumen, esta línea inicializa la aplicación y la deja lista para definir rutas y manejar solicitudes.

---

## 🛣️ Definición de la ruta principal

```python
@app.route('/', methods=['GET', 'POST'])
def buscar():
```
- **@app.route('/')** define la ruta principal de la aplicación (la raíz del sitio).
- **methods=['GET', 'POST']** indica que esta ruta acepta:
  - **GET:** cuando el usuario accede a la página por primera vez.
  - **POST:** cuando el usuario envía el formulario de búsqueda.

La función **buscar()** se ejecuta cada vez que se accede a esta ruta.



