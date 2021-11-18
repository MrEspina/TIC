import random
def apuesta():
    ap1=0
    ap2=0
    print("---Primer  jugador---")
    for cont in range(1,4):
        num=random.randint(1,7)
        print(num)
        ap1=ap1+num
    print("El puntuaje del primer jugador es: "+str(ap1))
    print("---Segundo jugador---")
    for cont in range(1,4):
        num=random.randint(1,7)
        print(num)
        ap2=ap2+num
    print("El puntuaje del segundo jugador es: "+str(ap2))
    print("---------------------")
    if(ap1>ap2):
        print("gana el primer jugador.")
    else:
        print("Gana el segundo jugador.")
apuesta()

