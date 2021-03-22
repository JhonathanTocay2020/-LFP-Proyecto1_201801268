import Generar_Token_Factura
import os
#--------------Variables Globales------------------
auxNum=''
auxI=''
tokens=[]
tokens_error=[]
auxProducto =[]
#--------------------------------------------------
def factura(cadena,Datos_Facturas):
    fila = 1
    columna = 0
    cadena = cadena+"\n"
    estado = 0
    num = ""
    auxReservada=""
    cad2 = ""
    i = 0
    while i < len(cadena):
        if estado == 0:
            if cadena[i] == "'":
                columna+=1
                estado = 3
            elif cadena[i] == ',':
                columna +=1
            elif (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122):
                auxReservada = auxReservada + cadena[i]
                estado = 1
            elif ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                num = num + cadena[i]
                estado = 2
            #--------------------------------------------------------
            elif ord(cadena[i]) == 32 or cadena[i]=='':
                columna += 1
            elif cadena[i] == '\t':
                columna += 1
            elif cadena[i]=="\n":
                fila +=1
            #----------------------------------------------------------------
            else:
                tokens_error.append({"fila": fila, "columna": columna, "valor": cadena[i],"descripcion": "[Error Lexico] Caracter Desconocido"})
                estado = 0
    # --------------------------------------- Identificador ---------------------------------------------------------------
        elif (estado == 1):
            if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122) or (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (cadena[i] == "_"):
                auxReservada = auxReservada + cadena[i]
                estado = 1

            else:
                #print(auxReservada)
                columna += 1
                tokens.append({"token": "tk_id", "valor": auxReservada,"fila":fila,"columna": columna})
                auxReservada = ""
                estado = 0
                i = i-1
    # ---------------------------------------------- Numero ---------------------------------------------------------------
        elif(estado == 2):
            if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                num = num + cadena[i]
                estado = 2
            elif ord(cadena[i])==37:
                num = num + cadena[i]
                columna += 1
                tokens.append({"token": "tk_porcentaje", "valor": num,"fila":fila,"columna": columna})
                num = ""
                estado = 0
            else:
                columna += 1
                tokens.append({"token": "tk_numero", "valor": num,"fila":fila,"columna": columna})
                num = ""
                estado = 0
                i = i - 1
    # -------------------------------------------- Cadena ----------------------------------------------
        elif estado == 3:
            if cadena[i] == "'":
                columna +=1
                tokens.append({"token": "tk_cadena", "valor": cad2,"fila":fila,"columna": columna})
                cad2 = ""
                estado = 0
            else:
                cad2 = cad2 + cadena[i]
        i += 1
    # ------------------------------------- Obtener Datos -----------------------------------------
    #print("------------------------ Tokens --------------------------")

    for h in tokens:
        if h['token'] == 'tk_cadena':
            Datos_Facturas.append(h['valor'])
        elif h['token'] == 'tk_porcentaje':
            Datos_Facturas.append(h['valor'])
        elif h['token'] == 'tk_numero':
            auxNum = h['valor']
        elif h['token'] == 'tk_id':
            auxI = h['valor']
            auxProducto.append({"numero": auxNum,"ID": auxI})
            auxNum = ""
            auxI = ""

    Datos_Facturas.append(auxProducto)
    Generar_Token_Factura.reporte_Tokens(tokens)
    os.system('Reporte_Factura_Tokens.html')

    if tokens_error !=[]:
        Generar_Token_Factura.reporte_Tokens_error(tokens_error)
        os.system('Reporte_Factura_Tokens_Error.html')

    #for p in Datos_Facturas:
    #    print(p)
    print("-------------------------------------------------------------------")