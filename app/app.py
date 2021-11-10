from flask import Flask,render_template
from resources import temperatura

app= Flask(__name__)

# Ruta para el Home (usando decorator)
@app.route("/")
def home():
    lista=[]
    data={
        'titulo':'temperatura',
        'bienvenida':'faasd',
        'lista':lista,
        'numeros_lista':len(lista)
    }
    return render_template("index.html",data=data)

app.add_url_rule("/temperatura", "temperatura_index", temperatura.index, methods = ['GET'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)