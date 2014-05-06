#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"

# Goal: create Json files from database data to be parsed by d3
import MySQLdb
import Bio
import os
from Bio import Entrez
import json 

def get_seqs(gene):
	#connect to db
	db = MySQLdb.connect("localhost","root","quaker22","gene" )

	#setup cursor
	cursor = db.cursor()

	#sizes of all of the chromosomes
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

	families = []
	#return the family_abrev of the gene
	try:
		sql_families = "SELECT family_abrev FROM gene_fam WHERE gene = " + "'" + gene + "'" + ";"
		#print sql_genes
	   	# Execute the SQL command
		cursor.execute(sql_families)
		# Fetch all the rows in a list
		results = cursor.fetchall()
		for row in results:
			families.append(row[0])
#			print row[0]
	except:
	   print "Error: unable to fetch data"

	#get the location of the gene from the table of the gene family 
	try:
		sql_loc = "SELECT chr, start_loc FROM " + "'" + families[0] + "'" + " WHERE gene = " + "'" + gene + "'" + ";"
		#print sql_genes
	   	# Execute the SQL command
		cursor.execute(sql_loc)
		# Fetch all the rows in a list
		results = cursor.fetchall()
		print results
		for row in results:
			chr_main = row[0]
			start_main = row[1]
#			print row[0]
	except:
	   print "Error: unable to fetch data"

	#


	

	#json.dumps(obj)






