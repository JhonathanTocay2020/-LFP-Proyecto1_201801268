import time

no_factura =0
Productos =[]

def reporte(Base,Datos_Facturas):
    nombre_restaurante = Base[0]
    fecha = time.strftime("%d/%m/%Y")
    nombre = 'Factura'
    nombre_cliente = Datos_Facturas[0]
    nit = Datos_Facturas[1]
    direccion = Datos_Facturas[2]
    auxPropina = Datos_Facturas[3]
    auxPropina1 = auxPropina.replace('%','')
    Propina = float(auxPropina1)
    Propina_Decimal = Propina/100

    #print(auxPropina)
    #SubTotal = 0
    #auxPropina2 = int(auxPropina1)/100
    #print(auxPropina2)
    Productos = Datos_Facturas[4]
    Lista_Seccion = Base[2]
    #print(nombre_restaurante)
    #print('Factura No. XX')
    #print('Fecha: '+str(fecha))
    #print()
    #print('Datos del Cliente')
    #print('Nombre: ' + nombre_cliente)
    #print('NIT: '+nit)
    #print('Direccion: '+direccion)
    #print()
    #print("{:<20} {:^20} {:^20} {:^20}".format("Cantidad", "Concepto", "Precio", "total"))
    SubTotal = 0
    #for x in Productos:
    #    for z in Lista_Seccion:
    #        if z['id'] == x['ID']:
    #            cantidad = float(x['numero'])
    #            precio = float(z['numero'])
    #            total = cantidad * precio
    #            print("{:<20} {:^20} {:^20} {:^20}".format(x['numero'], z['nombre'],'Q. '+ str(precio),'Q. '+ str(total)))
    #            SubTotal += total

    #print("SubTotal: " + str(SubTotal))
    #auxPop = SubTotal * Propina_Decimal
    #print('Propina (' + str(auxPropina) + ')       Q. '+str(auxPop))
    #auxTotal = SubTotal + auxPop
    #print('Total: Q. '+ str(auxTotal))

    with open(nombre + '.html', 'w') as html:
        html.write('<!DOCTYPE html>')
        html.write('<html lang = "es">')
        html.write('    <head>')
        html.write('        <meta charset = "UTF-8">')
        html.write('        <meta name = "viewport" content= "width=divice-width,user-scalable=no,initial-scale=1.0,maxium-scale=1.0,minium-scale=1.0">')
        html.write('        <title>Factura</title>')
        html.write('        <link rel="stylesheet" href="style.css">')
        html.write('    </head>')
        html.write('    <body>')
        html.write('        <div class = "central">')
        html.write('            <h3>'+nombre_restaurante+'</h3>')
        html.write('            <h3>Factura No. '+ str(no_factura) +'</h3>')
        html.write('            <h3>Fecha: '+ str(fecha)+'</h3>')
        html.write('            <br>')
        html.write('            <p>&nbsp;&nbsp;&nbsp;&nbsp;Datos del Cliente</p>')
        html.write('            <p>&nbsp;&nbsp;&nbsp;&nbsp;Nombre:'+ nombre_cliente +' XX</p>')
        html.write('            <p>&nbsp;&nbsp;&nbsp;&nbsp;Nit:'+ nit +'</p>')
        html.write('            <p>&nbsp;&nbsp;&nbsp;&nbsp;Direccion:'+ direccion +'</p>')
        html.write('            <br>')
        html.write('            <h3>Descripcion</h3>')
        html.write('            <br>')
        html.write('            <table class="container">')
        html.write('                <thead>')
        html.write('                    <tr>')
        html.write('                        <th><h1>Cantidad</h1></th>')
        html.write('                        <th><h1>Conocepto</h1></th>')
        html.write('                        <th><h1>Precio</h1></th>')
        html.write('                        <th><h1>Total</h1></th>')
        html.write('                </thead>')
        html.write('                <tbody>')
        #------------------------------- Impresion de Productos -------------------------------
        #for x in Productos:
        #    for z in Lista_Seccion:
        #        if z['id'] == x['ID']:
        #            cantidad = float(x['numero'])
        #            precio = float(z['numero'])
        #            total = cantidad * precio
        #            print("{:<20} {:^20} {:^20} {:^20}".format(x['numero'], z['nombre'], 'Q. ' + str(precio),'Q. ' + str(total)))
        #            SubTotal += total

        #print("SubTotal: " + str(SubTotal))
        #auxPop = SubTotal * Propina_Decimal
        #print('Propina (' + str(auxPropina) + ')       Q. ' + str(auxPop))
        #auxTotal = SubTotal + auxPop
        #print('Total: Q. ' + str(auxTotal))
        #------------------------------------------------------------
        if Propina_Decimal >= 0 and Propina_Decimal <= 1:
            #print('propina aceptada')
            for x in Productos:
                for z in Lista_Seccion:
                    if z['id'] == x['ID']:
                        cantidad = float(x['numero'])
                        precio = float(z['numero'])
                        total = cantidad * precio
                        html.write('                    <tr>')
                        html.write('                        <td>' + str(x['numero']) + '</td>')
                        html.write('                        <td>' + str(z['nombre']) + '</td>')
                        html.write('                        <td>Q. ' + str("{:.2f}".format(precio)) + '</td>')
                        html.write('                        <td>Q. ' + str("{:.2f}".format(total)) + '</td>')
                        html.write('                    </tr>')
                        SubTotal += total

            html.write('                    <tr>')
            html.write('                        <td colspan="3">Sub Total</td>')
            html.write('                        <td>Q. ' + str("{:.2f}".format(SubTotal)) + '</td>')
            html.write('                    </tr>')
            auxPop = SubTotal * Propina_Decimal
            html.write('                        <td colspan="3">Propina (' + str(auxPropina) + ')</td>')
            html.write('                        <td>Q. ' + str("{:.2f}".format(auxPop)) + '</td>')
            html.write('                    </tr>')
            auxTotal = SubTotal + auxPop
            html.write('                    <tr>')
            html.write('                        <td colspan="3">Total</td>')
            html.write('                        <td>Q. ' + str("{:.2f}".format(auxTotal)) + '</td>')
            html.write('                    </tr>')
            # -------------------------------------------------------------------------------------
        else:
            html.write('                <tr>')
            html.write('                    <td colspan="4">"La propina no se encuentra en el Rango de 0% a 100%"</td>')
            html.write('                </tr>')
            #print('La propina no se encuentra en el Rango de 0% a 100%')
        html.write('                </tbody>')
        html.write('            </table>')
        html.write('        </div>')
        html.write('    </body>')
        html.write('</html>')
        html.close()



