def calculadora_2():
            print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
            print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
            print("/\     1=suma                   /\ ")
            print("\/     2=resta                  \/")
            print("/\     3=producto               /\ ")
            print("\/     4=fraccionamiento        \/")
            print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
            print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
def erroneo():
    print("ERRONEO, COMO TU")
def suma(x,y):
    rta=x+y
    print("Resulta ser: "+str(rta))
def resta(x,y):
    rta=x-y
    print("Resulta ser: "+str(rta))
def mult(x,y):
    rta=x*y
    print("Resulta ser: "+str(rta))
def div(x,y):
    rta=x/y
    print("Resulta ser: "+str(rta))
def calculadora():
        error=0
        while(error==0):
                op=0
                x=input("introduce una cifra: ")
                y=input("introduce otra cifra: ")
                calculadora_2()
                z=input("realizaremos un(a): ")
                if(y==0 and z==4):
                    error=1
                    erroneo()
                else:
                    if(z==1):
                        suma(x,y)
                    else:
                        if(z==2):
                            resta(x,y)
                        else:
                            if(z==3):
                                mult(x,y)
                            else:
                                if(z==4):
                                    div(x,y)
                                else:
                                       print("m*a en el chat")
                error=1
calculadora()
