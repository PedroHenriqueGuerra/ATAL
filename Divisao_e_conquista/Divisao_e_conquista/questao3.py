def teto(v, tam, k):
    meio = tam // 2
    candidato = None

    if tam == 0:
        return None

    if k > v[-1]:
        return -1

    if v[meio] == k:
        return k
    else:
        if v[meio] > k:
            candidato = teto(v[:meio + 1], meio, k)
            if candidato is None:
                candidato = v[meio]
                return candidato
        else:
            candidato = teto(v[meio + 1:], meio, k)
            return candidato
    return candidato


def piso(v, tam, k):
    meio = tam // 2
    candidato = None
    # [1, 4, 6, 8, 9]
    if tam == 0:
        return None

    if k < v[0]:
        return -1

    if k >= v[-1]:
        return v[-1]

    if v[meio] == k:
        return k
    else:
        if v[meio] < k:
            candidato = piso(v[meio:], meio, k)
            if candidato is None:
                candidato = v[meio]
        else:
            candidato = piso(v[:meio], meio, k)
            return candidato
    return candidato

v = [1, 4, 6, 8, 9]
tam = 5
k = 10

for i in range(0, k + 1):
    print("k = ", i, " ----> teto = ", teto(v, tam, i), ",piso = ", piso(v, tam, i))
