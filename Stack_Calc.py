from Stack import *
import re
from re import split
from graphviz import Digraph
from graficador import *

#SE REALIZARAN LAS OPERACIONES
def operation(left,token,right):
    a = float(right)
    b = float(left)

    if token == "+":
        return a + b
    elif token == "-":
        return a - b
    elif token == "*":
        return a * b
    elif token == "/":
        return a / b
    elif token == "%":
        return a % b
    else:
        return -1

# AGREGA LOS ELEMENTOS A LA PILA
def insert_in_stack(line,hover):  
    ent = " ".join(line)
    out = ent.replace("(","")
    print(">>Su entrada en POSTFIJO es: " + out) 
    print(">>Generando resultado...")
    myStack = Stack()
    left = ""
    right = ""
    
    sumador = -1
    tope = len(line)

    for token in line:
        tope = tope-1
        if(token!="("):
            if (token == "+") or (token == "-") or (token == "/") or (token == "*") :
                    left = myStack.pop()
                    right = myStack.pop()
                    resultado = operation(left,token,right)
                    myStack.push(resultado)
                    sumador +=1
            else:
                    myStack.push(token)
    
    
    print(">>El resultado es: " + str(myStack.pop()))
    print("")
    print("Presione cualquier tecla para regresar al inicio")

    if hover==1:
        ir = str(input())
        if input!=None:
            take_name()


def optioner():
    print(">>Ingrese exit para regresar al menú principal")
    clave = str(input())
    if clave == "exit":
        take_name()      
    else:
        optioner()


def insert_with_graph(line):  
    ent = " ".join(line)
    out = ent.replace("(","")
    print("Su entrada en POSTFIJO es: " + out) 
    print("Generando gráfica y resultado...")
    myStack = Stack()
    left = ""
    right = ""
    
    sumador = -1
    tope = len(line)

    for token in line:
        tope = tope-1
        if(token!="("):
            if (token == "+") or (token == "-") or (token == "/") or (token == "*") :
                    left = myStack.pop()
                    right = myStack.pop()
                    resultado = operation(left,token,right)
                    myStack.push(resultado)
                    sumador +=1
                    concatenador(myStack.get_elements(),sumador,tope)
            else:
                    myStack.push(token)
                    concatenador(myStack.get_elements(),sumador,tope)
    
    print("El resultado es: " + str(myStack.pop()))
    print("")
    optioner()

#FUNCION DE FACTORIAL
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
#FUNCION DE RAIZ CUADRADA
def quarter(num):
    return pow(num,(1/2))

#FUNCION PARA CONVERTIR LAS PALABRAS RESERVADAS A FLOTANTES E INGRESARLOS A LISTA
def convert_the_line(line,option,hover):
    #PALABRAS RESERVADAS
    res_uno = r"Pow"
    res_dos = r"Fact"
    res_tres = r"Sqrt"
    pat = "[\D]+\]+"

    i=-1
    print(line)
    
    result = 0
    for token in line:
        i+=1 
        
        if (re.match(res_uno, token)) or (re.match(res_dos, token)) or (re.match(res_tres, token)) or (re.match(pat, token)) : 
            numbers = split('\D+',line[i])
            if(re.match(res_uno,token)):
                result = pow(float(numbers[1]),float(numbers[2]))
                line[i] = str(result)
            elif(re.match(res_dos,token)):
                line[i] = str(factorial(float(numbers[1])))
            elif(re.match(res_tres, token)):
                line[i] = str(quarter(float(numbers[1])))

    if option==1:
        insert_in_stack(line,hover)
    elif option==0:
        insert_with_graph(line)

def importancia(char):
     if (char == "+"):
        return 0
     elif (char == "-"):
        return 0
     elif (char == "*"):
        return 1
     elif (char == "/"):
        return 1
     elif (char == "("):
        return 2



 #FUNCION PARA CONVERSION POSTFIJA
