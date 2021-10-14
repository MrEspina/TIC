def saludador ():
    a=input("Elige el primer numero: ")
    b=input("Elige el segundo numero: ")
    c=input("Si quieres sumar pulse 1, si quiere restar pulse 2, si quiere multiplicar pulse 3, si quiere dividir pulse 4: ")
    if c==1:
        print(a+b)
    if c==2:
        print(a-b)
    if c==3:
        print(a*b)
    else:
        print(a/b)
saludador()
