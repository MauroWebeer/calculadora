from Calculator import Calculator
from VerificandoNumero import VerificandoNumero
import time

print('''Bem vindo!!!
Para Encerrar Digite S''')
time.sleep(2)

valor = input(f'''Insira um valor
''').replace('.','')

while VerificandoNumero.eh_numero(valor) == False:
    valor = input(f'Insira um valor válido')

while valor:
    opcao = input(f"""
        Escolha uma operação:
        1: Adição
        2: Subtração
        3: Multiplicação
        4: Divisão
        5: Sair
    """)

    while VerificandoNumero.eh_opcao(opcao) == False:
        opcao = input(f"""
            Escolha uma operação válida:
            1: Adição
            2: Subtração
            3: Multiplicação
            4: Divisão
            5: Sair
        """)

    if int(opcao) == int(1):
        valor_2 = input(f'insira outro valor')
        while VerificandoNumero.eh_numero(valor_2) == False:
            valor_2 = input(f'Insira um valor válido')
        valor = Calculator.soma(valor, valor_2)
    if int(opcao) == int(2):
        valor_2 = input(f'insira outro valor')
        while VerificandoNumero.eh_numero(valor_2) == False:
            valor_2 = input(f'Insira um valor válido')
        valor = Calculator.subt(valor, valor_2)
    if int(opcao) == int(3):
        valor_2 = input(f'insira outro valor')
        while VerificandoNumero.eh_numero(valor_2) == False:
            valor_2 = input(f'Insira um valor válido')
        valor = Calculator.mult(valor, valor_2)
    if int(opcao) == int(4):
        valor_2 = input(f'insira outro valor')
        while VerificandoNumero.eh_numero(valor_2) == False:
            valor_2 = input(f'Insira um valor válido')
        valor = Calculator.div(valor, valor_2)
    if int(opcao) == int(5):
        break

    print(valor)

