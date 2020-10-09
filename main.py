import os
import parser

json_path = "./json"

plain_text_path = "./plainText"

plain_text_files = os.listdir(plain_text_path)

for plain_text_file in plain_text_files:
    parser.parse_plain_text(plain_text_file)

json_files = os.listdir(json_path)

for json in json_files:
    parser.write_to_word(json)
