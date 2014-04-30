#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"
print "<html> Hello world!</html>" 

#Script to find locations of genes in genome
#input: list of info about the selected gene, list of info about gene family
#ouput: json or tsv file 

import MySQLdb
import Bio
import os
from Bio import Entrez
import json

#store the locations