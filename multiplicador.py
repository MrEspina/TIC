def multiplicador():   
    a=input("que tabla deseas: ")
    print("----------------------------")
    print("--------TABLA DEL "+str(n)+"--------")
    print("----------------------------")
    for cont in range (0,11):
          print(" "+str(a)+" x "+str(cont)+" = "+str(cont*a))             
multiplicador()
