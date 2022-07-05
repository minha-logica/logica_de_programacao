def strToInt(list_str):
    list_int = []
    for s in list_str:
        list_int.append(int(s))
    return list_int

def maior(a, b):
    return int(((a+b+abs(a-b))/2))

a, b, c = strToInt(input().split())
aux = maior(a,b)
aux = maior(aux,c)
print("%d eh o maior" %aux)