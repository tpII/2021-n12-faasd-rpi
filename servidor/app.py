from flask import Flask
from flask import jsonify
import time
import board
import adafruit_dht

app = Flask(__name__)

#Iniciar el sensor dht, conectado al pin 17 
dhtDevice = adafruit_dht.DHT11(board.D17)

def getTemperatura():
    try:
        temperature = float(dhtDevice.temperature)
        return (temperature)
    except RuntimeError as error:
        print(error.args[0])

def getHumedad():
    try:
        humidity = float(dhtDevice.humidity)
        return (humidity)
    except RuntimeError as error:
        print(error.args[0])

@app.route("/temperatura")
def temperatura():
    temp= str(getTemperatura())
    return jsonify(entero=temp,
                   real=temp)

@app.route("/humedad")
def humedad():
    hum= str(getHumedad())
    return jsonify(entero=hum,
                   real=hum)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=6000)
