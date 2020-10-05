# Ashil Ramjee
# Python OAI harvester for Identify Verb
# See licenses.txt for licenses
# See ReadMe for installion and running information

import sys
import urllib2
import zlib
import time
import re
import xml.dom.pulldom
import operator
import codecs
from optparse import OptionParser
from httpRequest import getFile

if __name__ == "__main__":

    # Set command line options
    parser = OptionParser()
    parser.add_option("-l", "--link", dest="link", help="URL of repository")
    parser.add_option("-o", "--filename", dest="filename", help="write repository to file")
    (options, args) = parser.parse_args()

    if options.link is None or options.filename is None:
        parser.print_help()
        parser.error("a repository url and output file are required")

    # Form the verb for the request
    if options:
        serverString = ''
        if options.link:
            serverString = options.link
        if options.filename:
            outFileName = options.filename
    else:
        print usage

    if not serverString.startswith('http'):
        serverString = 'http://' + serverString
    print "Writing sets to %s from archive %s" % (outFileName, serverString)

    # create a file that it writes the XML to
    ofile = codecs.lookup('utf-8')[-1](file(outFileName, 'wb'))
    ofile.write('<repository xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" \
     xmlns:dc="http://purl.org/dc/elements/1.1/" \
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
    print "Using url:%s" % serverString + '?Identify'

    data = getFile(serverString, 'Identify')
    recordCount = 0
    events = xml.dom.pulldom.parseString(data)
    for (event, node) in events:
        if event == "START_ELEMENT" and node.tagName == 'Identify':
            events.expandNode(node)
            node.writexml(ofile)
            recordCount += 1
    ofile.write('\n</repository>\n'), ofile.close()
    print "Wrote out repository information"
