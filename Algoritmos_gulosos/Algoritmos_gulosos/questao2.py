def assinaturas(lista):
    """
    >>> assinaturas([[1,3],[2,5],[3,6]])
    1
    [3]
    >>> assinaturas([[4,7],[1,3],[2,5],[5,6]])
    2
    [3, 6]
    """
    i = lista[0][0]
    f = lista[0][1]
    quantVisitas = 0
    horarioVisitas = []

    for x in lista[1:]:
        if f >= x[0]:
            i = x[0]
        else:
            horarioVisitas.append(f)
            i = x[0]
            f = x[1]
            quantVisitas += 1

        if f > x[1]:
            f = x[1]

    horarioVisitas.append(f)
    quantVisitas += 1
    print(quantVisitas)
    print(horarioVisitas)
