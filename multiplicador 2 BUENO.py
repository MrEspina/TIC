def multiplicador_2():
    x=0
    a=input("Que tabla quieres ver")
    print("---------------")
    print("---- TABLA ----")
    print("---- DEL "+str(a)+" ----")
    print("---------------")
    while(x<11):
        print(str(a)+"*"+str(x)+" = "+str(x*a))
        x=x+1
multiplicador_2()
