import csv
import os
from datetime import datetime
from time import sleep
from functions import convert_tc, convert_keywords, convert_date, load_headers, combine_genres, combine_talent

confirmation = ''

while confirmation.lower() != 'yes' and confirmation.lower() != 'no':
    print('Beginning Report Conversion')
    print('Report Conversion Checklist:')
    print('\t1. Removed top two rows (Report Title and empty line')
    print('\t2. File saved as a .csv')
    print('\t3. File saved in \"input\" folder')
    confirmation = input('Continue? (Yes or No): ')
    if confirmation.lower() == 'yes':
        print('Beginning conversion')
    elif confirmation.lower() == 'no':
        print('Exiting')
        exit(1)
    else:
        print('Incorrect input detected. Please try again.\n')
        sleep(1)

# Gets file path of script
base_file_path = os.path.realpath(__file__)

# Gets base path (Example /Users/Ralph.Pura/Desktop...)
base = os.path.dirname(base_file_path)

# Creates path for required data
header_path = base + '/data/headers/3.0_Headers.csv'
data_path = base + '/data/input/'
output_path = base + '/data/output/'

# Gets names for all files within /data/input folder
files = os.listdir(data_path)
files.remove('.DS_Store')
print(files)

# Gets number of files in /data/input folder
num_entries = len(files)

num_selection = 1

print("Files found:")
for each in files:
    # Ignores .DS_Store file
    if each != '.DS_Store':
        print('\t' + str(num_selection) + '. ' + each)
        num_selection += 1
        #print('\t' + each)

selection = 0

while selection < 1 or selection > num_entries-1:
    try:
        selection = int(input('Select file to load: '))
        if selection == 0 or selection > num_entries-1:
            print('Incorrect input. Please select a number between 1 and ' + str(num_selection-1))
    except ValueError:
        print('Error: Non-numeric character detected. Please select a number between 1 and ' + str(num_selection-1))
        pass

data_file = data_path + '/' + files[selection-1]

print('File selected: ' + files[selection-1])
sleep(2)

genre_dict = {}
actor_dict = {}

