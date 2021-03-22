import Generar_Token_Menu
import os
# -------------------- VARIABLES GLOBALES AUXILIARES ------------------------------
auxNS = ''
auxID = ''
auxNombre_ID = ''
auxPrecio = ''
auxDescripcion = ''


def analizador_sintactico(lexema_scan, Base,lexema_error,Lexemas_aceptados):
    nombre_del_Restaurante = ''
    Nombre_Seccion = []
    Lista_Seccion =[]
    print("------------------------ Sintactico --------------------------")
    i = 0
    estado = 0
    cont_res = 1
    while i < len(lexema_scan):
    # --------------------------------------- Estado Inicial --------------------------------------------
        if estado == 0:
            if(lexema_scan[i]['token'] == 'tk_restaurante'):
                if cont_res == 1:
                    Lexemas_aceptados.append(lexema_scan[i])
                    cont_res += 1
                    estado = 1
                else:
                    lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] Se repite la palabra reservada Restaurante"})
                    estado = 0
            elif(lexema_scan[i]['token'] == "tk_comilla"):
                estado = 5

            elif(lexema_scan[i]['token'] == "tk_Abrir_Corchete"):
                estado = 8
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico Desconocido]"})
                estado = 0
    # -------------------------------------------------------------------------------------------------
        # ------------------------------ Restaurante --------------------------------------
        elif estado == 1:
            if(lexema_scan[i]['token'] == 'tk_igual'):
                estado = 2
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo ="})
                estado = 0

        elif estado == 2:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 3
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0

        elif estado == 3:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                nombre_del_Restaurante = lexema_scan[i]['valor']
                lexema_scan[i]['token'] = 'tk_Nombre_Restaurante'
                Lexemas_aceptados.append(lexema_scan[i])
                estado = 4
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] Se Esperaba el Nombre del Restaurante"})
                estado = 0

        elif estado == 4:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 0
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0
    # -------------------------------------------------------------------------------------------------
        # -------------------------------- Seccion ----------------------------------------------
        elif estado == 5:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                Nombre_Seccion.append(lexema_scan[i]['valor'])
                auxNS = lexema_scan[i]['valor']
                lexema_scan[i]['token'] = 'tk_Seccion'
                Lexemas_aceptados.append(lexema_scan[i])
                estado = 6
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] Se esperaba el Nombre de una Seccion'"})
                estado = 0

        elif estado == 6:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 7
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0

        elif estado == 7:
            if (lexema_scan[i]['token'] == "tk_Dos_Puntos"):
                estado = 0
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] Se esperaba 2 puntos"})
                estado = 0

    # -------------------------------------------------------------------------------------------------
        # -------------------------------- Producto ----------------------------------------------
        elif estado == 8:
            if (lexema_scan[i]['token'] == "tk_identificador"):
                auxID = lexema_scan[i]['valor']
                Lexemas_aceptados.append(lexema_scan[i])
                estado = 9
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un identificador"})
                estado = 0

        elif estado == 9:
            if (lexema_scan[i]['token'] == "tk_Punto_Coma"):
                estado = 10
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'],"valor": lexema_scan[i]['valor'],"descripcion": "[Error Sintactico] se esperaba un punto y coma"})
                estado = 0

        elif estado == 10:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 11
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'],"descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0

        elif estado == 11:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                lexema_scan[i]['token'] = 'tk_Nombre_identificador'
                auxNombre_ID = lexema_scan[i]['valor']
                Lexemas_aceptados.append(lexema_scan[i])
                estado = 12
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'],"valor": lexema_scan[i]['valor'],"descripcion": "[Error Sintactico] se esperaba el nombre del identificador"})
                estado = 0

        elif estado == 12:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 13
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0

        elif estado == 13:
            if (lexema_scan[i]['token'] == "tk_Punto_Coma"):
                estado = 14
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un punto y coma "})
                estado = 0

        elif estado == 14:
            if (lexema_scan[i]['token'] == "tk_numero"):
                auxPrecio = lexema_scan[i]['valor']
                Lexemas_aceptados.append(lexema_scan[i])
                estado = 15
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un Numero"})
                estado = 0

        elif estado == 15:
            if (lexema_scan[i]['token'] == "tk_Punto_Coma"):
                estado = 16
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un punto y coma"})
                estado = 0

        elif estado == 16:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 17
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0

        elif estado == 17:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                lexema_scan[i]['token'] = 'tk_Descripcion'
                auxDescripcion = lexema_scan[i]['valor']
                Lexemas_aceptados.append(lexema_scan[i])
                estado = 18
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba una Descripcion"})
                estado = 0

        elif estado == 18:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 19
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba un signo '"})
                estado = 0

        elif estado == 19:
            if (lexema_scan[i]['token'] == "tk_Cerrar_Corchete"):
                Lista_Seccion.append({"seccion": auxNS,"id": auxID, "nombre": auxNombre_ID, "numero": float(auxPrecio), "descripcion": auxDescripcion})
                auxID = ''
                auxNombre_ID = ''
                auxPrecio = ''
                auxDescripcion = ''
                estado = 0
            else:
                lexema_error.append({"fila": lexema_scan[i]['fila'], "columna": lexema_scan[i]['columna'], "valor": lexema_scan[i]['valor'], "descripcion": "[Error Sintactico] se esperaba ]"})
                estado = 0
        i += 1

    Base.append(nombre_del_Restaurante)
    Base.append(Nombre_Seccion)
    Base.append(Lista_Seccion)

    Generar_Token_Menu.reporte_Tokens_AS(Lexemas_aceptados)
    os.system('Reporte_Tokens_Aceptados_S.html')

    # ----------------------------------------------------
    if lexema_error != []:
        Generar_Token_Menu.reporte_Tokens_error(lexema_error)
        os.system('Reporte_Tokens_Error.html')
    # -------------------------------------------------------------------------
    #print("----------------------------- Datos --------------------------")
    #print('Nombre Restaurante: ' + nombre_del_Restaurante)
    #print("Secciones: " + str(Nombre_Seccion))
    #print("Productos: ")
    #for x in Lista_Seccion:
    #   print(x)
