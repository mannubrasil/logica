n1=int(input("digite um número"))
n2=int(input("digite um número"))
n3=int(input("digite um número"))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
    print("o maior número é:",maior)
