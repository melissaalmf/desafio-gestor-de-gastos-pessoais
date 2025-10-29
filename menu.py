
def Menu():
    opcao = int(input('Escoha 1 para entrada ou 2 para saída:'))
    if opcao == 1:
        ws['a2'] = 'entrada'
    elif opcao == 2:
        ws['a2']= 'saída'

    ws['b2'] = input('Coloque uma descrição para a operação:')
    ws['c2'] = float(input('Ponha o valor:'))
    wb.save('gerenciador_financeiro.xlsx')
Menu()
