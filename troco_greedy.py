moedas = (1,2,5,10)
# moedas = (1,3,4)
V = 6
# Valor otimo: 3 10 + 10 + 5

def troco(valor):
    num_moedas = 0
    i = len(moedas) - 1
    while valor:
        moeda = moedas[i]
        if moeda > valor:
            i -= 1
        else:
            valor -= moeda
            num_moedas += 1
    return num_moedas

r = troco(V)
print(r)
