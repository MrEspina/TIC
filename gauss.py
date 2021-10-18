def gauss():
    a=input("Hasta que numero quierews que cuente:")
    acum=0
    for cont in range (1,a+1) :
        acum=acum+cont
        print (str(cont) +" acum= "+str(acum))
gauss()
