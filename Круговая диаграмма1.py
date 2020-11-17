import xlswriter
import sys


workbook=xlswriteer.Workbook('res.xlsx')
worksheet=workbook.add_worksheet()
data = []
for line in sys.stdin:
    line=line.strip()
    for_data=line. split(' ')
    data.append((for_data[0], int(for_data[1])))
for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)
chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'categories': '=Sheet1!A1:A'+str(len(data)), 'values': '=Sheet1B!:B'+str(len(data))})
worksheet.insert_chart('C3', chart)
workbook.close()
