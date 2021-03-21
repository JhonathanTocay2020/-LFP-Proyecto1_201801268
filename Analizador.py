import Generar_Token_Menu
import os

def analizador(cadena, lexema, lexema_error,lexema_scan):
    lexema.clear()
    lexema_error.clear()
    estado = 0
    num = ""
    fila = 1
    columna = 0
    auxReservada=""
    cad2 = ""
    i = 0

    while i < len(cadena):
        if estado == 0:
            if cadena[i] == '[':
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_Abrir_Corchete", "valor": "["})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_Abrir_Corchete", "valor": "["})
            elif cadena[i] == ']':
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_Cerrar_Corchete", "valor": "]"})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_Cerrar_Corchete", "valor": "]"})
            elif cadena[i] == ':':
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_Dos_Puntos", "valor": ":"})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_Dos_Puntos", "valor": ":"})
            elif cadena[i] == "'":
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_comilla", "valor": "'"})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_comilla", "valor": "'"})
                estado = 4
            elif cadena[i] == "=":
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_igual", "valor": "="})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_igual", "valor": "="})
            elif cadena[i] == ";":
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_Punto_Coma", "valor": ";"})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_Punto_Coma", "valor": ";"})
            elif (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122):
                auxReservada = auxReservada + cadena[i]
                estado = 1
            elif ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                num = num + cadena[i]
                estado = 2
            elif ord(cadena[i]) == 32 or cadena[i]=='':
                columna += 1
            elif cadena[i] == '\t':
                columna += 1
            elif cadena[i] == '\n':
                fila = fila + 1
            else:
                columna += 1
                lexema_error.append({"fila": fila, "columna": columna, "token": "tk_desconocido", "valor": cadena[i]})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_desconocido", "valor": cadena[i]})
    # --------------------------------------- Identificador ---------------------------------------------------------------
        elif (estado == 1):
            if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122) or (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (cadena[i] == "_"):
                auxReservada = auxReservada + cadena[i]
                estado = 1
            else:
                columna += 1
                if (auxReservada.lower() == 'restaurante'):
                    lexema.append({"fila": fila, "columna": columna, "token": "tk_" + auxReservada, "valor": auxReservada})
                    lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_" + auxReservada, "valor": auxReservada})
                    auxReservada = ""
                    estado = 0
                    i = i-1
                else:
                    lexema.append({"fila": fila, "columna": columna, "token": "tk_identificador", "valor": auxReservada})
                    lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_identificador", "valor": auxReservada})
                    auxReservada = ""
                    estado = 0
                    i = i-1
    # ---------------------------------------------- Numero ---------------------------------------------------------------
        elif(estado == 2):
            if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                num = num + cadena[i]
                estado = 2
            elif cadena[i] == '.' or ord(cadena[i]) == 46:
                num = num + cadena[i]
                estado = 3
            else:
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_numero", "valor": num})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_numero", "valor": num})
                num = ""
                i = i - 1
                estado = 0
    # -----------------------------------------  Numero Decimal  ---------------------------------------------------------
        elif estado == 3:
            if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
                num = num + cadena[i]
            else:
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_numero", "valor": num})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_numero", "valor": num})
                num = ""
                i = i-1
                estado = 0
    # -------------------------------------------- Cadena ----------------------------------------------
        elif estado == 4:
            if cadena[i] == "'":
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_cadena", "valor": cad2})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_cadena", "valor": cad2})
                columna += 1
                lexema.append({"fila": fila, "columna": columna, "token": "tk_comilla", "valor": "'"})
                lexema_scan.append({"fila": fila, "columna": columna, "token": "tk_comilla", "valor": "'"})
                cad2 = ""
                estado = 0
                #i -= 1
            else:
                cad2 = cad2 + cadena[i]

        i += 1

    Generar_Token_Menu.reporte_Tokens(lexema)
    os.system('Reporte_Tokens_Aceptados.html')
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    # ------------------------------------- imprimir -----------------------------------------
    #print("------------------------ Token Scan --------------------------")
    #for h in lexema_scan:
    #    print(h)
    #print("-------------------------------------------------------------------")
    #print("------------------------ Token Aceptados --------------------------")
    #for b in lexema:
    #    print(b)
    #print("-------------------------------------------------------------------")
    #print("------------------------ Token Rechazados -------------------------")
    #--------------- token error ------------------
    #for j in lexema_error:
    #    print(j)
    #print("-------------------------------------------------------------------")
