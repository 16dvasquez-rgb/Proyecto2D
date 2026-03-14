#Crear una clase figura , que tenga de metodos getArea , y crear 3 subclases, triangulo, circulo y rectangulo, las cuales van a tener su propio metodo getArea() 
import math

class Figure():
    def __init__(self):
        pass

    def getArea(self):
        pass
    
class Rectangle(Figure):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width*self.height
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.side = side

    def getArea(self):
        return super().getArea()
    
    def getArea(self):
        return self.side**2
    
class Triangle(Figure):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def getArea(self):
        return self.base*self.height/2

class Circle(Figure):    
    def __init__(self,radio):
        self.radio = radio

    def getArea(self):
        return self.radio*self.radio*math.pi
    
Coin = Circle(radio=2)
SandwichBread = Square(side=4)
Pizza = Triangle(base=3, height=4)
ChocolateBar = Rectangle(width=4,height=3)

#hacer una listra con las 4 varaiblers que creaste y ejecutar por cada una de ellas usando un for getArea()
shapelist = [Coin,SandwichBread,Pizza,ChocolateBar] 

def ShapePrinter(shapelist):
    for item in shapelist:
        if item.getArea()<12:
            print(item.getArea(),"es menor que 12")
        elif item.getArea()>12:       
            print(item.getArea(),"es mayor que 12")
        else:
            print(item.getArea(),"es igual a 12")

ShapePrinter(shapelist)