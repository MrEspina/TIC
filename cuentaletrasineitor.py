def cuentaletrasineitor():
    palabra=raw_input("PALABRA: ")
    x=0
    y=0
    z=0
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            x=x+1
        else:
            if(palabra[cont]=='e'):
                x=x+1
            else:
                if(palabra[cont]=='i'):
                    x=x+1
                else:
                    if(palabra[cont]=='o'):
                        x=x+1
                    else:
                        if(palabra[cont]=='u'):
                            x=x+1
                        else:
                            y=y+1
        cont=cont+1
    z=x+y
    print("Hay "+str(x)+" vocales.")
    print("Hay "+str(y)+" conconantes.")
    print("En total son "+str(z)+" letras.")
cuentaletrasineitor()
