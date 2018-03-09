import json
import yaml
import csv
from pprint import pprint

FILENAME_JSON = 'input.json'
FILENAME_CSV = 'input.csv'
FILENAME_YAML = 'input.yaml'

with open(FILENAME_JSON, 'r') as json_file:
    json_data = json.load(json_file)

json_list_dicts = json_data['data']
# pprint(json_list_dicts)

with open(FILENAME_YAML, 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)

yaml_list_dicts = yaml_data['data']
# pprint(yaml_list_dicts)

with open(FILENAME_CSV, 'r') as csv_file:
    reader = csv.reader(csv_file)
    names = next(reader)
    lines = [l for l in reader]

csv_list_dicts = [
    {
        names[col_num]: col_val
        for col_num, col_val in enumerate(line)
    } for line in lines
]
# pprint(csv_list_dicts)
# creating dictionary for each line whos key is name taken from names (col_num)
# where key is (names) and value is (lines)
# enumerate iterates over list adding tuples

combined_list_of_dicts = yaml_list_dicts + csv_list_dicts + yaml_list_dicts

combined_list_of_dicts = json_list_dicts + yaml_list_dicts + csv_list_dicts

#output comboined data into a csv file
with open('output.csv', 'w') as csv_out:
    header = ','.join(names)
    csv_out.write(header + '\n')
    for dict_val in combined_list_of_dicts:
        row_list = [str(dict_val[name]) for name in names]
        row_string = ','.join(row_list)
        csv_out.write(row_string + '\n')

with open('output.json', 'w') as fp:
    json.dump(combined_list_of_dicts, fp)
#json.dump

with open('output.yaml', 'w') as outfile:
    outfile.write(yaml.dump(combined_list_of_dicts))
