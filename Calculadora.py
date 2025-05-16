def operacao_basicas():
    num1 =float(input('Digite o primeiro número: '))
    op = input('Digite a operação (+, -, *, /): ')
    num2 =float(input('Digite o segundo número: '))

    if op == '+':
        print(f'Resultado: {num1 + num2}')
    elif op == '-':
        print(f'Resultado: {num1 - num2}')
    elif op == '*':
        print(f'Resultado: {num1 * num2}')
    elif op == '/':
        if num2 != 0:
            print(f'Resultado: {num1 / num2}')
        else:
            print('Erro: Divisão por zero não é permitida.')
            

def regra_de_tres():
    print("\n=== REGRA DE TRÊS SIMPLES ===")
    print("""
    A       B
    ──  =  ──
    C       X

    Onde:
    - A e B são grandezas diretamente proporcionais.
    - Você conhece A, B e C, e quer encontrar X.
    """)

    print("Digite os valores conhecidos:")
    try:
        A = float(input("Valor de A: "))
        B = float(input("Valor de B: "))
        C = float(input("Valor de C: "))
    except ValueError:
        print("Erro: Digite apenas números!")
        return

    if A == 0:
        print("Erro: 'A' não pode ser zero (divisão inválida).")
        return

    X = (B * C) / A
    print(f"\nResultado: X = {X:.2f}\n")


def potencia(base, expoente):
    """
    Calcula a potência de um número.
    
    Args:
        base (float): O número base
        expoente (float): O expoente para elevar a base
        
    Returns:
        float: Resultado da base elevada ao expoente
    """
    return base ** expoente

import math

def calcular_radiciacao():
    print("\n=== RADICIAÇÃO (√) ===")
    print("Escolha o tipo de raiz:")
    print("1 - Raiz quadrada (√x)")
    print("2 - Raiz cúbica (³√x)")
    print("3 - Raiz enésima (ⁿ√x)")
    
    tipo = input("👉 Digite a opção desejada (1-3): ")
    
    try:
        if tipo == '1':
            num = float(input("Digite o número para calcular a raiz quadrada: "))
            if num < 0:
                print("Erro: Não existe raiz real de número negativo!")
            else:
                resultado = math.sqrt(num)
                print(f"√{num} = {resultado:.4f}")
                
        elif tipo == '2':
            num = float(input("Digite o número para calcular a raiz cúbica: "))
            resultado = num ** (1/3)
            print(f"³√{num} = {resultado:.4f}")
            
        elif tipo == '3':
            num = float(input("Digite o número: "))
            indice = float(input("Digite o índice da raiz: "))
            if indice == 0:
                print("Erro: Índice não pode ser zero!")
            elif num < 0 and indice % 2 == 0:
                print("Erro: Não existe raiz real de número negativo com índice par!")
            else:
                resultado = num ** (1/indice)
                print(f"{indice:.0f}√{num} = {resultado:.4f}")
                
        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Erro: Digite apenas números válidos!")


def triangolo_retangulo():
    cat1=float(input('digite cateto 1 '))
    cat2=float(input('digite cateto 2 '))

    TR=((cat1 * cat2 )/2)
    print(f'A area é {TR} ')



while True:
    print("\n")
    print(" "*15 + "📊 CALCULADORA UNIVERSAL 📊")
    print('\n')

    print("1 ➔ Operações básicas (+ - * /)")
    print("2 ➔ Regra de três simples")
    print("3 ➔ Potenciação (xʸ)")
    print("4 ➔ Radiciação (√)")
    print("5 ➔ Calcular triângulo retângulo")
    print("6 ➔ Sair do programa")
    print("-" * 50 + "\n")
    print("\n")
   
        
    opcao = input("👉 Digite o número da opção desejada: ")

        
    if opcao== '1':
        operacao_basicas()
    elif opcao== '2':
        regra_de_tres()
    elif opcao == '3':
            print("\n=== POTENCIAÇÃO (xʸ) ===")
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = potencia(base, expoente)
            print(f"\nResultado: {base}^{expoente} = {resultado}")
    elif opcao== '4':
        calcular_radiciacao()
    elif opcao == '5':
        triangolo_retangulo()
    elif opcao=='6':
        break
    else:
        print("digite algo doido")
        print('\n')
        print('\n')
