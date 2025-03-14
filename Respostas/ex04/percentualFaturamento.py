"""
EXERCÍCIO 04 - Percentual de Faturamento

"""

faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_mensal.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_mensal.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")