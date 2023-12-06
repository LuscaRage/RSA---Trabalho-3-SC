import random
import math


def gerar_senhas(): #Faz a chave pública e privada RSA de tamanho 1024
    p = generate_prime(1024 // 2)
    q = generate_prime(1024 // 2)
    n = p * q   
    tangete_n = (p - 1) * (q - 1)

    e = random.randint(2, tangete_n - 1) # Valor aritario entre 1 e tangente de n
    while math.gcd(e, tangete_n) != 1: # Veririca se tem divisores comuns, caso tenha escolhe outro valor
        e = random.randint(2, tangete_n - 1)

    #Aqui é calculado o inverso multiplicativo de e (mod tangete_n) (ou seja um número que multiplicado a d seja congruente a 1 modulo tangente de n).
    gcd, aux, _ = extended_gcd(e, tangete_n)
    if gcd != 1:
        raise ValueError("não existe inverso multiplicativo modular")
    d = aux % tangete_n 

    return (n, e), (n, d)



def generate_prime(bits): #Gera um primo aleatório com tamanho específico
    while True:
        n = random.randint(2 ** (bits - 1), 2 ** bits - 1)
        if teste_de_Miller_Rabin(n):
            return n

def teste_de_Miller_Rabin(n, k=7): #Testa se é primmo com Miller Rabin
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def extended_gcd(a, b): #Função para calcular o MDC os coeficientes de Bézout
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y



