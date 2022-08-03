def quantPostos(distancia, tanque, postos, paradas):
    """
    >>> quantPostos(950, 400, 4, [200, 375, 550, 750])
    2
    >>> quantPostos(10, 3, 4, [1, 2, 5, 9])
    -1
    """

    aux = tanque
    cont = 0

    for i in range(postos):

        if i == postos - 1:
            if distancia - tanque > paradas[-1]:
                cont = -1
            break

        if paradas[i] + tanque < paradas[i + 1]:
            cont = -1
            break

        if i == 0:
            tanque -= paradas[i]
        else:
            tanque = paradas[i] - paradas[i - 1]

        if tanque <= paradas[i + 1] - paradas[i]:
            cont += 1
            tanque = aux

    return cont
