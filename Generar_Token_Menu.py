def reporte_Tokens(base):
    nombre = 'Reporte_Tokens_Aceptados'
    with open(nombre + '.html', 'w') as html:
        html.write('<html>')
        html.write('    <head>')
        html.write('        <title>Reporte Tokens Aceptados</title>')
        html.write('        <link rel="stylesheet" type="text/css" href="estilo_TK.css">')
        html.write('    </head>')
        html.write('    <body >')
        html.write('        <h1><span class="blue"></span>Reporte<span class="blue"></span> <span class="yellow"> Tokens</span></h1>')
        html.write('        <h2> Analisis <a href="http://pablogarciafernandez.com" target="_blank">Lexico</a></h2>')
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