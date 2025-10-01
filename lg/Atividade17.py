n1=int(input("digite um número"))
n2=int(input("digite um número"))
if  n2 == 0:
    print("Não é possível dividir por zero.")
else:
    if n1 % n2 == 0:
        print("O primeiro número é divisível pelo segundo.")
    else:
        print("O primeiro número NÃO é divisível pelo segundo.")