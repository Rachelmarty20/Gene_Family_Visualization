#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"

# Goal: create Json files from database data to be 
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

	chr1 = 249250621
	chr2 = 243199373
	chr3 = 198022430
	chr4 = 191154276
	chr5 = 180915260
	chr6 = 171115067
	chr7 = 159138663
	chr8 = 146364022
	chr9 = 141213431
	chr10 = 135534747
	chr11 = 135006516
	chr12 = 133851895
	chr13 = 115169878	
	chr14 = 107349540
	chr15 = 102531392	
	chr16 = 90354753	
	chr17 = 81195210	
	chr18 = 78077248
	chr19 = 59128983
	chr20 = 63025520
	chr21 = 48129895
	chr22 = 51304566
	chrX = 155270560
	chrY = 59373566




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
