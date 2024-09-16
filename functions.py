import csv

# Converts timecodes to add "0". Example 1:30:00,1:56:00 => 01:30:00,01:56:00
def convert_tc(tcs):
    print('\tConverting: ' + tcs, end=' ')
    tc_array = tcs.split(',')

    converted_string = ''

    for each in range(len(tc_array)):
        updated_tc = '0' + tc_array[each] + ','
        updated_tc = updated_tc.replace('.', ';')
        #print(updated_tc)
        converted_string += updated_tc

    print(' | Converted: ' + converted_string[:-1])

    return converted_string[:-1]

# Removes spaces in between keywords. Example 'Action, Adventure, Animals' => 'Action,Adventure,Animals'
def convert_keywords(keywords):
    print('\tConverting: ' + keywords, end=' ')
    keywords_array = keywords.split(',')

    converted_string = ''

    for each in range(len(keywords_array)):
        if each == 0:
            converted_string += keywords_array[each] + ','
        else:
            temp = keywords_array[each]
            temp = temp.replace(' ', '', 1)
            converted_string += temp + ','

    print(' | Converted: ' + converted_string[:-1])

    return converted_string[:-1]


def convert_date(date):
    print('\tConverting: ' + date, end=' ')

    date_dict = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }

    date_array = date.split()
    month = date_dict[date_array[0]]
    day = date_array[1][:-1]
    year = date_array[2]
    converted_date = year + '-' + month + '-' + day

    print(' | Converted: ' + converted_date)

    return converted_date

# Loads file headers from headers.csv
def load_headers(header_file):

    header = []

    with open(header_file, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            for each in row:
                header.append(each)

    return header

# Gets talent array from specific house number and combines it. Returns string
# Example: [Isaac Carter;Talent, Brook Carter;Talent] => Isaac Carter;Talent | Brook Carter;Talent]
def combine_talent(talent_arr):
    output = ''

    for each in talent_arr:
        output += each + '|'

    return output[:-1]

def combine_genres(genre_arr):
    output = ''

    for each in genre_arr:
        output += each + ','

    return output[:-1]