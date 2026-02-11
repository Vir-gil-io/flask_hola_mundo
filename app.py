from flask import Flask, render_template, request
import requests
#importando la librería de Flask

app = Flask(__name__)

#Se crea un objeto app con su propiedad __name__ que se establece como el nombre del módulo actual.

#@app.route('/')
#def index():
#    return render_template('index.html')
#Se define la respuesta por medio de un método para la ruta especificada

@app.route('/', methods=['GET', 'POST'])
def buscar():
    lugares = []
    error = False
    query=""
    
    if request.method == 'POST':
        query = request.form['lugar']
        
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': query,
            'format': 'json',
            'limit': 5
        }
        
        headers = {
            "User-Agent": "Flask-Educational-App"
        }

        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()

        if data:
            for item in data:
                lugares.append({
                    'lat': item['lat'],
                    'lon': item['lon'],
                    'nombre': item['display_name']
                })
        else:
            error = True

    return render_template(
        'map.html',
        lugares=lugares,
        error=error,
        query=query
    )

if __name__=='__main__':
    app.run(debug=True)