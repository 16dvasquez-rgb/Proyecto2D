#Crea una funcion que convierta metros a pies. ingresas metros y devuelve pies
class UnitConverter:
    def MeterToFeet(self):
        meter = float (input("ingresa los metros aqui"))
        feet = 3.28084
        return meter*feet 
    def FeetToMeter(self):
        feet = float (input("ingresa los pies aqui"))
        meter = 3.28084
        return feet/meter
    def MilesToKilometers(self):
        miles = float (input("ingresa las millas aqui"))
        kilometer = 1.60934
        return miles*kilometer
    def KilometersToMiles(self):
        kilometers = float (input("ingresa los kilometros aqui"))
        miles = 1.60934 
        return kilometers/miles
    def KilosToPounds(self):
        kilos = float (input("ingresa los kilos aqui"))
        pounds = 2.20462
        return kilos*pounds
    
converter = UnitConverter()


#crear una clase que convierta unidades cuadraticas o de area y unidades cubicas y de volumen      

class QuadraticUnitConverter:

    @staticmethod
    def SquareMeterToSquareYard(            ):
        SquareMeter = float (input("ingreas los metros cuadrados aqui"))
        SquareYard = 1.19599
        return SquareMeter*SquareYard

print (QuadraticUnitConverter.SquareMeterToSquareYard())

# class Enemy():
#     @staticmethod
#     def revivir

#     def attack
#     def ultimate
#     def avoid

# zombie = Enemy()
# zombie = Enemy()
# zombie = Enemy()
# zombie = Enemy()
# zombie = Enemy()
# zombie = Enemy()
# zombie = Enemy()

# Enemy.killAll()

class CubicUnitConverter:

    @staticmethod
    def CubicMeterToCubicFeet():
        CubicMeter = float (input("ingreas los metros cubicos aqui"))
        FeetMeter = 35.3147
        return CubicMeter*FeetMeter
    
print (CubicUnitConverter.CubicMeterToCubicFeet())