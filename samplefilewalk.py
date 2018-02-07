from ftplib import FTP
import os, sys, os.path

def handleDownload(block):
    file.write(block)
    print ".",

dir1="c:/Python27/"

Remotedir="/"
#for files in os.walk(dir1):
 #   print files

user="dlpuser@dlptest.com"
password="fwRhzAnR1vgig8s"

ftp = FTP('ftp.dlptest.com')

ftp.login(user,password)
ftp.retrlines('LIST')
#ftp.cwd(Remotedir)
ftp.cwd(Remotedir)

#for files in os.walk(Remotedir):
 #   print files
    #ftp.retrbinary('RETR C:\\Data\\test\\' + files,handleDownload,
     #              open(files, 'wb'));