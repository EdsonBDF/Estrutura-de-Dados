# Função para adição
def adicao(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para multiplicação
def multiplicacao(x, y):
    return x * y

# Função para divisão
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Função principal para escolher a operação
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"{num1} + {num2} = {adicao(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Escolha inválida!")