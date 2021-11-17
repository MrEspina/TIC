def mayor_10():
    y=input("CUANTOS VALORES CONTAMOS: ")
    x=0
    mayor=x
    for cont in range(1,y+1):
        x=input("PON UN NUMERO: ")
        if(x>mayor):
            mayor=x
        else:
            mayor=mayor
    print("EL MAYOR ES: "+str(mayor))
mayor_10()
