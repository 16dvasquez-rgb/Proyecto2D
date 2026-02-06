#Crear una funcion que reciba 3 numeros y me retorne el mayor de ellos
def NumberReturn(number1, number2, number3):
    if (number1 > number2) and number1 > number3:   
        return number1
    elif (number2 > number1) and number2 > number3:
        return number2
    elif (number3 > number2) and number3 > number1:
        return number3
    else: 
        return number1  


#print (NumberReturn(1,1,1))
#Crear una funcion que reciba 1 numero y me diga si es unidad, decena, o centena, si es mayor o igual que mil no hacer nada
def NumberUnitCalculator(mynumber):
    if mynumber <10:
        print ("tu numero es unidad")
    elif mynumber <100 and mynumber >=10: 
        print ("tu numero es decena")
    elif mynumber <1000 and mynumber >=100:
        print ("tu numero es centena")
    elif mynumber >=1000:
        return

#NumberUnitCalculator(-50)

# Crear una funcion que reciba una lista de numeros y solo imprima los mayores a 100

def numberPrinter(list):
    for n in list:
        if n >100:
            print(n)
    
# listadeprueba = [1,240,222,400]
# numberPrinter(listadeprueba)
# Crear una funcion que reciba 1 numero y me retorne ese numero al cuadrado 
def numbersquared(number):
   return number*number

print (numbersquared(4)) 

# 4^2 = 4*4 ; 5^3 = 5*5*5 ; 10^3 :; n^m

#FUNCION QUE ME PERMITA MULTIPLICAR UNA N CANTIDAD DE VECES UN NUMERO POR SI MISMO es decir 
# n*n*n*n*n*n*n*n*n

def numberspower(number,power):
    NumberSaver = 1
    for i in range (power):
        print (i)
        NumberSaver = number*NumberSaver
    return NumberSaver

print(numberspower(5,3)) #number*number*number*number*number


