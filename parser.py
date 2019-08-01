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
translationsModule = sh.cell(0, 0).value
# Iterate through each row in worksheet and fetch values into dict
for j in range(1, sh.ncols):
    if j!=0:
        for i in range(0, sh.nrows):
            if i == 0 :
                language = sh.cell(0, j).value
                d[language] = {}
                d[language][translationsModule] = {}
            else:
                key = sh.cell(i, 0).value
                d[language][translationsModule][key] = sh.cell(i, j).value
for lang, translations in d.items():
    app_json = json.dumps(translations, ensure_ascii=False)
    jsonObject = json.dumps(app_json,  indent=4, separators=(',', ': '))
    f = open("exports/"+lang+".json", "w")
    f.write(app_json)
    f.close()
