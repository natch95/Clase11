#=================================================================
#Ejemplo2 de hacer una sobrecarga de un operador (suma, resta, etc)
#=================================================================

class itspower:
    def __init__(self,x): #inicializar un objeto 'x'
        self.x=x            #le da el atributo al objeto de ser igual a x.
    def __pow__(self,other):  #pow es una funcion integrada dentro de python, por eso podemos usarla como un inicializador
        return self.x**other.x

a=itspower(2)
b=itspower(10)
resultado=a**b
print(resultado) #usando a=2 y b=10 el resultado va a ser 1024. 2 elevado a la 10

#=================================================================
#Ejemplo 3. Funciones recursivas. Le permite dividir una tarea en subtareas
#=================================================================
def factorial(n): #funcion 'factorial' que recibe el parametro 'n'
    f=1
    while n>0:
        f*=n        #toma el valor n y lo multiplica
        n-=1        #toma 'n' y le quita un numero
    print(f)
factorial(4)        #valor de entrada del ciclo es '4'

#=================================================================
#Ejemplo 4
#=================================================================
def factorial(numero):
    print("Valor inicial ->",numero)    #imprime un texto para mostrar el numero
    if numero>1:
        numero=numero*factorial(numero -1)
    print("valor final ->",numero)
    return numero
print (factorial(5))


    