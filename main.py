#Ejercicio 1. Constructores. Programacion basada en objetos
#========================================================================================================
#Cada vez que creamos un objeto de esa clase, la definicion del constructor es la primera en ejecutarse. 
# La forma de inicializar el valor de un atributo de clase sin un constructor
#========================================================================================================

class three:
    val=7

Constructor __init__(self)

#========================================================================================================
#Tambien podemos hacer esto dentro de las funciones de clase
#========================================================================================================
class three:
    def func(self,val):
        self.val=val
t=three()
t.func(8)
t.val

t.func(6) #also lets us re-initialize attibutes
t.val

#========================================================================================================
#O podemos pedirle informacion al usuario.
#========================================================================================================

class three:
    def __init__(self): #al momento de invocar la clase, se inicializa la funcion
        self.val=input("What value?")
t=three()
t.val
#========================================================================================================
#Creacion de objetos:
#__new__ es un metodo de clase estatica que nos permite controlar la creacion de objetos. 
# Cada vez que hacemos una llamada al constructor de la clase, realiza una  llamada a __new__.
# Si bien esta es una funcion predeterminada para cada clase, definitivamente podemos jugar con ella.
#========================================================================================================

class demo:                 
    def __new__(self):      #inicializador __new__ (el otro inicializador es __init__)
        return 'dataflair'
d=demo()                    # invocamos a la clase demo
type(d)

#========================================================================================================
#Tambien podemos crear un nuevo atributo exclusivamente para este objeto y leerlo al definir valores.
#No hay mucho que pueda hacer una vez que ya haya definido el objeto.
#========================================================================================================

kumquat.color='orange'
print("I am ",kumquat.color)

#========================================================================================================
#Entonces,?Que sucede cuando no proporcionamos explicitamente un constructor para una clase?
#Puede python manejarlo? Por que no lo intentamos?
#========================================================================================================

class color:
    def show(self):
        print("You can see me")
orange=color()
orange.show()

#========================================================================================================
#Un constructor que Python nos presta cuando olvidamos incluir uno.
#Este no hace absolutamente nada sino crea una instancia del objeto; es un constructor vacio, sin cuerpo.
#========================================================================================================

class demo:
    def show(self):
        print("Thank you for instantiating me :)")
d=demo()
d.show()

class demo:
    def __init__(self):
        print("Thank you for instantiating me :)")
d=demo()

#========================================================================================================
#Si le da mas de un constructor, eso no conduce a la sobrecarga del constructor en Python
#========================================================================================================
class one:
    def __init__(self):
        print("First constructor")
    def __init__(self):
        print("Second constructor")
o=one()

class one:
    def __init__(self,a=1,b=2):
        print(a+b)
o=one(2)

#========================================================================================================
#Tipico fragmento de codigo que se usa en la programacion basada en objetos
#========================================================================================================
class Mi_Clase:
    Saludos="
    def __init__(self,Nombre="todos"): #funcion 'init' Inicia el atributo 1
        self.Saludos=Nombre+"!"
    def Di_Hola(self):                 #atributo 2
        print("Hola a {0}".format(self.Saludos))