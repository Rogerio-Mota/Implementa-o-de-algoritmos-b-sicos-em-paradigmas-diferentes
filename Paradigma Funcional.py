from functools import reduce

funcionarios = [
    {"nome": "Alice", "cargo": "Desenvolvedora", "salario": 5000},
    {"nome": "João", "cargo": "Designer", "salario": 3000},
    {"nome": "Macos", "cargo": "Gerente", "salario": 8000}
]
def validar_bonus(f):
    if f["salario"] <= 8000:
        return True
    else:
        return False

def gerar_valor_bonus(f):
    return (f["nome"], f["cargo"], f["salario"] * 0.10)

def somar_valores(acumulado, item):
    return acumulado + item[2]

filtrados = filter(validar_bonus, funcionarios)
bonificados = list(map(gerar_valor_bonus, filtrados))
total = reduce(somar_valores, bonificados, 0)

print("Bônus Salarial:")
for nome, cargo, bonus in bonificados:
    print(f"{nome} ({cargo}) | Bônus: R$ {bonus:.2f}")

print(f"Total Gasto: R$ {total:.2f}")