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
