from docx import Document
import json
import os

path = "/Users/satty/Documents/Tools/Meeting_generator/json"

files = os.listdir(path)

first_file = files[0]

doc = Document('SD-App 20201008.docx')

michelle = 'michelle'
marc = 'marc'
hunk = 'hunk'
william = 'william'
sandy = 'sandy'
eric = 'eric'

numTables = doc.tables
table = numTables[0]

#會議日期
date = first_file.split('SD-App')[1].split('.')[0].strip()
table.cell(1, 1).text = date

# 紀錄
# table.cell(3, 3).text = "Michelle"

#read file
first_filename = first_file.split('.')[0]

with open(first_file , 'r') as reader:
    json_data = json.loads(reader.read())
    #主席
    if marc in json_data:
        table.cell(2, 1).text = 'Marc'
    else:
        table.cell(2, 1).text = 'Hunk'

##########Leader
#工作項目
    if marc in json_data:
        table.cell(7, 0).text = json_data[marc]
    else:
        table.cell(7, 0).text = json_data[hunk]

######william
#工作項目
    table.cell(8, 0).text = json_data[william]

######michelle
#工作項目
    table.cell(9, 0).text = json_data[michelle]

######sandy
#工作項目
    table.cell(10, 0).text = json_data[sandy]

######eric
#工作項目
    table.cell(11, 0).text = json_data[eric]

doc.save(first_filename+'.docx')