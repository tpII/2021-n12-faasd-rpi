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
        temp = requests.get(urltemp) # Llamar a funcion en rpi con get
        hum = requests.get(urlhum) # Llamar a funcion en rpi con get

    def getTemperatura(self):
        self.count = 0
        contador= 2
        self.js.document.getElementById("DisplayHumedad").style.display='none'      # Hacer no visible el bloque Humedad
        self.js.document.getElementById("DisplayHome").style.display='none'         # Hacer no visible el bloque home
        self.js.document.getElementById("DisplayTemperatura").style.display='block' # Hacer visible el bloque temperatura
        while (self.count==0):                  # Mientras siga en la seccion temperatura
            response = requests.get(urltemp)    # Llamar a funcion en rpi con get y obtener el JSON
            if (str(response)=='<Response [200]>'):
                temp= response.json()
                db.add_temp(temp['valor'])               # Agregar valor a la base de datos

                self.js.setearTemperatura(temp['valor'])                                               # Actualizar termometro
                if (contador==2):
                    temperaturas= db.ultimosdiez('temperatura')                                         # Obtener valores historicos
                    self.js.actualizarChart(temperaturas,'chartdivTemperatura')                         # Actualizar el grafico
                    self.js.document.getElementById("chartdivTemperatura").style.display='block'        # Hacer visible el grafico
                    contador=0
                else:
                    contador+=1
            else:
                print('Deployeando funcion')
                
            time.sleep(5)

    def getHumedad(self):
        self.count = 1
        self.js.document.getElementById("DisplayTemperatura").style.display='none'  # Hacer no visible el bloque temperatura
        self.js.document.getElementById("DisplayHome").style.display='none'         # Hacer no visible el bloque home
        self.js.document.getElementById("DisplayHumedad").style.display='block'     # Hacer visible el bloque humedad
        while (self.count==1):                  # Mientras siga en la seccion humedad
            response = requests.get(urlhum)     # Llamar a funcion en rpi con get y obtener el JSON
            if (str(response)=='<Response [200]>'):
                hum= response.json()
                db.add_hum(hum['valor'])                 # Agregar valor a la base de datos

                humedades= db.ultimosdiez('humedad')                                        # Obtener valores historicos
                self.js.actualizarChart(humedades,'chartdivHumedad')                        # Actualizar el grafico
                self.js.setearHumedad(hum['valor'])                                        # Actualizo termometro
                self.js.document.getElementById("chartdivHumedad").style.display='block'    # Hacer visible el grafico
            else:
                print('Deployeando funcion')
                
            time.sleep(5)

# Ruta para el Home (usando decorator)
@app.route("/")
def index():

    App.count=-1 # Hacer no visible ambos bloques temperatura y humedad

    data={
        'titulo':'RPI FAASD',
    }
    return App.render(render_template('index.html',data=data))

# app.add_url_rule("/", "", temperatura.index, methods = ['GET'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)