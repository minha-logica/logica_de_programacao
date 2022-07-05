def toFloat(m):
    n = []
    for x in m:
        n.append(float(x))
    return n
def dp(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
x1, y1 = toFloat(input().split())
x2, y2 = toFloat(input().split())
print("%.4f" %dp(x1, y1, x2, y2))