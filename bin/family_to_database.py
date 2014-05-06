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
'''
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
	print family
'''	
for i in len(1):
	# drop table if already exists
	sql_drop = "DROP TABLE " + ANKRD + ";"
	#sql_drop = "DROP TABLE " + family + ";"
	# create a table in the database with the abreviated family name
	#sql_tables = "CREATE TABLE " + "'" + family + "'" + "(id varchar(20), name varchar(60), chr int, start_loc int, end_loc int, summary nvarchar(MAX));"
	sql_tables = "CREATE TABLE " + 'ANKRD' + "(id varchar(20), name varchar(60), chr int, start_loc int, end_loc int, summary nvarchar(MAX));"
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
		var_1 = int(uid_comp)
		var_2 = i # name of gene
		if "ChrLoc" in record[0]["GenomicInfo"][0]:
			var_3 = record[0]["GenomicInfo"][0]["ChrLoc"] # chromosome
		else:
			var_3 = ''
		var_4 = int(record[0]["GenomicInfo"][0]["ChrStart"]) # start loc
		var_5 = int(record[0]["GenomicInfo"][0]["ChrStop"]) #end loc
		var_6 = record[0]["Summary"] # summary
		#insert into family table
		#print var_1
		print var_2
		#print var_3
		#print var_4
		#print var_5
		#print var_6
		sql_family = "INSERT INTO " + "'" + family + "'" + " (id, name, chr, start_loc, end_loc, summary) VALUES " + "('%d', '%s', '%s', '%d', '%d', '%s');" % (var_1, var_2, var_3, var_4, var_5, var_6) 
		try:
			cursor.execute(sql_family)
			db.commit()
		except:
			db.rollback()	
		'''
		# drop table if exists
		sql_drop = "DROP TABLE " + i + ";"
		# create a table for each gene to hold sequences
		sql_tables = "CREATE TABLE " + "'" + i + "'" + "(nuc_seq nvarchar(MAX), aa_seq nvarchar(MAX));"
		try:
			cursor.execute(sql_family)
			db.commit()
		except:
			db.rollback()
		# find ids in nucleotide database
		handle = Entrez.elink(dbfrom="gene", db="nuccore", id=uid_comp)
		record = Entrez.read(handle)
		num_of_seqs = len(record[0][u'LinkSetDb'][0][u'Link'])
		print num_of_seqs
		for seq in record[0][u'LinkSetDb'][0][u'Link']:
			seq_id = seq[u'Id']
			print seq_id 
			if seq_id != '568815361':
				handle = Entrez.efetch(db="nuccore", id=seq_id, rettype="XML", retmode="XML") #rettype was gb
				record_seq = Entrez.read(handle, validate = False)
				#nuc_seq = record_seq[0][u'GBSeq_sequence']
				if record_seq[u'Bioseq-set_seq-set'][0].has_key(u'Seq-entry_set'):
					print "in loop"
					nuc_seq = record_seq[u'Bioseq-set_seq-set'][0][u'Seq-entry_set'][u'Bioseq-set'][u'Bioseq-set_seq-set'][0][u'Seq-entry_seq'][u'Bioseq'][u'Bioseq_inst'][u'Seq-inst'][u'Seq-inst_seq-data'][u'Seq-data'][u'Seq-data_iupacna'][u'IUPACna']
					print nuc_seq
					#aa_seq = record_seq[0][u'GBSeq_feature-table'][5][u'GBFeature_quals'][9][u'GBQualifier_value'] 
					aa_seq = record_seq[u'Bioseq-set_seq-set'][0][u'Seq-entry_set'][u'Bioseq-set'][u'Bioseq-set_seq-set'][1][u'Seq-entry_seq'][u'Bioseq'][u'Bioseq_inst'][u'Seq-inst'][u'Seq-inst_seq-data'][u'Seq-data'][u'Seq-data_iupacaa'][u'IUPACaa']
					print aa_seq
					sql_seq = "INSERT INTO " + "'" + seq + "'" + " (nuc_seq, aa_seq) VALUES (" + nuc_seq + ", " + aa_seq + ");"
					try:
						cursor.execute(sql_family)
						db.commit()
					except:
						db.rollback()
'''
db.close()


#[{u'Id': '608785222'}, {u'Id': '608785220'}, {u'Id': '608785218'}, {u'Id': '578809822'}, {u'Id': '568815593'}, {u'Id': '568815331'}, {u'Id': '528476642'}, {u'Id': '528475572'}, {u'Id': '299115949'}, {u'Id': '219519609'}, {u'Id': '162319315'}, {u'Id': '157734151'}, {u'Id': '157696490'}, {u'Id': '157169617'}, {u'Id': '71515362'}, {u'Id': '18873825'}, {u'Id': '16258977'}, {u'Id': '6483302'}]
	
 	