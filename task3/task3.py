import json
import sys

if sys.argv and len(sys.argv) > 2:  # если из командной строки
    tests = sys.argv[1]
    values = sys.argv[2]
else:                               # если из консоли
    tests = input()
    values = input()

with open(tests, "r") as tests_file:
    data_tests = json.load(tests_file)

with open(values, "r") as values_file:
    data_values = json.load(values_file)

data_values = data_values['values']
data_tests = data_tests['tests']

def recurs(obj, id, val):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "values":
                recurs(v, id, val)
            if k == 'id' and v == id:
                obj['value'] = val

    elif isinstance(obj, list):
        for slv in obj:
            recurs(slv, id, val)

for i in data_values:
    id = i['id']
    val = i['value']
    recurs(data_tests, id, val)


with open("report.json", "w") as report_file:
    json.dump(data_tests, report_file)