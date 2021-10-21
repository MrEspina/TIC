def sustituye_vocales1():
    palabra=raw_input("PALABRA: ")
    x=raw_input("Que letra quieres poner: ")
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            print(x)
        else:
            if(palabra[cont]=='e'):
                print(x)
            else:
                if(palabra[cont]=='i'):
                    print(x)
                else:
                    if(palabra[cont]=='o'):
                        print(x)
                    else:
                        if(palabra[cont]=='u'):
                            print(x)
                        else:
                            print(palabra[cont])
        cont=cont+1
    print("Palabra transformada: "+palabra)
sustituye_vocales1()
