"""
EXERCÍCIO 03: Faturamento

"""
import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = [item['valor'] for item in dados]

menor = min(faturamento) if faturamento else 0
maior = max(faturamento) if faturamento else 0
media = sum(faturamento) / len(faturamento) if len(faturamento) > 0 else 0

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Média mensal: {media}")