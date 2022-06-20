import json

with open("dados.json") as dados_json:
    dados = json.load(dados_json)

soma = 0
maior = 0
dia = 0
media_Mensal = 0
contador = 0
#soma de todos os valores

for valor in dados:
    soma += valor["valor"]
    if valor["valor"] != 0:
        media_Mensal += 1

# maior valor
media = soma / media_Mensal
for maior_valor in dados:
    if maior_valor["valor"] > maior:
        maior = maior_valor["valor"]
        dia = maior_valor["dia"]
    if maior_valor["valor"] > media:
        contador += 1
print('O maior valor foi no dia {} com um faturamento de {:.4f}'.format(dia, maior))
# menor valor

dia = 0
menor = dados[0]["valor"]
for menor_valor in dados:
    if menor_valor["valor"] < menor and menor_valor["valor"] != 0:
        menor = menor_valor["valor"]
        dia = menor_valor["dia"]

print('O menor valor foi no dia {} com um faturamento de {:.4f}'.format(dia, menor))

print('A média mensal é de {:.4f}'.format(soma/media_Mensal))
print('O número de dias em que o faturamento foi maior que a média geral  ({:.1f}) foram de {} dias'.format(media,contador))

    
