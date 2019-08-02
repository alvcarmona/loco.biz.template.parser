import xlrd
from collections import OrderedDict
import simplejson as json
import io
import requests

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('files/Copy of Subscription model copies.xlsx')
sh = wb.sheet_by_index(0)
# List to hold translations
language =''
key = ''
d = {}

localizeKey = "hyfXaDws07D0vrxQYglxR86Ds42O6bGL9"

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
for lang, translations in d.items():
     # post straight to localize: https://localise.biz/api/docs/import/import
         # post straight to localize: https://localise.biz/api/docs/import/import
    formated = json.dumps(translations, ensure_ascii=False)
