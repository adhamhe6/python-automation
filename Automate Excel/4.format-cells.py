from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook('xlsx/report.xlsx')
sheet = wb['report']

# Add format
sheet['A1'] = 'Sales Report'
sheet['A2'] = 'January'
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=10)

wb.save('xlsx/report_january.xlsx')