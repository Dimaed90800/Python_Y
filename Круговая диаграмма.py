import xlsxwriter
import sys
 
workbook = xlsxwriter.Workbook('res.xlsx')
worksheet = workbook.add_worksheet()
 
# Данные
data = []
for line in sys.stdin:
    line=line.strip()
    line1=line.split()
    if line1:
        data.append((line1[0], int(line1[1])))
        print(line1)
for i in enumirate(data):
    worksheet.write(i, 0, i[0])
    worksheet.write(i, 1, i[1])
# Тип диаграмы
chart = workbook.add_chart({'type': 'pie'})
 
# Строим по нашим данным
chart.add_series({'categories': '=Sheet1!A1:A5', 'values': '=Sheet1!B1:B'+str(len(data))})
 
worksheet.insert_chart('C3', chart)
 
workbook.close()