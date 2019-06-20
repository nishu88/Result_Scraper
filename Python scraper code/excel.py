l=['ELECTRONICS AND COMMUNICATION ENGINEERING', '1RV17EC003', 'ABHINAV S', '3', '8.20', '16MA31B', 'DISCRETE AND INTEGRAL TRANSFORMS', 'S', '16ET32', 'ENVIRONMENTAL TECHNOLOGY', 'A', '16EC33', 'ANALOG MICROELECTRONICS CIRCUITS', 'B', '16EC34', 'ANALYSIS AND DESIGN OF DIGITAL CIRCUITS', 'B', '16EC35', 'NETWORK ANALYSIS AND SYNTHESIS', 'C', '16EC36', 'CONTROL SYSTEMS', 'B', '']
import xlsxwriter
workbook = xlsxwriter.Workbook('EC_2019.xlsx')
worksheet = workbook.add_worksheet()
row=1
col=0
for x in l:
    worksheet.write_string(row,col,x)
    col+=1
row+=1    

workbook.close()
