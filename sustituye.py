def sustituye_vocales():
    palabra=raw_input("PALABRA: ")
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            print('u')
        else:
            if(palabra[cont]=='e'):
                print('u')
            else:
                if(palabra[cont]=='i'):
                    print('u')
                else:
                    if(palabra[cont]=='o'):
                        print('u')
                    else:
                        print(palabra[cont])
        cont=cont+1
    print("Palabra transformada: "+palabra)
sustituye_vocales()
