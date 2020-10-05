# Ashil Ramjee
# Class containing a method to send a HTTP Request and get the response
# Check licenses.txt for licenses

import sys
import urllib2
import zlib
import time
import re
import xml.dom.pulldom
import operator
import codecs
from optparse import OptionParser

nDataBytes, nRawBytes, nRecoveries, maxRecoveries = 0, 0, 0, 3

# Method to send the http verb request to the OAI repository and get the XML data
def getFile(serverString, command, verbose=1, sleepTime=0):
    global nRecoveries, nDataBytes, nRawBytes
    if sleepTime:
        time.sleep(sleepTime)
    remoteAddr = serverString + '?verb=%s' % command
    if verbose:
        print "\r", "getFile ...'%s'" % remoteAddr[-90:]
    try:
        remoteData = urllib2.urlopen(remoteAddr).read()
    except urllib2.HTTPError, exValue:
        if exValue.code == 503:
            retryWait = int(exValue.hdrs.get("Retry-After", "-1"))
            if retryWait < 0:
                return None
            print 'Waiting %d seconds' % retryWait
            return getFile(serverString, command, 0, retryWait)
        print exValue
        if nRecoveries < maxRecoveries:
            nRecoveries += 1
            return getFile(serverString, command, 1, 60)
        return
    nRawBytes += len(remoteData)
    try:
        remoteData = zlib.decompressobj().decompress(remoteData)
    except:
        pass
    nDataBytes += len(remoteData)
    # checks if there is an OAI error
    mo = re.search('<error *code=\"([^"]*)">(.*)</error>', remoteData)
    if mo:
        print "OAIERROR: code=%s '%s'" % (mo.group(1), mo.group(2))
    else:
        return remoteData
