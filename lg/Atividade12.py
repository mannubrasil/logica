idade1=float(input("digite um número"))
if idade1>=0 and idade1<=12:
    print("criança")
elif idade1>=13 and idade1<=17:
    print("adolescente")
elif idade1>=18 and idade1<=59:
    print("adulto")
else:
    print("idoso")