maior = 0
pos = 0
posfinal = 0
with open("dados.txt", "r") as arq:
    for linha in arq:
        atual = int(linha)
        if(atual > maior):
            maior = atual
            posfinal = pos
        pos += 1
print(str(maior) + "\n" + str(posfinal))