def toPost(list,option,hover):
    strLine = "".join(list)
    ad = len(list) #VARIABLE PARA PODER VACIAR LA PILA CUANDO LLEGUE AL FINAL
    
    #LISTA PARA GUARDAR LOS SIGNOS
    stack = Stack()
    #LISTA PARA ALMACENAR LOS DATOS ORDENADOS EN NOTACION POSTFIJA
    transformed = [] 

    g = 0
    e = -1

    strin = ""

    for i in list:
        ad = ad -1 
   
        if (i == "+") or (i == "-") or (i == "/") or (i == "*") or (i=="("):
           stack.push(i)
           
           if(  (importancia(stack.get_element(e)) == importancia(stack.get_element(e+1)) == 2)):
                   stack.pop()
                   e = e-1
           if((stack.get_Size()>1) and (importancia(stack.get_element(e)) >= importancia(stack.get_element(e+1)))):
               if(stack.get_element(e-1)=="("):
                   stack.destroyer(e-1)

               stack.pop()
               transformed.append(stack.pop())
               stack.push(i)
               
           else:
               e+=1
           
        elif (i!="(") and (i!=")"):
           transformed.append(i)

        if (i==")"):
           transformed.append(stack.pop())
           e = -1

    while(stack.get_Size()!=0):
        transformed.append(stack.pop())

        convert_the_line(transformed,option,hover)
  
    
def pre_to_post(list,hover):

        pila = Stack()

        postfija = []

        count = -1 

        apilador = 0

        for i in list:
            count+=1


            if (i == "+") or (i == "-") or (i == "/") or (i == "*") or (i=="("):
                pila.push(i)  
            else:
                postfija.append(i)

                    
            if len(postfija)>2 :
                if (postfija[0] != "+") and (postfija[0] != "-") and (postfija[0] != "/") and (postfija[0] != "*") and (postfija[1] != "+") and (postfija[1] != "-") and (postfija[1] != "/") and (postfija[1] != "*") and (postfija[2] != "+") and (postfija[2] != "-") and (postfija[2] != "/") and (postfija[2] != "*"):
                    apilador+=1
            
            if (list[count] != "+") and (list[count] != "-") and (list[count] != "/") and (list[count] != "*") and (list[count -1] != "+") and (list[count -1] != "-") and (list[count -1] != "/") and (list[count -1] != "*"):
                    postfija.append(pila.pop())  
                    apilador +=1

            if apilador>1:
                postfija.append(pila.pop()) 
                apilador = 0
                

        while(pila.get_Size()!=0):
            postfija.append(pila.pop())  

        postfija = [x for x in postfija if x is not None]


        convert_the_line(postfija,1,hover)



#SE REALIZARAN LAS OPERACIONES
def operation(left,token,right):
    a = float(right)
    b = float(left)

    if token == "+":
        return a + b
    elif token == "-":
        return a - b
    elif token == "*":
        return a * b
    elif token == "/":
        return a / b
    elif token == "%":
        return a % b
    else:
        return -1



#FUNCION PARA EL TIPO DE NOTACION
def identify(line,hover):
   word = line.split()

   if  word[0] == 'POST:':
       word.pop(0)
       convert_the_line(word,1,hover)

       
   elif word[0] == 'PRE:':
       print("hay un pre")
       word.pop(0)
       pre_to_post(word,hover)

   elif word[0] == 'IN:':
       word.pop(0)
       toPost(word,1,hover)

#FUNCION ENCARGADA DE LA LECTURA DE ARCHIVOS
def lector(path):
       try:
        file = open(path, "r")
        lines_list = (file.readlines())
        hover = len(lines_list)
        for i in range(len(lines_list)):
            hover = hover-1
            if lines_list[i] != '\n':
                identify(lines_list[i],hover)
         
        file.close()
        
       except:
        print("ingrese una ruta válida")
        take_name()


def go_to_graphic():
    print("Ingrese su expresion Infija")
    infija = str(input()).split()
    try:
     toPost(infija,0,0)
    except:
        print("Ingrese una entrada válida")
        go_to_graphic()

 
#FUNCION DE MENU
def take_name():
    print("***********************************************")
    print("Lenguajes formales y de programación sección:A-")
    print("*    Gerson Aaron Quinia Folgar 201904157     *")
    print("***********************************************")
    print("**************Eliga una opción*****************")

    print("1. Cargar Archivo")
    print("2. Graficar Operación")
    print("3. Salir ")

    option = int(input())

   
    if option == 1:
        print("Ingrese la ruta del archivo")
        path = str(input())
        lector(path)
        
    elif option == 2:
        go_to_graphic()

    elif option == 3:
        print("Finalizó la aplicación :)")
    else:
        print("")
        print("Por favor Eliga una opción válida")
        take_name()

if __name__=='__main__':
    take_name()  



