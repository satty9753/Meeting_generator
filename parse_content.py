import os

path = "/Users/michelle/Documents/IIT/Project/Tools/meeting_generator/plainText"

files = os.listdir(path)

first_file = files[0]

f = open(path + '/' +first_file, 'r')

data = {}

for line in f.readlines():
    if 'Marc Liu' in line:
        if 'marc' not in data:
            data['marc'] = ''
        else:   
            data['marc'] += line
    # elif 'William' in line:
    #     data['william'] += line


print(data)
f.close()