def eprimo(x):
    cont = 2

    if x % 2 == 0 and x != 2 and x != 1:
        return False

    else:
        while x != cont and not x % cont == 0:
            cont = cont + 1

        if x == cont:
            return True
        else:
            return False


def n_primos(y):
    i = 2
    primos = 1

    while i <= y:
        if eprimo(i):
            primos = primos + 1
            i = i + 1

    return primos