# First pass of csv file and gets information for genres and actors. Also, dedupes list.
with open(data_file, encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    #print(reader)
    next(reader)
    for row in reader:
        #print(row)
        if row[0] not in genre_dict:
            genre_dict[row[0]] = [row[13]]
        elif row[0] in genre_dict and row[13] not in genre_dict[row[0]]:
            genre_dict[row[0]].append(row[13])

        # Rearranges name. Example: Last, First => First Last;Role
        #print(row[10])
        first = row[10].split(', ')[1]
        last = row[10].split(',')[0]
        name = first + ' ' + last + ';' + row[11]

        if row[0] not in actor_dict:
            actor_dict[row[0]] = [name]
        elif row[0] in actor_dict and name not in actor_dict[row[0]]:
            actor_dict[row[0]].append(name)

# Used for debugging
#print(genre_dict)
#print(actor_dict)

output_data = []
output_data.append(load_headers(header_path))

completed_house_numbers = []

# Begins filling array with pertinent data
with open(data_file, encoding='UTF-8-SIG') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        # Iterates through each row to find if FireTV is the platform
        if 'Fire TV' in row:
            if row[0] == '':
                break
            print('Checking: ' + row[0])

            # Checks if house number has already been added
            if row[0] in completed_house_numbers:
                print(row[0] + ' found in completed_house_numbers\n')
                continue
            else:
                temp_data = row
                output_array = []

                # Adds 57 empty elements in array
                for num in range(0,58):
                    output_array.append('')

                # Asset ID
                output_array[0] = temp_data[0]
                # Title
                output_array[1] = temp_data[1]
                # Original Language
                output_array[2] = temp_data[2]
                # Asset Type
                output_array[3] = temp_data[3]
                # Episode Number
                output_array[4] = temp_data[4]
                # Season Number
                output_array[5] = temp_data[5]
                # Synopsis
                output_array[6] = temp_data[6]
                # Season Synopsis and Series Synopsis
                output_array[24] = temp_data[38]
                output_array[29] = temp_data[38]
                # Summary
                output_array[7] = temp_data[7]
                # Rating Body;Value
                output_array[8] = temp_data[8] + ';' + temp_data[9]
                # Cast Name; Role
                output_array[9] = combine_talent(actor_dict[temp_data[0]])
                # External ID; Source
                output_array[10] = temp_data[12] + ';' + 'Gracenote'
                # Genre, Season Genre
                output_array[11] = combine_genres(genre_dict[temp_data[0]])
                output_array[23] = combine_genres(genre_dict[temp_data[0]])
                # Keywords
                output_array[12] = convert_keywords(temp_data[14])
                # Provider
                output_array[13] = temp_data[15]
                # Release Date
                output_array[14] = temp_data[16]
                # Video File Location
                output_array[15] = temp_data[17]
                # Duration
                output_array[16] = temp_data[18]
                # Graphic File Format
                # Graphic File Location
                # FrameRate
                output_array[19] = temp_data[19]
                # Subtitle File Location
                output_array[20] = temp_data[20]
                # Season Title, Series Title
                output_array[21] = temp_data[21]
                output_array[28] = temp_data[21]
                # Total Episodes
                output_array[22] = temp_data[22]
                # Season Summary
                output_array[25] = temp_data[24]
                output_array[30] = temp_data[24]
                # Season Release Date
                output_array[26] = temp_data[25]
                # Series ID
                output_array[27] = temp_data[26]

                # Cue points
                output_array[31] = convert_tc(temp_data[27])
                # Segments
                # Series_Thumbnail_URL
                output_array[39] = 's3://Images/S3/erthx/' + temp_data[28]
                output_array[51] = 's3://Images/S3/erthx/' + temp_data[28]
                # Titled series portrait URL
                output_array[33] = 's3://Images/S3/erthx/' + temp_data[29]
                output_array[40] = 's3://Images/S3/erthx/' + temp_data[29]
                output_array[46] = 's3://Images/S3/erthx/' + temp_data[29]
                # Untitled series portrait poster URL
                output_array[34] = 's3://Images/S3/erthx/' + temp_data[30]
                output_array[41] = 's3://Images/S3/erthx/' + temp_data[30]
                output_array[48] = 's3://Images/S3/erthx/' + temp_data[30]
                # Landscape_Poster_URL
                output_array[47] = 's3://Images/S3/erthx/' + temp_data[31]
                output_array[44] = 's3://Images/S3/erthx/' + temp_data[31]
                output_array[37] = 's3://Images/S3/erthx/' + temp_data[31]
                output_array[49] = 's3://Images/S3/erthx/' + temp_data[31]
                output_array[42] = 's3://Images/S3/erthx/' + temp_data[31]
                output_array[35] = 's3://Images/S3/erthx/' + temp_data[31]
                # Thumbnail_URL
                output_array[45] = 's3://Images/S3/erthx/' + temp_data[32]
                output_array[38] = 's3://Images/S3/erthx/' + temp_data[32]
                output_array[50] = 's3://Images/S3/erthx/' + temp_data[32]
                output_array[43] = 's3://Images/S3/erthx/' + temp_data[32]
                output_array[36] = 's3://Images/S3/erthx/' + temp_data[32]
                # Rights Start Window
                output_array[52] = convert_date(temp_data[33])
                # Rights End Window
                output_array[53] = convert_date(temp_data[34])
                # Territory Includes
                output_array[54] = temp_data[35]
                # Territory Excludes
                # Service Type
                output_array[56] = temp_data[36]
                # Platforms
                output_array[57] = temp_data[37]

                #print(temp_data[26])
                completed_house_numbers.append(row[0])
                output_data.append(output_array)

# for each in output_data:
#     print(each)

# Gets current date and time
date = datetime.now()
# Sets output file date/time
output_file = output_path + 'output_' + date.strftime('%Y_%m_%d_%H%M%S') + '.csv'

# Writes data into output file.
with open(output_file, 'w', encoding='utf-8-sig', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(output_data)

print('Done')
