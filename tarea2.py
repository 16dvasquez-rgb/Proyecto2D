#crear una funcion que reciba una lista de letras y te las devuelva juntas en una sola palabraS
def WordMixer (wordlist):
    finalword = ""
    for letter in wordlist:
        finalword= finalword+letter 
    return finalword
# print (WordMixer(["a","k","c"]))
#crea una funcion que reciba una lista de numeros y que imprima cuantos son pares y cuantos son impares                           
def EvenAndOddCounter(numberlist):
    even = 0
    odd = 0
    for number in numberlist:
        if number% 2 == 0:
            even+=1
        else:
            odd+=1
    print ("tienes",even,"pares")
    print ("tienes",odd,"impares")


# EvenAndOddCounter([10,20,8,4,6])

import math

def quadratic(a,b,c):
    delta = b**2 -4*a*c 
    if delta <0:
        print("no se puede resolver")
        return

    DeltaSqrt = math.sqrt(delta)
    alfaPlus = (-b + DeltaSqrt) /2*a
    AlfaMinus =(-b - DeltaSqrt) /2*a
    return [alfaPlus,AlfaMinus]    
    

print (quadratic(1,0,-2))