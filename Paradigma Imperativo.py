funcionarios = [
    {"nome": "Alice", "cargo": "Dev", "salario": 5000},
    {"nome": "João", "cargo": "Design", "salario": 3000},
    {"nome": "Marcos", "cargo": "Gerente", "salario": 8000}
]

valor_x = 8000
total_bonus = 0

print("Bônus Salarial")
for i in range(len(funcionarios)):
    if funcionarios[i]["salario"] <= valor_x:
        nome = funcionarios[i]["nome"]
        bonus = funcionarios[i]["salario"] * 0.10
        total_bonus += bonus
        funcionarios[i]["salario"] += bonus
        print(f" {nome}: Bônus de R$ {bonus:.2f}")

print(f"Total Gasto é: R$ {total_bonus:.2f}\n")