class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_bonus(self, taxa):
        return self.salario * taxa

class FolhaPagamento:
    def __init__(self, lista):
        self.funcionarios = lista

    def processar_bonus(self, limite):
        acumulado = 0
        print("Bônus Salarial:")
        for f in self.funcionarios:
            if f.salario <= limite:
                bonus_individual = f.calcular_bonus(0.10)
                acumulado += bonus_individual
                print(f"{f.nome:} ({f.cargo}) | Bônus: R$ {bonus_individual:.2f}")
        return acumulado

equipe = [Funcionario("Alice:", "Desenvolvedora", 5000), Funcionario("João:", "Design", 3000), Funcionario("Marcos:", "Gerente", 8000)]
sistema = FolhaPagamento(equipe)
total = sistema.processar_bonus(8000)
print(f"Valor Total Gasto R$ {total:.2f}\n")