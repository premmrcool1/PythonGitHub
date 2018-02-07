import json
from pandas.io.json import json_normalize
import subprocess
import os

#command='C:/cygwin64/bin/curl -gH "Authorization: Token token=mmx-fGTT0032xxTH" "https://poc47.orionic.com/api/v1/objects?limit=50000&filter[origin_nm]=Conn_Metro_Infa_Sud1" > C:\cygwin64\home\Premkumar.Nagarajan\Lineage'

#p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#out,err = p.communicate()
with open("C:\Users\Premkumar.Nagarajan\Desktop\Metro\igc_assets.json") as data_file:
    data = json.load(data_file)
#print data
#json.dumps(data, sort_keys=True, indent=4)
df = json_normalize(data,'_context')

#print df
df.to_csv("C:\Users\Premkumar.Nagarajan\Desktop\Learning\sample_test1.csv")