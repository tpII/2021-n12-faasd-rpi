def handle(req): # Funcion de prueba

    import random

    if (req == 'temp'):
        return str(random.randint(1,100))
    else:
        return 'No anda'
