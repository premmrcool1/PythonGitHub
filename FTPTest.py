from ftplib import FTP
import os, sys, os.path

def handleDownload(block):
    file.write(block)
    print ".",

ddir='C:\\Data\\test\\'
os.chdir(ddir)
ftp = FTP('test1/server/')

print 'Logging in.'
ftp.login('user1\\anon', 'pswrd20')
directory = '\\data\\test\\'

print 'Changing to ' + directory
ftp.cwd(directory)
ftp.retrlines('LIST')

print 'Accessing files'

for  files in os.walk(directory):
    for file in files:
        full_fname = os.path.join(root, fname);
        print 'Opening local file '
        ftp.retrbinary('RETR C:\\Data\\test\\' + fname,
                       handleDownload,
                       open(full_fname, 'wb'));
        print 'Closing file ' + filename
        file.close();
ftp.close()