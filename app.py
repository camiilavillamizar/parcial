from flask import Flask
import csv 
import os
from pathlib import Path
from datetime import datetime


app = Flask(__name__)

class datos:
    def __init__(self, fch, ti, te, h):
        self.fch = fch
        self.ti = ti
        self.te = te
        self.h = h
    def __str__(self):
        return self.ti+","+self.te+","+self.h

@app.route("/")
def inicio():
    return "Hola mundo"

@app.route("/log/<ti>/<te>/<h>")
def index(ti, te, h):
    archivo = open("09052019.csv", "a")
    d = datos(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),ti, te, h)
    print(d)
    archivo.write(str(d.fch)+" "+str(d.ti)+","+str(d.te)+","+str(d.h)+"\n");
    return "Dato agregado con éxito"




    