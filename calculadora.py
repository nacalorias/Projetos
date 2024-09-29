while True:
    operacao = input("Escolha uma operação: + (adição), * (multiplicação), - (subtração), / (divisão), ** (potência), 0 para sair: ")
    if operacao == '0':
        break
    valor1=float(input("Digite um valor: "))
    valor2=float(input('Digite um valor: '))

    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '/':
        resultado = valor1 / valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '**':
        resultado = valor1 ** valor2
    elif operacao == '-':
        resultado = valor1 - valor2

    print("O resultado é: "+str(resultado))
