import xlrd
from collections import OrderedDict
import simplejson as json
import io

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('files/Copy of Subscription model copies.xlsx')
sh = wb.sheet_by_index(0)
# List to hold translations
language =''
key = ''
d = {}

# Iterate through each row in worksheet and fetch values into dict
for j in range(1, sh.ncols):
    if j!=0:
        for i in range(0, sh.nrows):
            if i == 0 :
                language = sh.cell(0, j).value
                d[language] = {}
            else:
                key = sh.cell(i, 0).value
                d[language][key] = sh.cell(i,j).value
app_json = json.dumps(d, ensure_ascii=False)
json = json.dumps(app_json,  indent=4, separators=(',', ': '))
f = open("exports/translations.json", "w")
f.write(app_json)
f.close()

