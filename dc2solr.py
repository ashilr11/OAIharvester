# Ashil Ramjee
# Python script to change dc XML to Solr XML

import os
import sys
import xml.etree.ElementTree as ET
import urllib, urllib2
from string import Template
import time

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

# Uses a Saxon XSLT parser to transfrom the dcXML into solr XML
def transformFiles(saxonLocation):
	fileList = listdir_fullpath('./dcXML')
	for file in fileList:
		outputFile = "." + file.split(".")[1] + "_Solr.xml"
		cs = 'java -jar {saxonLocation} -s:{file} -xsl:dc2solr.xsl -o:{outputFile}'.format(file=file, outputFile=outputFile, saxonLocation=saxonLocation)
		try:
			os.system(cs)
			print file,"processed."
		except:
			print file,"had errors and did NOT process."
	os.system("mv ./dcXML/*_Solr.xml ./solrXML/")


if __name__ == "__main__":
	saxonLocation = "saxon-he-10.1.jar"
	startTime = int(time.time())
	transformFiles(saxonLocation)
	endTime = int(time.time())
	totalTime = endTime - startTime
	print "Total seconds elapsed",totalTime
