def achar_menor(v, inicio, fim):
    """
    >>> achar_menor([0, 1, 2, 6, 9, 11, 15],0,6)
    3
    >>> achar_menor([1, 2, 3, 4, 6, 9, 11, 15],0,7)
    0
    >>> achar_menor([0, 1, 2, 3, 4, 5, 6, 8],0,7)
    7
    """

    if v[inicio] != inicio:
        return inicio
    else:
        meio = (inicio + fim) // 2
        if v[meio] == meio:
            return achar_menor(v, meio + 1, fim)
        else:
            return achar_menor(v, inicio, meio)
