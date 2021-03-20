
#--------------Variables Globales------------------
auxNum=''
auxI=''
tokens=[]
auxProducto =[]
#--------------------------------------------------
def factura(cadena,Datos_Facturas):
    cadena = cadena+"\n"
    estado = 0
    num = ""
    auxReservada=""
    cad2 = ""
    i = 0
    while i < len(cadena):
        if estado == 0:
            if cadena[i] == "'":
                #print("'")
                estado = 3
            elif (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122):
                auxReservada = auxReservada + cadena[i]
                estado = 1
            elif ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                num = num + cadena[i]
                estado = 2
            else:
                estado = 0
    # --------------------------------------- Identificador ---------------------------------------------------------------
        elif (estado == 1):
            if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122) or (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (cadena[i] == "_"):
                auxReservada = auxReservada + cadena[i]
                estado = 1

            else:
                #print(auxReservada)
                tokens.append({"token": "tk_id", "valor": auxReservada})
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
                tokens.append({"token": "tk_porcentaje", "valor": num})
                num = ""
                estado = 0
            else:
                tokens.append({"token": "tk_numero", "valor": num})
                num = ""
                estado = 0
                i = i - 1
    # -------------------------------------------- Cadena ----------------------------------------------
        elif estado == 3:
            if cadena[i] == "'":
                tokens.append({"token": "tk_cadena", "valor": cad2})
                cad2 = ""
                estado = 0
            else:
                cad2 = cad2 + cadena[i]
        i += 1
    # ------------------------------------- imprimir -----------------------------------------
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
    #for p in Datos_Facturas:
    #    print(p)
    print("-------------------------------------------------------------------")