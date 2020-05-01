# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:44:10 2020

@author: Franco
"""
import csv, sys

def process(d,n,p):
    sys.stdout.write("\nFecha: " + d + " Nombre: " + n + " Precio: " + str(p))

print("Comenzando proceso:")


with open('archivo_csv_columnas.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        nombre = row["nombre"]
        closing_price = float(row["closing_price"])
        process(date, nombre, closing_price)

print("\n\nProceso finalizado")
        