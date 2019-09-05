from flask import Flask
import csv 
import os
from pathlib import Path
from datetime import datetime
from copy import deepcopy   #Para implementar prototype 


app = Flask(__name__)

class datos:
    clon = 0
    def __init__(self, fch, ti, te, h):
        self.fch = fch
        self.ti = ti
        self.te = te
        self.h = h
    def __str__(self):
        return self.fch+","+self.ti+","+self.te+","+self.h+"\n"

    def clonacion(self):
        self.clon = 1
        return deepcopy(self)

@app.route("/")
def inicio():
    return "Hola mundo"

@app.route("/log/<ti>/<te>/<h>")
def index(ti, te, h):
    archivo = open("09052019.csv", "a")
    d = datos(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),ti, te, h)
    dcopy = d.clonacion()
    print(d)
    archivo.write(str(dcopy.fch)+" "+str(dcopy.ti)+","+str(dcopy.te)+","+str(dcopy.h)+"\n");
    return "Dato agregado con éxito"




    