#Este programa tem o papel de saber qual número está na casa das dezenas de um número digitado.

#Criando a entrada de dados e a variavel que irá fazer o calculo e guardar os resultados:
number = int(input("Digite um número inteiro: "))
result = (number // 10) % 10

#Mostrando na tela o resultado:
print("O dígito das dezenas é", result)
#Fim-se