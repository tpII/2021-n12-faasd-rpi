def handle(req): #Funcion que se comunica con el servidor y devuelve la humedad

    import requests

    url= 'http://192.168.1.75:6000/humedad'

    humedad= requests.get(url).text

    return humedad
