#!/usr/bin/python

# Script to create a new table in database for each gene family and populate it
# with information from ncbi

# input: query of families in database
# output: unique tables for each gene family populated in database

import MySQLdb
import os
import Bio
from Bio import Entrez

#connect to db
db = MySQLdb.connect("localhost","root","quaker22","gene" )

#setup cursor
cursor = db.cursor()

#create an array of gene families to traverse later
families = []
sql_fam = "SELECT distinct family_abrev FROM gene_fam;"
try:
   # Execute the SQL command
   cursor.execute(sql_fam)
   # Fetch all the rows in a list
   results = cursor.fetchall()
   for row in results:
      families.append(row[0])
#     print row[0]
except:
	print "Error: unable to fetch data"

for family in families:
	# drop table if already exists
	sql_drop = "DROP TABLE " + family + ";"
	# create a table in the database with the abreviated family name
	sql_tables = "CREATE TABLE " + "'" + family + "'" + "(id varchar(20), name varchar(60), chr int, start_loc int, end_loc int, summary nvarchar(MAX));"
	
	try:
    	cursor.execute(sql_tables)
    	db.commit()
    	print family
	except:
		db.rollback()	


	#return all of the genes within the same gene family as the origninal gene
	genes = []
	try:
		sql_genes = "SELECT gene FROM gene_fam WHERE family_abrev = " + "'" + family + "'" + ";"
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

	# enter entrez
	Entrez.email = "ramarty@ucsd.edu"

	#create data structure or send to mysql db?
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
		# create variables to hold data to insert
		var_1 = uid_comp
		var_2 = i # name of gene
		var_3 = int(record[0]["GenomicInfo"][0]["ChrLoc"]) # chromosome
		var_4 = int(record[0]["GenomicInfo"][0]["ChrStart"]) # start loc
		var_5 = int(record[0]["GenomicInfo"][0]["ChrStop"]) #end loc
		var_6 = record[0]["Summary"] # summary
		#insert into family table
		sql_family = "INSERT INTO " + "'" + family + "'" + " (id, name, chr, start_loc, end_loc, summary) VALUES (" + var_1 + ", " + var_2 + ", " + var_3 + ", " + var_4 + ", " + var_5 + ", " var_6 + ");"
		try:
	    	cursor.execute(sql_family)
	    	db.commit()
	    except:
	    	db.rollback()	
	
		# drop table if exists
		sql_drop = "DROP TABLE " + seq + ";"
		# create a table for each gene to hold sequences
		sql_tables = "CREATE TABLE " + "'" + seq + "'" + "(nuc_seq nvarchar(MAX), aa_seq nvarchar(MAX));"
		# find ids in nucleotide database
		handle = Entrez.elink.read(Entrez.elink(dbfrom="gene", db="nucleotide", id=uid_comp))
		record = Entrez.read(handle)
		num_of_seqs = len(record[0][u'LinkSetDb'][0][u'Link'])
		for seq in record[0][u'LinkSetDb'][0][u'Link']):
			seq_id seq[u'Id']
			handle_seq = Entrez.efetch(db="nucleotide", id=seq_id, rettype="gb", retmode="XML")
			record_seq = Entrez.read(handle_seq)
			nuc_seq = record_seq[0][u'GBSeq_sequence']
			aa_seq = record[0][u'GBSeq_feature-table'][5][u'GBFeature_quals'][9][u'GBQualifier_value'] 
			sql_seq = "INSERT INTO " + "'" + seq + "'" + " (nuc_seq, aa_seq) VALUES (" + nuc_seq + ", " + aa_seq + ");"

	gene_seqs = gene_locations.get_seqs(gene_comp)

	return gene_orig, gene_comp
 	