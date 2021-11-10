from flask import Flask,render_template

def index():
    lista=[]
    data={
        'titulo':'temperatura',
        'bienvenida':'hola',
        'lista':lista,
        'numeros_lista':len(lista)
    }
    return render_template('temperatura/index.html',data=data)