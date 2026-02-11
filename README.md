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
-- 
