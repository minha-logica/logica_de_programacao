def menor_maior(a, b, c):
    menor = (a+b-abs(a-b) + 2*c - abs(a+b-abs(a-b)-2*c))//4
    maior = (a+b+abs(a-b) + 2*c + abs(a+b+abs(a-b)-2*c))//4
    return menor, maior
n1 , n2 = menor_maior(int(input()),int(input()), int(input())) 
print(n1, n2)