#!/usr/bin/python

# Script to create a new table in database for each gene and populate it
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
	print family
	
	#sql_genes = "SELECT gene FROM gene_fam WHERE family_abrev = ';"
	sql_genes = "SELECT gene FROM gene_fam WHERE family_abrev = " + "'" + family + "'" + ";"
	#print sql_genes
	try:
	   	# Execute the SQL command
		cursor.execute(sql_genes)
		# Fetch all the rows in a list
		results = cursor.fetchall()
	except:
	   print "Error: unable to fetch data"
	#for genes not already in database
	genes = []
	for row in results:
		genes.append(row[0])
#		print row[0]

	# enter entrez
	Entrez.email = "ramarty@ucsd.edu"

	for i in genes:
		print i
		#try efetch for gene database
		handle = Entrez.esearch(db = "gene", term = i + '[gene] AND human[Orgn]')
		# set as record
		record = Entrez.read(handle)
		#print record
		#pull UID
		uid_comp = int(record["IdList"][0])
		#print uid_comp
		# drop table if exists
		sql_drop = "DROP TABLE " + i + ";"
		print sql_drop
		try:
			cursor.execute(sql_drop)
			db.commit()
		except:
			db.rollback()
		# create a table for each gene to hold sequences
		sql_tables = "CREATE TABLE " + i + "(nuc_seq text, aa_seq text);"
		print sql_tables
		try:
			cursor.execute(sql_tables)
			db.commit()
		except:
			db.rollback()
		# find ids in nucleotide database
		#which database should I be using???
		handle = Entrez.elink(dbfrom="gene", db="nucleotide", id=uid_comp)
		record = Entrez.read(handle)
		#print record
		try:
			num_of_seqs = len(record[0][u'LinkSetDb'][1][u'Link'])
			print num_of_seqs
			for seq in record[0][u'LinkSetDb'][1][u'Link']:
				seq_id = seq[u'Id']
				#print seq_id 
				#if seq not in tables?
				#if seq_id != '568815361':
				handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="XML", retmode="XML") #rettype was gb
				record_seq = Entrez.read(handle, validate = False)
				#print record_seq[u'Bioseq-set_seq-set'][0]
				#nuc_seq = record_seq[0][u'GBSeq_sequence']
				nuc_seq = record_seq[u'Bioseq-set_seq-set'][0][u'Seq-entry_set'][u'Bioseq-set'][u'Bioseq-set_seq-set'][0][u'Seq-entry_seq'][u'Bioseq'][u'Bioseq_inst'][u'Seq-inst'][u'Seq-inst_seq-data'][u'Seq-data'][u'Seq-data_iupacna'][u'IUPACna']
				nuc_seq = str(nuc_seq)
				#print nuc_seq
				#aa_seq = record_seq[0][u'GBSeq_feature-table'][5][u'GBFeature_quals'][9][u'GBQualifier_value'] 
				aa_seq = record_seq[u'Bioseq-set_seq-set'][0][u'Seq-entry_set'][u'Bioseq-set'][u'Bioseq-set_seq-set'][1][u'Seq-entry_seq'][u'Bioseq'][u'Bioseq_inst'][u'Seq-inst'][u'Seq-inst_seq-data'][u'Seq-data'][u'Seq-data_iupacaa'][u'IUPACaa']
				aa_seq = str(aa_seq)
				#print aa_seq
				#sql_seq = "INSERT INTO " + i + " (nuc_seq, aa_seq) VALUES (" + nuc_seq + ", " + aa_seq + ");"
				sql_seq = "INSERT INTO " + i + " VALUES (" + "'" + nuc_seq + "'" + ", " + "'" + aa_seq + "'" + ");"
				print sql_seq
				cursor.execute(sql_seq)
				db.commit()
		except:
			#why errors for some and not others??
			db.rollback()
			print "error"

db.close()






