import os
import sys
from tkinter import *
from tkinter import filedialog
# Importacion de Clases
import Analizador
import sintactico
import Generar_Menu
import Analizador_Factura
import Generar_Factura
import Generar_Grafica
# ------------ Variables Globales ------------
lexema = []
lexema_error = []
lexema_scan =[]
# ------------- Facturas
Datos_Facturas = []
contador_Facturas = 0
# ------------- Sintantico
Base = []

def main():
    print('-------------------- Proyecto 1 ---------------------')
    Presentacion()
    while True:
        opciones()
        print(">> Ingrese una Opcion:")
        print(">>", end="")
        entrada = input().lower()
        seleccion(entrada)

def seleccion(entrada):
    en = entrada
    if en == "1":
        print(" -------------------- Cargar Menu -------------------- ")
        openFile()
        sintactico.analizador_sintactico(lexema_scan, Base)
    elif en == "2":
        print(" -------------------- Cargar Orden -------------------- ")
        openFile_Factura()
    elif en == "3":
        print(" -------------------- Generar Menú --------------------")
        if Base !=[]:
            print(" ¿Desea Poner un Limite en los precios? Si/No")
            print(">>", end="")
            resp = input().lower()
            if resp == "si":
                try:
                    p_limite = float(input("Ingrese El Precio Limite:"))
                    Generar_Menu.reporte_Filtro(Base, p_limite)
                    os.system('Menu.html')
                except ValueError:
                    print("no ha ingresado un numero valido")
            elif resp == "no":
                Generar_Menu.reporte(Base)
                os.system('Menu.html')
            else:
                print(" ---------- Esta opcion No existe ----------")
        else:
            print("Ingrese un Archivo Valido en Cargar Menu para Generar Menu")
            print("----------------------------------------------------------")
    elif en == "4":
        print(" -------------------- Generar Factura -------------------- ")
        if Datos_Facturas != []:
            Generar_Factura.reporte(Base, Datos_Facturas)
            os.system('Factura.html')
        else:
            print("Ingrese un archivo Valido en Cargar Orden para poder Generar la Factura")
            print("----------------------------------------------------------")
    elif en == "5":
        print(" -------------------- Generar Árbol --------------------")
        if Base != []:
            Generar_Grafica.un(Base)
        else:
            print("Ingrese un Archivo Valido en Cargar Menu para Generar el Arbol")
            print("--------------------------------------------------------------------")
    elif en == "6":
        print(" -------------------- Salir --------------------")
        Presentacion()
        sys.exit()
    else:
        print(" --------------- No se Encontro la Opcion --------------- ")

def Presentacion():
    print('-----------------------------------------------------\n'
          '| Lenguajes Formales y de Programacion Seccion B+   |\n'
          '| Jhonathan Daniel Tocay Cotzojay Carné: 201801268  |\n'
          '-----------------------------------------------------')

def opciones():
    print('1. Cargar Menú')
    print('2. Cargar Orden')
    print('3. Generar Menú')
    print('4. Generar Factura')
    print('5. Generar Árbol')
    print('6. Salir')

def openFile():
    filepath = filedialog.askopenfilename(filetypes=(("Archivos de Texto","*.lfp"),("Todos Los Archivos","*.*")))
    archi(filepath)

def archi(filepath):
    archivo = open(filepath)
    file = archivo.read()
    # ------------------------------ Datos Del Archivo --------------------------------
    #-----------------------------------------------------------------------------------
    nombre_archivo = os.path.basename(filepath)
    extension = nombre_archivo.split('.')

    if (extension[-1].lower() == "lfp"):
        try:
            Analizador.analizador(file, lexema, lexema_error, lexema_scan)
        except:
            print("Opss!",sys.exc_info()[0],"ocured.")
    else:
        print("La extension del Archivo no es LFP")
# -----------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
def openFile_Factura():
    filepath = filedialog.askopenfilename(filetypes=(("Archivos de Texto", "*.lfp"),("Todos Los Archivos","*.*")))
    archivo_Factura(filepath)

def archivo_Factura(filepath):
    archivo = open(filepath)
    try:
        file = archivo.read()
    except:
        print("Opss!", sys.exc_info()[0], "ocured.")
    # ------------------------------ Datos Del Archivo --------------------------------
    # -----------------------------------------------------------------------------------
    nombre_archivo = os.path.basename(filepath)
    extension = nombre_archivo.split('.')
    #------------------------------------------------------------------------------------

    if (extension[-1].lower() == "lfp"):
        try:
            Analizador_Factura.factura(file, Datos_Facturas)
        except:
            print("Opss!",sys.exc_info()[0],"ocured.")
    else:
        print("La extension del Archivo no es LFP")

main()


