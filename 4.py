estados = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Espirito Santo", "Outros"]
faturamento = [6783643, 3667866, 2622988, 2716548, 1984953]
soma = 0
for i in faturamento:
    soma += i
for k in faturamento:
    x = faturamento.index(k)
    print("O estado de {} teve uma porcentagem de {:.1f}".format(estados[x], k/soma))