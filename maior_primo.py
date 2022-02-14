def eprimo(k):
    cont = 2

    if k % 2 == 0 and k != 2 and k != 1:
        return False

    else:
        while k != cont and not k % cont == 0:
            cont = cont + 1

        if k == cont:
            return True
        else:
            return False
            


def maior_primo(n):
    if n <= 2 and n > 0:
        return n

    else:
        i = n
        if eprimo(n) == True:
            return n

        else:
            i = i - 1
            while eprimo(i) == False:
                i = i - 1
            return i
