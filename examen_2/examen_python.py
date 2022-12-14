## 1. Primer punto

myArreglo = [
    {"nombre": "Juan"},
    {"nombre": "Pedro"},
    {"nombre": "Gorge"},
    {"nombre": None}
]
resultado = list(map(lambda x: x["nombre"], myArreglo))

# 2. Lo que imprime es la c 4 [4], dado que las listas (Arreglos) son datos mutables 
# y cuando se ingresa a la función cambiar2,
# se le pasa es la referencia en memoria, y dentro este se altera el valor.
# En cambio int es un valor inmutable y dentro de cambiar1 se le pasa es es valor 
# por lo tanto no se altera el valor en memoría

# 3. 
import csv
suma = 0

with open("file.csv") as fin:
    headerline = fin.next()
    total = 0
    for row in csv.reader(fin):
        suma += int(row[1])

#9. Una clase, es la que establece como deben de ser los objectos, los atributos que tienen los métodos. 
# Puede verse como si mi objecto fuese una galleta y la clase el model de esta.
# Tambien los métodos puede variar, un método de clase, se puede ejecutar sin la necesidad de instanciar
# y solo puede cambiar valores de clase.
# Los atributos de clases se pueden usar como constante para todos mis metodos, ya que todos los objectos
# con este atributo de clase a puntan al mismo valor de memoría.

class Persona:  #Esta es mi clase
    Total = 0 # Este es un atributo de clase
    def __init__(self, nombre:str, color_ojos:str, color_pelo:str, edad:int) -> None: 
        """Aquí Están las instrucciones para crea una persona"""
        self.__nombre = nombre
        self.__color_ojos = color_ojos
        self.__color_pelo = color_pelo
        self.__edad = edad
        self.update_total()
    
    @property
    def nombre(self)->str: 
        """Este es el get de nombre, ya que mis valores son 'privados'"""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre:str):
        """Este es el setter de mi propiedad nombre"""
        self.__nombre = nombre
        
    
    @classmethod
    def update_total(cls):
        cls.Total += 1
    
fredy  =  Persona("Fredy", "Negro", "Castaño", 23)
fredy.nombre = "Alberto"

# 10 ¿A qué hacen referencia los conceptos de Herencia y Polimorfismo?
# La herencia en POO, es defirnir una nueva clase basadas en clases anteriores.
class SerVivo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def comer(self):
        print("Estoy Comiendo")

## Aquí mi clase Human, herada tanto los atributos como los métodos de servivo
class Human(SerVivo):
    def __init__(self, nombre, genero, sexo) -> None:
        super().__init__(nombre)
        self.__sexo = sexo
        self.__genero = genero
    
    def respirar(self):
        print("Yo respiro")
        
cell = SerVivo("cell")
print(cell.comer())

fredy = Human("Fredy", "Hombre", "Masculino")
print(fredy.respirar())
print(fredy.comer())

# El polimorfimos quiere decir que un objecto puede  ser accedido utilizando la misma interfaz (Un ancesentró en común)
# Por ejemplo una clase Perro que herada de Animal, en Java puede ser instanciado Animal animal = new Perro()
# Ahora si en la clase perro se sobre-escribe el método hablar, mi objecto animal.hablar() va a ejecutarse el de la clase Perro (Ligadura dinámica)

# El polimorfismo no está programado en python por el Duck Typing (No le importa el tipo siempre se va a ejecutar)
# Ya que por la tipado dinámico no va a tener comportamientos raros.


## Qué conoce de archivos .bat, de la consola CMD y de la consola de PowerShell (ps1)
# .bat se es conjunto de instrucciones que se ejecutan en Windows. Puede verse similar a Bash en Linux
# y Powershell es la consola de windows, aunque siendo honesto estoy más familiarizado con Linux.



