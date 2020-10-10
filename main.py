import os
import parser

json_path = "./json"

plain_text_path = "./plainText"

plain_text_files = os.listdir(plain_text_path)

for plain_text_file in plain_text_files:
    #ignore .DS_Store
    if not plain_text_file.startswith('.'):
        new_fname = parser.file_renaming(plain_text_file)
        parser.parse_plain_text(new_fname)

json_files = os.listdir(json_path)

for json in json_files:
    #ignore .DS_Store
    if not json.startswith('.'):
        parser.write_to_word(json)
