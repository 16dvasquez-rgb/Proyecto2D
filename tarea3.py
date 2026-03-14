class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def greet(self):
        print("hola mi nombre es", self.name)


# Lista estática de 100 instancias
lista_personas = [
    Person("Juan", "García", 25),
    Person("María", "Rodríguez", 30),
    Person("Carlos", "López", 22),
    Person("Ana", "Martínez", 28),
    Person("Luis", "Pérez", 35),
    Person("Elena", "Sánchez", 24),
    Person("Diego", "González", 29),
    Person("Lucía", "Gómez", 31),
    Person("Pedro", "Fernández", 40),
    Person("Sofía", "Díaz", 27),
    Person("Javier", "Álvarez", 33),
    Person("Marta", "Romero", 21),
    Person("Andrés", "Vázquez", 26),
    Person("Paula", "Castro", 32),
    Person("Marcos", "Ortiz", 38),
    Person("Sara", "Blanco", 23),
    Person("Raúl", "Gil", 45),
    Person("Clara", "Ramírez", 19),
    Person("Hugo", "Torres", 20),
    Person("Irene", "Flores", 34),
    Person("Fernando", "Morales", 42),
    Person("Julia", "Suárez", 25),
    Person("Ricardo", "Delgado", 37),
    Person("Rosa", "Salazar", 50),
    Person("Óscar", "Navarro", 31),
    Person("Alicia", "Mendoza", 29),
    Person("Víctor", "Castillo", 28),
    Person("Beatriz", "Rivera", 36),
    Person("Rubén", "Guzmán", 41),
    Person("Leticia", "Ramos", 22),
    Person("Iván", "Vargas", 27),
    Person("Gabriela", "Ríos", 30),
    Person("Felipe", "Ibarra", 44),
    Person("Mónica", "Paredes", 26),
    Person("Sergio", "Molina", 33),
    Person("Natalia", "Acosta", 24),
    Person("Manuel", "Ortega", 48),
    Person("Lorena", "Miranda", 35),
    Person("Adrián", "Soto", 22),
    Person("Valeria", "Reyes", 31),
    Person("Tomás", "Luna", 39),
    Person("Claudia", "Herrera", 28),
    Person("Gustavo", "Medina", 43),
    Person("Patricia", "Pascual", 32),
    Person("Emilio", "Cabrera", 25),
    Person("Isabel", "Muñoz", 27),
    Person("Ángel", "Vega", 34),
    Person("Silvia", "Fuentes", 29),
    Person("Joaquín", "Pinto", 46),
    Person("Daniela", "León", 23),
    Person("Cristian", "Márquez", 30),
    Person("Verónica", "Caballero", 38),
    Person("Roberto", "Cano", 41),
    Person("Andrea", "Vila", 26),
    Person("Ignacio", "Peña", 33),
    Person("Esther", "Hidalgo", 31),
    Person("Alejandro", "Falcón", 22),
    Person("Bárbara", "Guerrero", 35),
    Person("Samuel", "Gallardo", 28),
    Person("Rocío", "Manso", 24),
    Person("Francisco", "Santos", 47),
    Person("Gloria", "Prado", 36),
    Person("Jordi", "Crespo", 29),
    Person("Inés", "Soler", 21),
    Person("Julián", "Esteban", 32),
    Person("Nerea", "Parra", 25),
    Person("Mario", "Bravo", 40),
    Person("Lidia", "Garzón", 33),
    Person("César", "Maza", 27),
    Person("Noelia", "Calvo", 30),
    Person("Marcos", "Roldán", 42),
    Person("Olga", "Bernal", 34),
    Person("Saúl", "Arias", 28),
    Person("Rebeca", "Serrano", 29),
    Person("Mateo", "Lara", 23),
    Person("Ainhoa", "Vaca", 31),
    Person("Enrique", "Moya", 45),
    Person("Miriam", "Solís", 26),
    Person("Álvaro", "Guerra", 37),
    Person("Teresa", "Hervás", 52),
    Person("Rodrigo", "Rueda", 30),
    Person("Fátima", "Benítez", 24),
    Person("Gonzalo", "Vicente", 39),
    Person("Leire", "Cortes", 28),
    Person("Eloy", "Duran", 33),
    Person("Susana", "Bonilla", 41),
    Person("Arturo", "Expósito", 29),
    Person("Estefanía", "Marco", 22),
    Person("Damián", "Roca", 35),
    Person("Belén", "Rey", 31),
    Person("Alfredo", "Aguilar", 44),
    Person("Manuela", "Montes", 27),
    Person("Ivonne", "Zúñiga", 30),
    Person("Esteban", "Bermúdez", 38),
    Person("Ariadna", "Pardo", 25),
    Person("Félix", "Nieto", 43),
    Person("Aurora", "Arroyo", 26),
    Person("Israel", "Sanz", 32),
    Person("Blanca", "Escribano", 29),
    Person("Héctor", "Jiménez", 31),
]

#crear una funcion que reciba un ibjeto persona y si es mayor de 40 anios. la persona salude

def PersonGreet(person):
    if person.age >= 40:
       person.greet()
    else:
        print("soy menor a 40 años")

PersonGreet(lista_personas[0])
def ListPersonGreet(personlist):
    for person in personlist:
        PersonGreet(person)
    return     

#crear una funcion que reciba una lista de personas y me imprima cuantas son mayores a 40 a;os y cuantas son menores a 40 a;os y tambien cuantas tienen cuarenta, quiero tambien que me el nombre y apellido de la persona con mayor edad y el nombre de la persona con la menor edad, ademas del promedio de las edades

def listPersonAnalyser(lista_personas):
    OverForty = 0
    UnderForty = 0
    Forty = 0
    Addition = 0        
    oldestPerson = lista_personas[0]
    youngestPerson = lista_personas[0]

    for person in lista_personas:

        #Codigo para conteo de edades
        if person.age > 40:
            OverForty+=1
        elif person.age < 40:
            UnderForty+=1
        elif person.age == 40:
            Forty+=1

        Addition += person.age
    
        #codigo para mayor y menor de personas
        if oldestPerson.age <= person.age:
            oldestPerson = person
        if youngestPerson.age >= person.age:
            youngestPerson = person      

    quantity = len(lista_personas)

    mean = Addition/quantity

    print ("el promedio de edad es de",mean)
    print(OverForty,"tienen mas de cuarenta")
    print(UnderForty,"tienen menos de cuarenta")
    print(Forty,"tiene cuarenta")
    print (oldestPerson.name,oldestPerson.lastname,"es la mayor persona")
    print (youngestPerson.name,youngestPerson.lastname,"es la menor persona")

listPersonAnalyser(lista_personas)
