from flask import Flask,render_template
import requests
import time

app= Flask(__name__)

#jyserver
import jyserver.Flask as jsf

## Cosas 
url = 'http://192.168.1.75:8080/function/prueba'
reqtemp = 'temp'
reqhum= 'hum'

@jsf.use(app)
class App:
    def __init__(self):
        self.count = -1 #Variable para leer temperatura=0 o humedad=1 o ninguna=-1
        # temp = requests.post(url, reqtemp).text[:-1] # Llamar a funcion en rpi con post
        # temp = requests.post(url, reqhum).text[:-1] # Llamar a funcion en rpi con post

    def getTemperatura(self):
        self.count = 0
        self.js.document.getElementById("DisplayHumedad").style.display='none' # Hacer no visible el bloque Humedad
        self.js.document.getElementById("DisplayTemperatura").style.display='block' # Hacer visible el bloque temperatura
        while (self.count==0): # Mientras siga en la seccion temperatura
            temp = requests.post(url, reqtemp).text[:-1] # Llamar a funcion en rpi con post
            self.js.document.getElementById("ValorTemperatura").innerHTML=temp # Actualizar valor
            time.sleep(2)
    
    def getHumedad(self):
        self.count = 1
        self.js.document.getElementById("DisplayTemperatura").style.display='none' # Hacer no visible el bloque temperatura
        self.js.document.getElementById("DisplayHumedad").style.display='block' # Hacer visible el bloque humedad
        while (self.count==1): # Mientras siga en la seccion humedad
            # temp = requests.post(url, reqhum).text[:-1] # Llamar a funcion en rpi con post
            self.js.document.getElementById("ValorHumedad").innerHTML='Humedad' # Actualizar valor
            time.sleep(2)

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