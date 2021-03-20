# -------------------- VARIABLES GLOBALES AUXILIARES ------------------------------
auxNS = ''
auxID = ''
auxNombre_ID = ''
auxPrecio = ''
auxDescripcion = ''


def analizador_sintactico(lexema_scan, Base):
    nombre_del_Restaurante = ''
    Nombre_Seccion = []
    Lista_Seccion =[]
    print("------------------------ Sintactico --------------------------")
    i = 0
    estado = 0

    while i < len(lexema_scan):
    # --------------------------------------- Estado Inicial --------------------------------------------
        if estado == 0:
            if(lexema_scan[i]['token'] == 'tk_restaurante'):
                estado = 1

            elif(lexema_scan[i]['token'] == "tk_comilla"):
                estado = 5

            elif(lexema_scan[i]['token'] == "tk_Abrir_Corchete"):
                estado = 8
            else:
                estado = 0
    # -------------------------------------------------------------------------------------------------
        # ------------------------------ Restaurante --------------------------------------
        elif estado == 1:
            if(lexema_scan[i]['token'] == 'tk_igual'):
                estado = 2
            else:
                print('se esperaba un signo =')

        elif estado == 2:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 3
            else:
                print("se esperaba un signo '")

        elif estado == 3:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                nombre_del_Restaurante = lexema_scan[i]['valor']
                lexema_scan[i]['token'] = 'tk_Nombre_Restaurante'
                estado = 4
            else:
                print("se esperaba una cadena")

        elif estado == 4:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 0
            else:
                print("se esperaba un signo '")
    # -------------------------------------------------------------------------------------------------
        # -------------------------------- Seccion ----------------------------------------------
        elif estado == 5:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                Nombre_Seccion.append(lexema_scan[i]['valor'])
                auxNS = lexema_scan[i]['valor']
                lexema_scan[i]['token'] = 'tk_Seccion'
                estado = 6
            else:
                print("Cadena no reconocida")

        elif estado == 6:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 7
            else:
                print("se esperaba un signo '")

        elif estado == 7:
            if (lexema_scan[i]['token'] == "tk_Dos_Puntos"):
                estado = 0
            else:
                print("se esperaba punto y coma")
    # -------------------------------------------------------------------------------------------------
        # -------------------------------- Producto ----------------------------------------------
        elif estado == 8:
            if (lexema_scan[i]['token'] == "tk_identificador"):
                auxID = lexema_scan[i]['valor']
                estado = 9
            else:
                print("se esperaba comilla simple")

        elif estado == 9:
            if (lexema_scan[i]['token'] == "tk_Punto_Coma"):
                estado = 10
            else:
                print("se esperaba punto y coma")

        elif estado == 10:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 11
            else:
                print("se esperaba comilla simple")

        elif estado == 11:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                lexema_scan[i]['token'] = 'tk_Nombre_identificador'
                auxNombre_ID = lexema_scan[i]['valor']
                estado = 12
            else:
                print("Se esperaba una cadena")

        elif estado == 12:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 13
            else:
                print("se esperaba comilla simple")

        elif estado == 13:
            if (lexema_scan[i]['token'] == "tk_Punto_Coma"):
                estado = 14
            else:
                print("se esperaba punto y coma")

        elif estado == 14:
            if (lexema_scan[i]['token'] == "tk_numero"):
                auxPrecio = lexema_scan[i]['valor']
                estado = 15
            else:
                print("se esperaba un numero")

        elif estado == 15:
            if (lexema_scan[i]['token'] == "tk_Punto_Coma"):
                estado = 16
            else:
                print("se esperaba punto y coma")

        elif estado == 16:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 17
            else:
                print("se esperaba comilla simple")

        elif estado == 17:
            if (lexema_scan[i]['token'] == "tk_cadena"):
                lexema_scan[i]['token'] = 'tk_Descripcion'
                auxDescripcion = lexema_scan[i]['valor']
                estado = 18
            else:
                print("Se esperaba una cadena")

        elif estado == 18:
            if (lexema_scan[i]['token'] == "tk_comilla"):
                estado = 19
            else:
                print("se esperaba comilla simple")

        elif estado == 19:
            if (lexema_scan[i]['token'] == "tk_Cerrar_Corchete"):
                Lista_Seccion.append({"seccion": auxNS,"id": auxID, "nombre": auxNombre_ID, "numero": float(auxPrecio), "descripcion": auxDescripcion})
                auxID = ''
                auxNombre_ID = ''
                auxPrecio = ''
                auxDescripcion = ''
                estado = 0
            else:
                print("se esperaba ]")
        i += 1

    Base.append(nombre_del_Restaurante)
    Base.append(Nombre_Seccion)
    Base.append(Lista_Seccion)

    # -------------------------------------------------------------------------
    #print("----------------------------- Datos --------------------------")
    #print('Nombre Restaurante: ' + nombre_del_Restaurante)
    #print("Secciones: " + str(Nombre_Seccion))
    #print("Productos: ")
    #for x in Lista_Seccion:
    #   print(x)
