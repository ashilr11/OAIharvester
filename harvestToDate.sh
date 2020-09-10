# Ashil Ramjee
# Bash Script to run the harvester component of the HERIPORT project
# Run as a Cron job

# Harvest files from ** in the file named dc.xml from the last date harvested.
# Date stored in the directory date in the text file date.txt
python2 listRecords.py -l http://oai.openedition.org/ -o dcXML/dc.xml -f $(head -n 1 date/date.txt)
echo Metadata retrieved.

# Run dc2solr.py to perform the conversion
python2 dc2solr.py
echo Metadata converted to solr ready xml.

# Index xml files into solr
solr/bin/post -c Test2 solrXML/*.xml
rm solrXML/*
echo Metadata indexed into solr.

# Update date file
> date/date.txt
echo "$(date +'%Y-%m-%d')" >> date/date.txt
echo Dates updated
