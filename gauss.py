def gauss():
    a=input("Hasta que numero quieres que sume los anteriores :")
    acum=0
    for cont in range (1,a+1) :
        acum=acum+cont
        print (str(cont) +" acum= "+str(acum))
gauss()
