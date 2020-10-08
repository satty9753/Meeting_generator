from docx import Document
import json
import os

path = "/Users/satty/Documents/Tools/Meeting_generator/json"

files = os.listdir(path)

first_file = files[0]

doc = Document('SD-App 20201008.docx')

numTables = doc.tables
table = numTables[0]

#會議日期
first_filename = first_file.split('.')[0]
date = first_file.split('SD-App')[1].split('.')[0].strip()
table.cell(1, 1).text = date

#主席
#......

#紀錄
table.cell(3, 3).text = "Michelle"

######Leader
#名稱
#工作項目

######william
#名稱
#工作項目


######michelle
#名稱
#工作項目

######sandy
#名稱
#工作項目


######eric
#名稱
#工作項目

doc.save(first_filename+'.docx')
# table.cell(3, 4).text = "Michelle"

# for table in numTables:
#     row_count = len(table.rows)
#     col_count = len(table.columns)
#     for i in range(row_count):
#         for j in range(col_count):
#             if "2020/10/08" in table.cell(i, j).text:
#                 print(i, j)
#             else:
#                 continue