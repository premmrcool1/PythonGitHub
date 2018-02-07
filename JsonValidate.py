import json
import sys
from pandas.io.json import json_normalize
import subprocess
import os
import pandas as pd
import io
import xlrd
import xlsxwriter


command='C:/cygwin64/bin/curl -gH "Authorization: Token token=mmx-fGTT0032xxTH" "https://poc47.orionic.com/api/v1/objects?limit=50000&filter[origin_nm]=MAS_57"  >  C:\Users\Premkumar.Nagarajan\Desktop\Metro\igc_assets1.json'

#json_file = "C:\Karthik\Personal\Python_Training\Data\world_bank\mas_57.json"

p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = p.communicate()


with open("C:\Users\Premkumar.Nagarajan\Desktop\Metro\igc_assets1.json") as json_file:
   json_data = json.load(json_file)

#print(json.dumps(json_data))
reload(sys)
sys.setdefaultencoding('utf8')

df = json_normalize(json_data,'result')
header = ["name","origin_nm","id","parent_id","type_id"]
df.to_csv("C:\Users\Premkumar.Nagarajan\Desktop\Metro\\output.csv", columns=header)

print "hi"
print "hoi"

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('C:\Users\Premkumar.Nagarajan\Desktop\Metro\pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

print "hi"

workbook = xlrd.open_workbook('C:\Users\Premkumar.Nagarajan\Desktop\Metro\pandas_simple.xlsx')
print "hello"
sheet = workbook.sheet_by_index(0)
print "cols:" , sheet.ncols