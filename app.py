from flask import Flask
import csv 
import os
from pathlib import Path

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Funciona"

@app.route("/log/<ti>/<te>/<h>")
def index(ti, te, h):
    archivo = open("09052019.csv", "a")
    archivo.write(str(ti)+","+str(te)+","+str(h));
    return "Dato agregado con éxito"




    