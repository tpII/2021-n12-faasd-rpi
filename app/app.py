from flask import Flask,render_template
import requests
import time
import db
import random

app= Flask(__name__)

# Iniciar base de datos
db.init_app(app)

# JYSERVER
import jyserver.Flask as jsf

## Variables
urltemp = 'http://192.168.1.75:8080/function/temperatura'
urlhum = 'http://192.168.1.75:8080/function/humedad'

@jsf.use(app)
class App:
    def __init__(self):
        self.count = -1 #Variable para leer temperatura=0 o humedad=1 o ninguna=-1
        # temp = requests.get(urltemp).json() # Llamar a funcion en rpi con get
        # hum = requests.get(urlhum).json() # Llamar a funcion en rpi con get

    def getTemperatura(self):
        self.count = 0
        self.js.document.getElementById("DisplayHumedad").style.display='none' # Hacer no visible el bloque Humedad
        self.js.document.getElementById("DisplayTemperatura").style.display='block' # Hacer visible el bloque temperatura
        while (self.count==0):   # Mientras siga en la seccion temperatura
            temp = requests.get(urltemp).json() # Llamar a funcion en rpi con get y obtener el JSON
            self.js.document.getElementById("ValorTemperatura").innerHTML= temp['entero'] # Actualizar valor
            db.add_temp(temp['entero'])             # Agregar valor a la base de datos

            temperaturas= db.ultimosdiez('temperatura')
            self.js.actualizarChart(temperaturas,'chartdivTemperatura')      # Actualizar el grafico
            time.sleep(1)

    def getHumedad(self):
        self.count = 1
        self.js.document.getElementById("DisplayTemperatura").style.display='none' # Hacer no visible el bloque temperatura
        self.js.document.getElementById("DisplayHumedad").style.display='block' # Hacer visible el bloque humedad
        while (self.count==1): # Mientras siga en la seccion humedad
            hum = requests.get(urlhum).json() # Llamar a funcion en rpi con get y obtener el JSON
            self.js.document.getElementById("ValorHumedad").innerHTML = hum['entero'] # Actualizar valor
            db.add_hum(hum['entero'])                 # Agregar valor a la base de datos

            humedades= db.ultimosdiez('humedad')      # O lista json
            self.js.actualizarChart(humedades,'chartdivHumedad')        # Actualizar el grafico
            time.sleep(1)


# Ruta para el Home (usando decorator)
@app.route("/")
def index():

    # temperaturas= ['temperatura':temperatura[1], 'timestamp':temperatura[0] for temperatura in db.ultimosdiez()]
    # print(type(temperaturas))
    # print(temperaturas)

    App.count=-1 # Hacer no visible ambos bloques temperatura y humedad

    data={
        'titulo':'RPI FAASD',
    }
    return App.render(render_template('index.html',data=data))

# app.add_url_rule("/", "", temperatura.index, methods = ['GET'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)