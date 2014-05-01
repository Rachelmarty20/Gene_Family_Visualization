#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"


#script to create list of information on a gene family

#input: gene
#output: gene information and gene family information

import MySQLdb
import Bio
import os
from Bio import Entrez



def gene_information(gene):

	#gene will eventually become an input parameter
#	gene = 'CDH10'

	#connect to db
	db = MySQLdb.connect("localhost","root","quaker22","gene" )

	#setup cursor
	cursor = db.cursor()

	#find all gene families to which the gene belongs
	families = []
	sql_fam = "SELECT family_abrev FROM gene_fam WHERE gene = " + "'" + gene + "'" + ";"
	try:
	   # Execute the SQL command
	   cursor.execute(sql_fam)
	   # Fetch all the rows in a list
	   results = cursor.fetchall()
	   for row in results:
	      families.append(row[0])
#	      print row[0]
	except:
	   print "Error: unable to fetch data"

	#store first family
	family_1 = families[0]

	#return all of the genes within the same gene family as the origninal gene
	genes = []
	try:
		sql_genes = "SELECT gene FROM gene_fam WHERE family_abrev = " + "'" + family_1 + "'" + ";"
	   	# Execute the SQL command
		cursor.execute(sql_genes)
		# Fetch all the rows in a list
		results = cursor.fetchall()
		for row in results:
			genes.append(row[0])
#			print row[0]
	except:
	   print "Error: unable to fetch data"

	db.close()

	#might need to add a column to db for ncbi entrez id 
	'''Need from entrez:
			how am I going to create the family tree?
			maybe do a separate rna, dna and protein comparisons for sequences? 
			http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec118
			gives directions to pull related information from other databases
			json, python converter
	'''
	# create data structure or send to mysql db?
	gene_orig = [] # gene name, chromosome, start loc, end loc, description, ect. 

	# enter entrez
	Entrez.email = "ramarty@ucsd.edu"

	# handle call
	handle = Entrez.esearch(db = "gene", term = gene + '[gene] AND human[Orgn]')

	# set as record
	record = Entrez.read(handle)

	# pull UID
	uid_orig = int(record["IdList"][0])

	# handle call
	handle = Entrez.esummary(db="gene", id=uid_orig)
	#handle = Entrez.efetch(db="gene", id=['1008'], retmode = "XML")

	# set as record
	record = Entrez.read(handle)

	# add elements to gene_orig
	gene_orig.append(gene) # gene name
	#gene_orig.append(record[]) # gene type
	gene_orig.append(int(record[0]["GenomicInfo"][0]["ChrLoc"])) # chromosome
	gene_orig.append(int(record[0]["GenomicInfo"][0]["ChrStart"])) # start loc
	gene_orig.append(int(record[0]["GenomicInfo"][0]["ChrStop"])) # end loc
	gene_orig.append(record[0]["Summary"]) # description


	#create data structure or send to mysql db?
	gene_comp = [] # gene name, chromosome, start loc, end loc, summary
	for i in genes:
		# handle call to find UID
		handle = Entrez.esearch(db = "gene", term = i + '[gene] AND human[Orgn]')
		# set as record
		record = Entrez.read(handle)
		# pull UID
		uid_comp = int(record["IdList"][0])
		# handle call
		handle = Entrez.esummary(db="gene", id=uid_comp)
		# set as record
		record = Entrez.read(handle)
		# add elements to gene_comp
		var_1 = i # gene name
		var_2 = int(record[0]["GenomicInfo"][0]["ChrLoc"]) # chromosome
		var_3 = int(record[0]["GenomicInfo"][0]["ChrStart"]) # start loc
		var_4 = int(record[0]["GenomicInfo"][0]["ChrStop"]) #end loc
		var_5 = record[0]["Summary"] # summary
		gene_comp.append([var_1, var_2, var_3, var_4, var_5])

#	return gene_orig, gene_comp
 	print gene_orig

#call main method
if __name__ == '__main__':
        gene_information('CDH10')



