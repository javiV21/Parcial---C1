"""
Una biblioteca ofrece préstamos de libros a través de una tarjeta impresa que contiene los datos de la
persona que realiza el préstamo. El sistema de préstamos registra la fecha en que se retira el libro y la fecha
límite para su devolución. Realiza un programa que solvente esto de una manera más eficaz.
Implementar la sección de devolución la cual si la fecha excede la que devolución se dará una sanción.
"""
#Importar librería para calcular fechas
from datetime import datetime

class Libro():
    def __init__(self, titulo = "", autor = ""):
        self.titulo = titulo
        self.autor = autor

class Cliente():
    def __init__(self, nombre = "", numTarjeta = ""):
        self.nombre = nombre
        self.numTarjeta = numTarjeta

class Prestamo():
    def __init__(self, libro = "", cliente = "", fechaPrestamo = None, fechaLimite = None, fechaDevolucion = None):
        self.libro = libro
        self.cliente = cliente
        self.fechaPrestamo = fechaPrestamo
        self.fechaLimite = fechaLimite
        self.fechaDevolucion = fechaDevolucion

    #funcion que calcula los días de retraso y supone una multa de $1 por día de retraso
    def CalcularSancion(self):
        if (self.fechaDevolucion > self.fechaLimite):
            diasRetraso = (self.fechaDevolucion - self.fechaLimite).days
            sancion = diasRetraso * 1.0
        else:
            sancion = 0.0
        return sancion

    def MostrarDatos(self):
        print(f"Título del libro: {self.libro.titulo}, escrito por {self.libro.autor}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Número de tarjeta {self.cliente.numTarjeta}")
        print(f"Fecha de préstamo: {self.fechaPrestamo.strftime('%d-%m-%Y')}")
        print(f"Fecha límite de préstamo: {self.fechaLimite.strftime('%d-%m-%Y')}")
        print(f"Fecha de devolución: {self.fechaDevolucion.strftime('%d-%m-%Y')}")
        print(f"Sanción: ${self.CalcularSancion()}")

prestamo1L = input("Ingresa el título del libro: ")
prestamo1A = input("Ingresa el autor del libro: ")
prestamo1 = Libro(prestamo1L, prestamo1A)

datosCliN = input("Ingresa el nombre del cliente: ")
datosCliT = input(f"Ingresa el número de tarjeta de {datosCliN}: ")
datosCli = Cliente(datosCliN, datosCliT)

#se asegura que se ingresen los datos en formato correcto.
while True:
    try:
        fechaPrestamo = datetime.strptime(input("Ingresa la fecha de préstamo, con el siguiente formato (DD-MM-YYYY): "), "%d-%m-%Y")
        fechaLim = datetime.strptime(input("Ingresa la fecha límite del préstamo, con el siguiente formato (DD-MM-YYYY): "), "%d-%m-%Y")
        fechaDevolucion = datetime.strptime(input("Ingresa la fecha de devolución, siguiendo el formato (DD-MM-YYYY): "), "%d-%m-%Y")
        break
    except ValueError:
        print("Fecha ingresada en formato incorrecto. Por favor, usa el formato DD-MM-YYYY.")

#creación de herencia para que la clase prestamo tenga los valores necesarios.
devolucion = Prestamo(libro=prestamo1, cliente=datosCli, fechaPrestamo=fechaPrestamo, fechaLimite = fechaLim, fechaDevolucion=fechaDevolucion)
devolucion.MostrarDatos()