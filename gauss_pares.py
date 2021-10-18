def gauss_pares():
    a=input("Hasta que numero quierews que cuente:")
    acum=0
    resto=0
    for cont in range (1,a+1) :
        resto= cont % 2
        if (resto==0):
            acum=acum+cont
        print (str(cont) +" acum= "+str(acum))
gauss_pares()
