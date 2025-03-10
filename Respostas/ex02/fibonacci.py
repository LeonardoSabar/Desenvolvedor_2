"""""

EXERCÍCIO 02 - Fibonacci

"""""

def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a, b]
    while b < n:
        a, b = b, a + b
        fib_sequence.append(b)
    
    return fib_sequence[:-1], n in fib_sequence

number = int(input("Informe um número: "))
sequence, belongs = fibonacci(number)

if belongs:
    print(f"O número {number} pertence à sequência Fibonacci: {sequence}")
else:
    print(f"O número {number} não pertence à sequência Fibonacci.")