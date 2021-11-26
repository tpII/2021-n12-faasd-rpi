def handle(req): #Funcion que lee el sensor DHT11 y devuelve la temperatura

    import Adafruit_DHT

    sensor = Adafruit_DHT.DHT11
    pin = 4 #Pin en la raspberry donde conectamos el sensor
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    return temperatura
