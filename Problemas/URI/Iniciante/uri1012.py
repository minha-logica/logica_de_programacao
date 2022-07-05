def strToFloat(list_str):
    list_float = []
    for s in list_str:
        list_float.append(round(float(s), 2))
    return list_float
PI = 3.14159
a, b, c = strToFloat(input().split())
print("TRIANGULO: %.3f" %((a*c)/2))
print("CIRCULO: %.3f" %(PI*(c**2)))
print("TRAPEZIO: %.3f" %(((a+b)*c)/2))
print("QUADRADO: %.3f" %(b**2))
print("RETANGULO: %.3f" %(a*b))