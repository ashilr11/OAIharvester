# Ashil Ramjee
# Python OAI harvester for Get Record
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
    parser.add_option("-m", "--mdprefix", dest="mdprefix", default="oai_dc", help="use the specified metadata format")
    parser.add_option("-i", "--identifier", dest="identifier", help="specify the identifier")
    (options, args) = parser.parse_args()

    if options.link is None or options.filename is None:
        parser.print_help()
        parser.error("a repository url and output file are required")

    # Form the verb for the request
    if options:
        serverString = verbOpts = identifier = mdPrefix = ''
        if options.link:
            serverString = options.link
        if options.filename:
            outFileName = options.filename
        if options.identifier:
            identifier = options.identifier
        if options.mdprefix:
            mdPrefix = options.mdprefix
    else:
        print usage

    if not serverString.startswith('http'):
        serverString = 'http://' + serverString
    print "Writing records to %s from archive %s" % (outFileName, serverString)

    # create a file that it writes the XML to
    ofile = codecs.lookup('utf-8')[-1](file(outFileName, 'wb'))
    ofile.write('<repository xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" \
     xmlns:dc="http://purl.org/dc/elements/1.1/" \
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')

    if identifier:
        verbOpts += '&identifier=%s' % identifier
    if mdPrefix:
        verbOpts += '&metadataPrefix=%s' % mdPrefix
    print "Using url:%s" % serverString + '?GetRecord' + verbOpts

    data = getFile(serverString, 'GetRecord' + verbOpts)
    recordCount = 0
    events = xml.dom.pulldom.parseString(data)
    for (event, node) in events:
        if event == "START_ELEMENT" and node.tagName == 'record':
            events.expandNode(node)
            node.writexml(ofile)
            recordCount += 1
    ofile.write('\n</repository>\n'), ofile.close()
    print "Wrote out %d records" % recordCount
