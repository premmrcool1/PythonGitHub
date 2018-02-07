import json
from pandas.io.json import json_normalize
import subprocess
import os

command='C:/cygwin64/bin/curl -gH "Authorization: Token token=mmx-laytezI7vXFjDAIcMMju2w" "https://pentaho.orionic.com/api/v1/objects/tree?levels=7&filter[origin_nm]=ORACLE_DDL_EXTRACT" > C:\cygwin64\home\Premkumar.Nagarajan\Lineage'

p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = p.communicate()
with open("C:\cygwin64\home\Premkumar.Nagarajan\Lineage") as data_file:
   data = json.load(data_file)

#json.dumps(data, sort_keys=True, indent=4)
df = json_normalize(data,'result')

print df
df.to_csv("C:\Users\Premkumar.Nagarajan\Desktop\Learning\output_obj.csv")