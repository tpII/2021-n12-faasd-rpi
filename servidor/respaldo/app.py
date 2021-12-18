from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/temperatura")
def temperatura():
    temp= 6
    return jsonify(valor=temp,
                   unidad='Celcius')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=6001)
