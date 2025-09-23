peso = int(input("Digite seu peso"))
altura = float(input("Digite sua altura"))
#Isso vai fazer o calculo do imc 
imc = peso / altura ** 2
valor = round(imc, 2)
if(imc < 18.5):
    print("Desnutrido", valor)
elif(imc < 24.9):
     print("Normal", valor)
elif(imc < 29.9):
     print("Excesso de peso", valor)
elif(imc < 34.9):
    print("Obsidade I", valor)
elif(imc < 39.9):
    print("Obsidade II", valor)
else:
    print("Obsidade III", valor)





