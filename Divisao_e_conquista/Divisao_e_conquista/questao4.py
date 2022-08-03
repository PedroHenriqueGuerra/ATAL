def frequenciaDeElemento(array, tamArray=None, inicio=None, final=None, elemento=None):
    """
    >>> frequenciaDeElemento([2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9])
    2 ocorre 3 vezes
    4 ocorre 3 vezes
    5 ocorre 2 vezes
    6 ocorre 1 vez
    8 ocorre 2 vezes
    9 ocorre 1 vez
    """

    if inicio == None and final == None and elemento == None:
        tamArray = len(array)
        inicio = 0
        final = tamArray - 1
        elemento = array[0]

    total = final - inicio + 1

    metade = inicio + (final - inicio) // 2

    if total == 1:
        print("%d ocorre %d vez" % (elemento, total))

        if final == tamArray - 1:
            return

        return frequenciaDeElemento(array, tamArray, final + 1, tamArray - 1, array[final + 1])

    if elemento == array[final]:
        if final < tamArray - 1 and array[final + 1] == elemento:
            return frequenciaDeElemento(array, tamArray, inicio, final + 1, elemento)

        print("%d ocorre %d vezes" % (elemento, total))

        if final == tamArray - 1: return

        return frequenciaDeElemento(array, tamArray, final + 1, tamArray - 1, array[final + 1])

    elif elemento <= array[metade]:
        return frequenciaDeElemento(array, tamArray, inicio, metade, elemento)

    elif elemento >= array[metade]:
        return frequenciaDeElemento(array, tamArray, metade, final, elemento)
