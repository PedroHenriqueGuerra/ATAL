def mediana(v1, v2, tam):
    median = tam // 2
    if tam == 1:
        if v1[median] == v2[median]:
            return v1[median]
        else:
            return (v1[tam - 1] + v2[tam - 1]) / 2
    else:
        if v1[median] < v2[median]:
            if tam % 2 == 0:
                return mediana(v1[median:], v2[:median], tam - median)
            else:
                return mediana(v1[median:], v2[:median + 1], tam - median)
        else:
            if tam % 2 == 0:
                return mediana(v1[:median], v2[median:], tam - median)
            else:
                return mediana(v1[:median + 1], v2[median:], tam - median)


v1 = [1, 2, 3, 4, 5, 6]
v2 = [3, 4, 5, 6, 7, 9]
print(mediana(v1, v2, 6))
print((mediana2(v1, v2, 6)))

v1 = [2, 3, 6, 7, 9]
v2 = [1, 2, 6, 10, 11]
print(mediana(v1, v2, 5))
print((mediana2(v1, v2, 5)))

v1 = [0, 1, 2, 4, 5]
v2 = [7, 9, 10, 12, 13]
print(mediana(v1, v2, 5))
print((mediana2(v1, v2, 5)))
