"""
EXERCÍCIO 03: Faturamento

"""
import json

data = '{"faturamento": [1000, 2000, 0, 3000, 4000, 0, 5000]}'

faturamento = json.loads(data)["faturamento"]

menor = min(faturamento) if faturamento else 0
maior = max(faturamento) if faturamento else 0
media = sum(faturamento) / len(faturamento) if len(faturamento) > 0 else 0

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Média mensal: {media}")