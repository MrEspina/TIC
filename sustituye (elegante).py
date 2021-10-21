def sustituye_vocales2():
    palabra=raw_input("PALABRA: ")
    x=raw_input("Que letra quieres poner: ")
    new=""
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            new=new+x
        else:
            if(palabra[cont]=='e'):
                new=new+x
            else:
                if(palabra[cont]=='i'):
                    new=new+x
                else:
                    if(palabra[cont]=='o'):
                        new=new+x
                    else:
                        if(palabra[cont]=='u'):
                            new=new+x
                        else:
                            new=new+palabra[cont]
        cont=cont+1
    print("Palabra transformada: "+palabra)
    print(new)


sustituye_vocales2()


