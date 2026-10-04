import xlwings as xw

wb = xw.Book('global_trade_excel_analysis.xlsx')
sheet = wb.sheets[0]
print("Conectado al libro:", wb.name)
print("Hojas disponibles:", [s.name for s in wb.sheets])

wb.api.RefreshAll()
print("Datos actualizados correctamente mediante Python.")

pivot_sheet = wb.sheets['Hoja2']
total_general = pivot_sheet.range('L20').value
print("Valor total general leido desde Excel:", total_general)
