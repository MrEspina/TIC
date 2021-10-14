def multiplicar():
    a=input("Que tabla de multiplicar quieres ver: ")
    print("---------------")
    print("---- TABLA ----")
    print("---- DEL "+str(a)+" ----")
    print("---------------")
    for cont in range(0,11):
        print(str(cont)+"x"+str(a)+" = "+str(cont*a))
multiplicar()
