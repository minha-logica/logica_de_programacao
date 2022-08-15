"""
Esta função realiza a soma de cada digito 
elevado ao quadrado de um número inteiro positivo.
Exemplos: 
    Para n = 13, soma = 1^2 + 3^2 = 10
    Para n = 21, soma = 2^2 + 1^2 = 5
"""
def soma_quadrado_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        numero = numero // 10 
        soma  += digito ** 2
    return soma
"""
Esta função retorna True se um número inteiro positivo 
é Feliz e retorna False se o número é Infeliz.
"""
def e_feliz(numero):
    sequencia = []
    soma = 0
    while soma != 1:
        soma = soma_quadrado_digitos(numero)
        if soma in sequencia:
            return False
        sequencia.append(soma)
        numero = soma
    return True
n = int(input())
if e_feliz(n):
    print("%s é feliz" %n)
else:
    print("%s é infeliz" %n)