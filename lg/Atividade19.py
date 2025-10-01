n1=float(input("digite seu peso:"))
n2=float(input("digite sua altura:"))
peso = n1/n2**2
if peso<=18.5:
    print("abaixo do peso")
elif peso < 25:
    print("peso normal")
elif peso < 30:
    print("sobrepeso")
else:
    print("obesidade")