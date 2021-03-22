def reporte_Tokens(base):
    nombre = 'Reporte_Factura_Tokens'
    with open(nombre + '.html', 'w') as html:
        html.write('<html>')
        html.write('    <head>')
        html.write('        <title>Reporte Tokens Aceptados</title>')
        html.write('        <link rel="stylesheet" type="text/css" href="estilo_TK.css">')
        html.write('    </head>')
        html.write('    <body >')
        html.write('        <h1><span class="blue"></span>Reporte<span class="blue"></span> <span class="yellow"> Tokens Factura</span></h1>')
        html.write('        <h2> Analisis <a target="_blank">Lexico</a></h2>')
        html.write('        <table class="container">')
        html.write('            <thead>')
        html.write('                <tr>')
        html.write('                    <th><h1>NO</h1></th>')
        html.write('                    <th><h1>LEXEMA</h1></th>')
        html.write('                    <th><h1>FILA</h1></th>')
        html.write('                    <th><h1>COLUMNA</h1></th>')
        html.write('                    <th><h1>TOKEN</h1></th>')
        html.write('                </tr>')
        html.write('            </thead>')
        html.write('            <tbody>')
        # -----------------------------------------------------------------------------------------
        i=0
        if (base != []):
            for al in base:
                i += 1
                html.write('                <tr>')
                html.write('                    <td>' + str(i) + '</td>')
                html.write('                    <td>' + str(al['valor']) + '</td>')
                html.write('                    <td>' + str(al['fila']) + '</td>')
                html.write('                    <td>' + str(al['columna']) + '</td>')
                html.write('                    <td>' + str(al['token']) + '</td>')
                html.write('                </tr>')
        else:
            html.write('                <tr>')
            html.write('                    <td></td>')
            html.write('                    <td>"LA LISTA ESTA VACIA"</td>')
            html.write('                </tr>')
        # -----------------------------------------------------------------------------------------
        html.write('            </tbody>')
        html.write('        </table>')
        html.write('    </body>')
        html.write('</html>')

# -------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------v
def reporte_Tokens_error(lexema_error):
    nombre = 'Reporte_Factura_Tokens_Error'
    with open(nombre + '.html', 'w') as html:
        html.write('<html>')
        html.write('    <head>')
        html.write('        <title>Reporte Tokens Rechazados</title>')
        html.write('        <link rel="stylesheet" type="text/css" href="estilo_TK.css">')
        html.write('    </head>')
        html.write('    <body >')
        html.write('        <h1><span class="blue"></span>Reporte<span class="blue"></span> <span class="yellow"> Errores Factura</span></h1>')
        html.write('        <h2> Analisis <a target="_blank"> Lexico y Sintactico</a></h2>')
        html.write('        <table class="container">')
        html.write('            <thead>')
        html.write('                <tr>')
        html.write('                    <th><h1>NO</h1></th>')
        html.write('                    <th><h1>LEXEMA</h1></th>')
        html.write('                    <th><h1>FILA</h1></th>')
        html.write('                    <th><h1>COLUMNA</h1></th>')
        html.write('                    <th><h1>TOKEN</h1></th>')
        html.write('                </tr>')
        html.write('            </thead>')
        html.write('            <tbody>')
        # -----------------------------------------------------------------------------------------
        i=0
        if (lexema_error != []):
            for al in lexema_error:
                i += 1
                html.write('                <tr>')
                html.write('                    <td>' + str(i) + '</td>')
                html.write('                    <td>' + str(al['fila']) + '</td>')
                html.write('                    <td>' + str(al['columna']) + '</td>')
                html.write('                    <td>' + str(al['valor']) + '</td>')
                html.write('                    <td>' + str(al['descripcion']) + '</td>')
                html.write('                </tr>')
        else:
            html.write('                <tr>')
            html.write('                    <td></td>')
            html.write('                    <td>"LA LISTA ESTA VACIA"</td>')
            html.write('                </tr>')
        # -----------------------------------------------------------------------------------------
        html.write('            </tbody>')
        html.write('        </table>')
        html.write('    </body>')
        html.write('</html>')