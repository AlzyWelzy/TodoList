from pathlib import  Path

# Path: essays.txt
path = Path('essay.txt')
open_file = open(path, 'r')

# Read the file
text = open_file.read().split(' ')
print(text)

text_list=[i.capitalize() for i in text]
print(text_list)
[print(i) for i in text_list]