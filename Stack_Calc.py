from Stack import *
import re
from re import split

print("***********************************************")
print("Lenguajes formales y de programación sección:A-")
print("*    Gerson Aaron Quinia Folgar 201904157     *")
print("***********************************************")
print("**************Eliga una opción*****************")

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
def insert_in_stack(line):  
    print("Su entrada en POSTFIJO es: " + "".join(line))
    myStack = Stack()
    left = ""
    right = ""

    for token in line:
        if (token == "+") or (token == "-") or (token == "/") or (token == "*") or (token == "%"):
                left = myStack.pop()
                right = myStack.pop()
                resultado = operation(left,token,right)
                myStack.push(resultado)
        else:
                myStack.push(token)
    print(myStack.pop())
    print("")
    

def convert_line(line):
    #PALABRAS RESERVADAS
    res_uno = r"Pow"
    res_dos = r"Fact"
    res_tres = r"Sqrt"
    i=-1
    for token in line:
        i+=1
        if (re.match(res_uno, token)) or (re.match(res_dos, token)) or (re.match(res_tres, token)): 
            print(line[i])
            numbers = split('\D+',line[i])
            result = pow(float(numbers[1]),float(numbers[2]))
            line[i] = str(result)

    insert_in_stack(line)

#FUNCION PARA EL TIPO DE NOTACION
def identify(line):
   word = line.split()

   if  word[0] == 'POST:':
       word.pop(0)
       #insert_in_stack(word)
       convert_line(word)
       
   elif word[0] == 'PRE:':
       print("hay un pre")
   elif word[0] == 'IN:':
       print("hay un in")


#FUNCION ENCARGADA DE LA LECTURA DE ARCHIVOS
def lector(path):
       try:
        file = open(path, "r")
        lines_list = (file.readlines())

        for i in range(len(lines_list)):
         identify(lines_list[i])
         
        file.close()
       except:
        print("ingrese una ruta válida")
        take_name()
    
#FUNCION DE MENU
def take_name():
    print("1. Cargar Archivo")
    print("2. Graficar Operación")
    print("3. Salir ")

    option = int(input())
   
    if option == 1:
        print("Ingrese la ruta del archivo")
        path = str(input())
        lector(path)

    elif option == 2:
        print("funciona")
        take_name()
    elif option == 3:
        take_name()
    else:
        print("")
        print("Por favor Eliga una opción válida")
        take_name()


take_name()  


