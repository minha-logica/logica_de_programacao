def potencia(a, b): 
    somatorio = 1 
    for i in range(b):
        soma = 0 
        for j in range(a): 
            soma += somatorio
        somatorio = soma 
    return somatorio
print(potencia((int(input())),(int(input()))))