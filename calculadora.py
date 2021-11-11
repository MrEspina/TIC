def calculadora():
        error=0
        while(error==0):
                op=0
                x=input("introduce una cifra: ")
                y=input("introduce otra cifra: ")
                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
                print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
                print("/\     1=suma                   /\ ")
                print("\/     2=resta                  \/")
                print("/\     3=producto               /\ ")
                print("\/     4=fraccionamiento        \/")
                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
                print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
                z=input("realizaremos un(a): ")
                if(y==0 and z==4):
                    error=1
                else:
                    if(z==1):
                        op=x+y
                        print("la suma resulta ser: "+str(op))
                    else:
                        if(z==2):
                            op=x-y
                            print("la resta resulta ser: "+str(op))
                        else:
                            if(z==3):
                                op=x*y
                                print("el producto resulta ser: "+str(op))
                            else:
                                if(z==4):
                                    op=float(x)/y
                                    print("el fraccionamiento resulta ser: "+str(op))
                                else:
                                       print("m*a en el chat")
                error=1
calculadora()
        


