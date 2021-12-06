def handle(req): # Funcion de prueba

    import random

    if (req == 'temp'):
        return str(random.randint(-10,10))
    else:
        return 'No andaaa'
