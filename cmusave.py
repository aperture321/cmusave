#!/usr/bin/env python

import urllib2
import os

#v1.0
stream_url = 'http://ice.somafm.com/groovesalad'
request = urllib2.Request(stream_url)
try:
    request.add_header('Icy-MetaData', 1)
    response = urllib2.urlopen(request)
    icy_metaint_header = response.headers.get('icy-metaint')
    if icy_metaint_header is not None:
        metaint = int(icy_metaint_header)
        read_buffer = metaint+255
        content = response.read(read_buffer)
        title = content[metaint:].split("'")[1] + "\n"
        os.chdir(os.path.expanduser("~"))
        filew = open(".savedata.txt", "r")
        infile = False
        for line in filew:
            if (line == title):
                infile = True
        filew.close() #now set for writing
        filew = open(".savedata.txt", "w")
        if (not infile):
            filew.write(title)
        filew.close()
except:
    print 'Error'
