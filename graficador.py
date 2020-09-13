from graphviz import Digraph
import graphviz
from graphviz import Graph


f = Digraph(format='pdf', name='grafico')
f.attr(rankdir='TB', size='8')
f.attr(bgcolor='blue:cyan', fontcolor='white')
f.attr('node', shape='plaintext')


def concatenador(nodo,sumador,tope):

    creador = ""
    impr = ""

    for i in range (len(nodo)):
        newnode = str(nodo[i])
        if i != "]" and i !="[":
         impr = "<tr><td>" + newnode + "</td></tr>" + impr

    impr = "<<table>" + impr + "</table>>"
    creador = "p" + str(sumador)
    f.node(creador,impr)
    if tope == 0:
       f.view()



