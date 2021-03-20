from graphviz import Digraph
import operator
def un(Base):
    # -------------------------------------------------
    nombre_del_Restaurante = Base[0]
    Nombre_Seccion = Base[1]
    Lista_Seccion = Base[2]
    # -------------------------------------------------
    #print('-----------------Generar Grafica-------------------------')
    dot = Digraph(comment='Grafica Restaurante')
    dot  # doctest: +ELLIPSIS
    #print(nombre_del_Restaurante)
    dot.node('A', str(nombre_del_Restaurante))
    # -------------------------------------------

    Lista_Seccion.sort(key=lambda p: p['numero'])
    #for m in Lista_Seccion:
    #    print(m)
    # -------------------------------------------
    i=0
    o=0
    for x in Nombre_Seccion:
        i = i + 1
        aux1 = chr(66 + i)
        dot.node(str(aux1), label= r''+str(x)+'')
        dot.edges(['A'+str(aux1)])
        #print(x)
        for z in Lista_Seccion:
            if z['seccion'] == x:
                o =o+1
                Numero = float(z['numero'])
                aux2 = chr(96+o)
                #des = z['nombre']+" Q."+str("{:.2f}".format(Numero)+" \n"+z['descripcion'])
                dot.node(str(aux2),label= r''+z['nombre']+" Q."+str("{:.2f}".format(Numero)+ ' '+z['descripcion']+''))

                #dot.node(str(aux2),label= r'centro\nSal')
                dot.edges([str(aux1)+str(aux2)])
    # -------------------------------------------------
    #print(dot.source)
    #print("------------------------------------------------------")
    dot.render('Grafica/Grafica_Salida.dot', view=True)  # doctest: +SKIP
    'Grafica/Grafica_Salida.dot.pdf'