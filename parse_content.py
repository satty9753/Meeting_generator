import os
import json

path = "/Users/satty/Documents/Tools/Meeting_generator/plainText"

files = os.listdir(path)

first_file = files[0]

marc = 'Marc Liu'
hunk = 'Hunk Yang'
william = 'William Weng'
michelle = 'Michelle Chen'
sandy = 'Sandy Yeh'
eric = 'Eric Yeh'

def addWord(s):
    if 'marc' in data:
        data['marc'] += s
    else:
        data['hunk'] += s
    data['william'] += s
    data['michelle'] += s
    data['sandy'] += s
    data['eric'] += s


def parse_person(part):
    if part == weeklyComplete:
        addWord('本週完成項目')
    elif part == processing:
        addWord('進行中項目')
    else:
        addWord('下週預計')

    if 'marc' in data:
        data['marc'] += part.split(marc)[1].split(william)[0]
    else:
        data['hunk'] += part.split(hunk)[1].split(william)[0]

    data['william'] += part.split(william)[1].split(michelle)[0]
    data['michelle'] += part.split(michelle)[1].split('Android')[0]
    data['sandy'] += part.split(sandy)[1].split(eric)[0]
    data['eric'] += part.split(eric)[1]


data = {'william':'', 'michelle':'', 'sandy':'', 'eric':''}

f = open(path + '/' +first_file, 'r')

content = f.read()

if marc in content:
    data['marc'] = ''
elif hunk in content:
    data['hunk'] = ''

weeklyComplete = content.split('本週完成項目：')[1].split('進行中項目：')[0]
processing = content.split('進行中項目：')[1].split('下週預計：')[0]
futurePlan = content.split('下週預計：')[1]

parse_person(weeklyComplete)
parse_person(processing)
parse_person(futurePlan)


f.close()

json_data = json.dumps(data,ensure_ascii=False,indent=2)

fname = first_file.split('.')[0]

new_path = 'json/'

with open(new_path + fname +'.json', "w") as outfile: 
    outfile.write(json_data) 