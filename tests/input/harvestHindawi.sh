# Ashil Ramjee
# Bash Script to run the harvester component of the HERIPORT project
# Run as a Cron job

# Harvest files from ** in the file named dc.xml
python2 listRecords.py -l https://www.hindawi.com/oai-pmh/oai.aspx -o dcXML/hindawi.xml -f 2020-10-01

echo Metadata retrieved.

# Run dc2solr.py to perform the conversion
python2 dc2solr.py
echo Metadata converted to solr ready xml.

# Index xml files into solr
solr/bin/post -c Test2 solrXML/*.xml

echo Metadata indexed into solr.
#rm solrXML/*
