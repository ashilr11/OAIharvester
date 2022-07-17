# Ashil Ramjee

To install:
    Download and extract the full zip file of the harvester component.
    Install 'pip2' for python as it may request some packages to be installed.
    To install the package run -> pip2 install 'package name'
    You will also need to install Apache Solr version 7.7.3.
    To install solr, download the tar archive file (.tgz) from the Apache Solr website.
    Extract the file using the command -> tar zxf solr-7.7.3.tgz in the same directory as the python classes
    Rename the solr-7.7.3 directory to solr

To run the whole process on Linux (can be set as a scheduled process using a crontab):
    Go into the same directory that contains the six verb python requests, dc2solr.py, solrXML and the two bash files
    First start a solr instance with the command -> solr/bin/solr start -e cloud
    Choose _default as the config file and choose a name for collection.
    Edit the harvestAll.sh and harvestToDate.sh and change the url to yours and change the name of the collection in the POST command for solr
    Run the command to harvest, convert and index all records-> ./harvestAll.sh
    To use selective harvesting: First harvest all records using the command above,
    Next, update date.txt to the current date in the format YYYY-MM-DD.
    Lastly, run the command -> ./harvestToDate.sh
    This will update the date text file each time its run. It uses the date as a 'from' parameter for ListRecords

To specifically run each OAI harvester verbs:
    ListRecords:
        Run the command with required options-> python2 listRecords.py -l theURL -o NameOfOutputFile -m metadataPrefix
        Run the command with required and optional options-> python2 listRecords.py -l theURL -o NameOfOutputFile -i identifier -m metadataPrefix -f from -u until -s set
        An example -> python2 listRecords.py -l http://oai.openedition.org/ -o dcXML/dc.xml -m oai_dc

    ListSets:
        Run the command with required options-> python2 listSets.py -l theURL -o NameOfOutputFile
        An example -> python2 listSets.py -l http://oai.openedition.org/ -o dcXML/dc.xml

    ListIdentifiers:
        Run the command with required options-> python2 listIdentifiers.py -l theURL -o NameOfOutputFile -m metadataPrefix
        Run the command with required and optional options-> python2 listIdentifiers.py -l theURL -o NameOfOutputFile -i identifier -m metadataPrefix -f from -u until -s set
        An example -> python2 listIdentifiers.py -l http://oai.openedition.org/ -o dcXML/dc.xml -m oai_dc

    ListMetadataFormats:
        Run the command with required options-> python2 listMetadataFormats.py -l theURL -o NameOfOutputFile
        Run the command with required and optional options-> python2 listMetadataFormats.py -l theURL -o NameOfOutputFile -i identifier
        An example -> python2 listMetadataFormats.py -l http://oai.openedition.org/ -o dcXML/dc.xml

    Identify:
        Run the command with required options-> python2 identify.py -l theURL -o NameOfOutputFile
        An example -> python2 identify.py -l http://oai.openedition.org/ -o dcXML/dc.xml

    GetRecord:
        Run the command with required options-> python2 getRecord.py -l theURL -o NameOfOutputFile -i identifier -m metadataprefix
        For example: python2 getRecord.py -l http://oai.openedition.org/ -o dcXML/dc.xml -i story2 -m oai_dc

To run the conversion of dc XML to Solr XML:
    Make sure the harvested XML files are in the dcXML folder.
    Run the command -> python dc2solr.py
    Converted Solr XML files will be in the solrXML folder.

To run command to index the files:
    Make sure the Solr Ready XML files are in are in solrXML
    Run the command to index them into Solr -> solr/bin/post -c collectionName solrXML/*.xml
    Edit the command above to specify your collection name
