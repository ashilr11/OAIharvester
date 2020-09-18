# Ashil Ramjee
# Bash Script to run the harvester component of the HERIPORT project
# Run as a Cron job

# Harvest files from ** in the file named dc.xml
python2 listRecords.py -l http://rafiki1.cs.uct.ac.za/~alex/cgi-bin/BleekAndLloydOAIInterface.py -o dcXML/bl.xml
python2 listRecords.py -l http://rafiki1.cs.uct.ac.za/~alex/cgi-bin/FHYAOAIInterface.py -o dcXML/fhya.xml
python2 listRecords.py -l http://rafiki1.cs.uct.ac.za/~alex/cgi-bin/MetsemegologoloOAIInterface.py -o dcXML/metse.xml
echo Metadata retrieved.

# Run dc2solr.py to perform the conversion
python2 dc2solr.py
echo Metadata converted to solr ready xml.

# Index xml files into solr
solr/bin/post -c Test2 solrXML/*.xml
#rm solrXML/*
echo Metadata indexed into solr.
