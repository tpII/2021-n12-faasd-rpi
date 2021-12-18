def handle(req): #Funcion que lee el servidor y devuelve la temperatura

    import requests

    url= 'http://192.168.1.75:6000/temperatura'

    temperatura= requests.get(url).text

    return temperatura

