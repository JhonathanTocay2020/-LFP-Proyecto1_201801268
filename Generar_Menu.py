nombre_del_Restaurante =''
Nombre_Seccion = []
Lista_Seccion = []

def reporte(Base):
    nombre_del_Restaurante = Base[0]
    Nombre_Seccion = Base[1]
    Lista_Seccion = Base[2]
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    #print(nombre_del_Restaurante)
    #i=0
    #for x in Nombre_Seccion:
        # h2
    #    i = i + 1
    #    print("No."+str(i))
        #h3
    #    print(x)
    #    for z in Lista_Seccion:
    #        #p
    #        if z['seccion'] == x:
    #            Numero = float(z['numero'])
    #            print("{:<10} {:<10}".format(z['nombre'], 'Q. ' + str(Numero)))
    #            print("{:<10}".format(z['descripcion']))
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    nombre = 'Menu'
    with open(nombre + '.html', 'w') as html:
        html.write('< !DOCTYPE>')
        html.write('<html>')
        html.write('    <head>')
        html.write('        <meta name = "viewport" content="width=device-width,initial-scale=1.0">')
        html.write('        <meta charset = "utf-8">')
        html.write('        <title>'+nombre_del_Restaurante +'</title>')
        html.write('        <link rel= ' + 'stylesheet' + ' type="text/css" href = "estilo.css">')
        html.write('    </head>')
        html.write('    <body>')
        html.write('        <div class="container">')
        html.write('            <h1>'+nombre_del_Restaurante +'</h1>')
        html.write('        </div>')
        html.write('        <div class="conten">')
        html.write('            <div class = "container">')
        # --------------------------------------------------------------------------------------------------
        # -------------------------------------- Impresion del Menu ----------------------------------------
        i=0
        for x in Nombre_Seccion:
            i = i + 1
            html.write('                <div class ="box">')
            html.write('                    <h2>'+ str(i) +'</h2>')
            html.write('                    <h3>'+x+'</h3>')
            for z in Lista_Seccion:
                if (z['seccion']==x):
                    Numero = float(z['numero'])
                    html.write('                    <p>'+z['nombre']+' Q ' + str(Numero) + ' <br>' +z['descripcion']+ '</p><br>')
            html.write('                </div>')
        # --------------------------------------------------------------------------------------------------
        html.write('            </div>')
        html.write('        </div>')
        html.write('    </body>')
        html.write('</html>')
        html.close()

def reporte_Filtro(Base,p_limite):
    nombre_del_Restaurante = Base[0]
    Nombre_Seccion = Base[1]
    Lista_Seccion = Base[2]
    # --------------------------------------------------------------------------------------
    nombre = 'Menu'
    with open(nombre + '.html', 'w') as html:
        html.write('< !DOCTYPE>')
        html.write('<html>')
        html.write('    <head>')
        html.write('        <meta name = "viewport" content="width=device-width,initial-scale=1.0">')
        html.write('        <meta charset = "utf-8">')
        html.write('        <title>'+nombre_del_Restaurante +'</title>')
        html.write('        <link rel= ' + 'stylesheet' + ' type="text/css" href = "estilo.css">')
        html.write('    </head>')
        html.write('    <body>')
        html.write('        <div class="container">')
        html.write('            <h1>'+nombre_del_Restaurante +'</h1>')
        html.write('        </div>')
        html.write('        <div class="conten">')
        html.write('            <div class = "container">')
        # --------------------------------------------------------------------------------------------------
        # -------------------------------------- Impresion del Menu ----------------------------------------
        i=0
        limite = float(p_limite)
        for x in Nombre_Seccion:
            i = i + 1
            html.write('                <div class ="box">')
            html.write('                    <h2>'+ str(i) +'</h2>')
            html.write('                    <h3>'+x+'</h3>')
            for z in Lista_Seccion:
                if (z['seccion']==x):
                    Numero = float(z['numero'])
                    if Numero <= limite:
                        #print(Numero)
                        #print(limite)
                        html.write('                    <p>'+z['nombre']+' Q ' + str(Numero) + ' <br>' +z['descripcion']+ '</p><br>')
            html.write('                </div>')
        # --------------------------------------------------------------------------------------------------
        html.write('            </div>')
        html.write('        </div>')
        html.write('    </body>')
        html.write('</html>')
        html.close()