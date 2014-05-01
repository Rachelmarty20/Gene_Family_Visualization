#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"


#print "<html> Hello world!</html>"
import MySQLdb
import Bio
import os
from Bio import Entrez
import json

def get_seqs(gene_comp):
	#connect to db
	db = MySQLdb.connect("localhost","root","quaker22","gene" )

	#setup cursor
	cursor = db.cursor()




#	Goal: return list of lists; gene name and sequence
#	return 
#Script to find locations of genes in genome
#input: list of info about the selected gene, list of info about gene family
#ouput: json or tsv file 

#import MySQLdb
#import Bio
#import os
#from Bio import Entrez
#import json
#store the locations
