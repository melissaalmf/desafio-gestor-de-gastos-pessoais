from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'gerenciador_financeiro'
ws.append(['operação', 'descrição','valor'])
wb.save('gerenciador_financeiro.xlsx')




