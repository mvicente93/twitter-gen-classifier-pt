'''
@author: vicente

Python script that reads the list of officially admitted names from the portuguese name registry institute, removes
not admitted names
'''
import csv
import os
from pre_processing import normalize

name_dict = {}
abrv_dict = {}
key_words_dict = {}

csvs_dir = os.path.dirname(__file__)

with open(csvs_dir+'/Lista_de_Nomes_Portugueses.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        name = normalize(row[0].decode('utf-8').lower().strip())

        if row[2] == 'Sim':
            if 'M' in row:
                name_dict[name] = 'M'
            elif 'F' in row:
                name_dict[name] = 'F'
            else:
                name_dict[name] = 'U'

with open(csvs_dir+'/Lista_de_Abreviaturas_Portuguesas.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        normalized_name = normalize(row[0].decode('utf-8').lower().strip())

        if 'M' in row:
            abrv_dict[normalized_name] = 'M'
        elif 'F' in row:
            abrv_dict[normalized_name] = 'F'
        else:
            abrv_dict[normalized_name] = 'U'

with open(csvs_dir+'/meaningful_words.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        normalized_name = normalize(row[0].decode('utf-8').lower().strip())

        if 'M' in row:
            key_words_dict[normalized_name] = 'M'
        elif 'F' in row:
            key_words_dict[normalized_name] = 'F'


