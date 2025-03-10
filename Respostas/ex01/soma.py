"""
EXERCÍCIO 1 - SOMA

Iniciamos SOMA e K em 0.
O loop while itera enquanto K for menor que INDICE.
Para cada iteração, incrementamos K e adicionamos o novo valor de K a SOMA.
A soma dos números de 1 a 13 é 91.
"""
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)