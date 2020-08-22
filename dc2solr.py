# Ashil Ramjee
# Python script to change OAIXML to Solr Ready XML

import os
import sys
import xml.etree.ElementTree as ET
import urllib, urllib2
from string import Template
import time

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def transformFiles(saxonLocation):
	#transform OAI XML to Solr indexing XML
	fileList = listdir_fullpath('./dcXML')
	for file in fileList:
		outputFile = "." + file.split(".")[1] + "_Solr.xml"
		cs = 'java -jar {saxonLocation} -s:{file} -xsl:dc2solr.xsl -o:{outputFile}'.format(file=file, outputFile=outputFile, saxonLocation=saxonLocation)
		try:
			os.system(cs)
			print file,"processed."
		except:
			#this should include a logging event
			print file,"had errors and did NOT process."

	#move all files to solrXML
	os.system("mv ./dcXML/*_Solr.xml ./solrXML/")

if __name__ == "__main__":
	#global vars
	saxonLocation = "saxon-he-10.1.jar"

	#timer
	startTime = int(time.time())

	transformFiles(saxonLocation)

	#end timer
	endTime = int(time.time())
	totalTime = endTime - startTime
	print "Total seconds elapsed",totalTime
