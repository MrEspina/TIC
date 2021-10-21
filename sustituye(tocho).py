def sustituye_vocales2():
    palabra=raw_input("PALABRA: ")
    x=raw_input("Que letra quieres poner: ")
    new=""
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            print(x)
            new=new+x
        else:
            if(palabra[cont]=='e'):
                print(x)
                new=new+x
            else:
                if(palabra[cont]=='i'):
                    print(x)
                    new=new+x
                else:
                    if(palabra[cont]=='o'):
                        print(x)
                        new=new+x
                    else:
                        if(palabra[cont]=='u'):
                            print(x)
                            new=new+x
                        else:
                            print(palabra[cont])
                            new=new+palabra[cont]
        cont=cont+1
    print(new)
    print("Palabra transformada: "+palabra)

sustituye_vocales2()


