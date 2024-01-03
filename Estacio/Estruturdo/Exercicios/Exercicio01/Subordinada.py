def ehPar (n) :
    r= (n%2==0)
    return r

def somar_par (ist):
    soma=0
    for num in ist:
        if (ehPar(num)):
            soma = soma + num
        return soma