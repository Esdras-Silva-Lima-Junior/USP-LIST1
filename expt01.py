#Neste programa você insere uma quantidade de segundos e ele converterá para quantos dias, horas, minutos e segundos aquela quantidade de segundos antes digitada irá valer.

#Criando entrada de dados e variaveis que irão fazer o calculo e guardarão os resultados finais:
segundos_total = int(input("Qual a quantidades de segundos que deseja converter: "))
a = segundos_total // 86400
b = (segundos_total // 3600) % 24
resto_segs = segundos_total % 3600
c = resto_segs // 60
d = resto_segs % 60

#Mostrando na tela o resultado final:
print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
#Fimse :D