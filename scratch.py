import csv
from functions import load_headers
import os
from datetime import datetime

file_name = '/Users/ralph.pura/Desktop/PythonScripts/Amagi_Converter/data/headers/3.0_Headers.csv'

output_data = [[]]

# with open(file_name, encoding='utf-8-sig') as header_file:
#     reader = csv.reader(header_file)
#     for row in reader:
#         for each in row:
#             output_data[0].append(each)

output_data[0] = load_headers(file_name)
#print(output_data)

### New Section ###

data_path = '/Users/ralph.pura/Desktop/PythonScripts/Amagi_Converter/data/input'

file = os.listdir(data_path)

data_file = data_path + '/' + file[0]

#print(data_file)

# genre_dict = {}
# actor_dict = {}
#
# with open(data_file, encoding='utf-8') as file:
#     reader = csv.reader(file)
#     #print(reader)
#     next(reader)
#     for row in reader:
#         #print(row)
#         if row[0] not in genre_dict:
#             genre_dict[row[0]] = [row[13]]
#         elif row[0] in genre_dict and row[13] not in genre_dict[row[0]]:
#             genre_dict[row[0]].append(row[13])
#
#         # Uncomment this when talent is added
#         first = row[10].split(', ')[1]
#         last = row[10].split(',')[0]
#         name = first + ' ' + last + ';' + row[11]
#
#         if row[0] not in actor_dict:
#             actor_dict[row[0]] = [name]
#         elif row[0] in actor_dict and name not in actor_dict[row[0]]:
#             actor_dict[row[0]].append(name)
#
# house_num = 'EXTVP-002981'
#
# actors_list = ''
#
# for each in actor_dict[house_num]:
#     actors_list += each + '|'
#
# print(actors_list[:-1])
#
# temp_arr = []
# for cell in range(0,57):
#     temp_arr.append('')
# print(temp_arr)
# print(len(temp_arr))

file_path = os.path.realpath(__file__)
base = os.path.dirname(file_path)
#print(file_path)
#print(base)

#-------------------------------------------------#

header_path = base + '/headers/3.0_Headers.csv'
data_path = base + '/data/input/'

input_data = os.listdir(data_path)

num_entries = len(input_data)

num_selection = 1

for each in input_data:
    if each != '.DS_Store':
        print(str(num_selection) + '. ' + each)
        num_selection += 1

selection = 0

while selection < 1 or selection > num_entries-1:
    try:
        selection = int(input('Select file to load: '))
        if selection == 1 or selection > num_entries-1:
            print('Incorrect input. Please select a number between 1 and ' + str(num_selection-1))
    except ValueError:
        print('Error: Non-numeric character detected. Please select a number between 1 and ' + str(num_selection-1))
        pass

print('File selected: ' + input_data[int(selection)])

to_open = data_path + input_data[selection]
with open(to_open, encoding='UTF-8-SIG') as input_file:
    reader = csv.reader(input_file)
    for each in reader:
        #break
        print(each)

date = datetime.now()
current = 'output_' + date.strftime('%Y_%m_%d_%H%M%S') + '.csv'

print(current)