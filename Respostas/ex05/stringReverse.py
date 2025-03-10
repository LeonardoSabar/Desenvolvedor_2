"""
EXERCÍCIO 05 - String Reverse

"""

def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string = input("Digite uma string: ")
string_invertida = inverter_string(string)
print(f"String invertida: {string_invertida}")