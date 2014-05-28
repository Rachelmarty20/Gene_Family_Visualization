#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"

# Goal: create Json files from database data to be parsed by d3
import MySQLdb
import Bio
import os
from Bio import Entrez
from Bio import pairwise2
from Bio.pairwise2 import _align
import json 
from Bio.SubsMat import MatrixInfo as matlist
import local_alignment
#import create_bar


#add error statements that print to main page if error occurs; also a success statement
#genes that work: CDH11, APOD, APOL3!!!!, 

form = cgi.FieldStorage()
mygene = form.getvalue("mygene")
#mygene = "CDH11"
#print mygene
#print 'hello'


def get_seqs(gene):
	#connect to db
	db = MySQLdb.connect("localhost","root","quaker22", "gene")

	#setup cursor
	cursor = db.cursor()

	try:
		f = open("/var/www/html/Gene_Family_Visualization/data/flare.json", "w")
	except:
		print "couldn't open"

	searched_genes = []
	#query to get tables
	sql_query = "SELECT gene FROM existing;"
#	print sql_families
	try:
	   	# Execute the SQL command
		cursor.execute(sql_query)
		# Fetch all the rows in a list
		results = cursor.fetchall()
		for row in results:
			searched_genes.append(row[0])
	except:
	   print "Error: unable to fetch data 0"
	#if to check if gene has already been searched

	try:
		searched_genes.remove("CDH11")
	except:
		print "couldn't remove"
	#!!!!!!!!! change back
	if gene in searched_genes:
		sql_fetch = "SELECT object FROM existing WHERE gene = " + "'" + gene + "'" + ";"
		#print sql_fetch
		try:
		   	# Execute the SQL command
			cursor.execute(sql_fetch)
			# Fetch all the rows in a list
			results = cursor.fetchall()
			output = results[0]
			output = str(output)
			output = output[2:-3]
			output = output.replace("'", '"')
			#print output
		except:
		  print "This gene provides too much data for a helpful visualization. Please try another gene."
		  return
		#json.dump(output, f)
		f.write(output)
	else:
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

		#assign variables that will be given real values later
		chr_main = 0
		start_main = 0
		chr_sib = 0
		start_sib = 0
		bucket_size = 0
		chr_dist = 0
		store_main = 0
		store_sib = 0
		counter = 0
		nuc_score = 0
		aa_score = 0
		name = ''
		summary = ''
		name_main = ''
		summary_main = ''
		store_nuc = ''
		store_aa = ''
		matrix = matlist.blosum62

		families = []
		#return the family_abrev of the gene
		sql_families = "SELECT family_abrev FROM gene_fam WHERE gene = " + "'" + gene + "'" + ";"
	#	print sql_families
		try:
		   	# Execute the SQL command
			cursor.execute(sql_families)
			# Fetch all the rows in a list
			results = cursor.fetchall()
			for row in results:
				families.append(row[0])
	#			print row[0]
		except:
		   print "This gene is not currently in our database. Please try another gene."
		   return

		#get the location of the gene from the table of the gene family
		sql_loc = "SELECT chr, start_loc, name, summary FROM " + families[0] + " WHERE name = " + "'" + gene + "'" + ";"
	#	print sql_loc 
		try:
		   	# Execute the SQL command
			cursor.execute(sql_loc)
			# Fetch all the rows in a list
			results = cursor.fetchall()
			#print results
			#print len(results)
			for row in results:
				chr_main = int(row[0])
				print chr_main
				start_main = int(row[1])
				print start_main
				name_main = str(row[2])
				summary_main = str(row[3])
		except:
		   print "This gene is not currently in our database. Please try another gene."
		   return 

		#get sequences of main gene, need to change select statement!!!!!!!!!!!!!!!!!!
		sql_seq = "SELECT nuc_seq, aa_seq FROM " + name_main + ";"
		print sql_seq
		try:
		   	# Execute the SQL command
			cursor.execute(sql_seq)
			# Fetch all the rows in a list
			results = cursor.fetchall()
			#print results
			#print len(results)
		except:
		   print "Our database does not contain the sequences necessary for the visualization. Please try another gene."
		   return
		for row in results:
			nuc_main = str(row[0])
			print nuc_main
			aa_main = str(row[1])
			print aa_main

		#print chr_main
		#print start_main

		#determine which chromosome we are working with, declare it as chromosome
		if chr_main == 1:
			chromosome = chr1
		elif chr_main == 2:
			chromosome = chr2
		elif chr_main == 3:
			chromosome = chr3
		elif chr_main == 4:
			chromosome = chr4
		elif chr_main == 5:
			chromosome = chr5
		elif chr_main == 6:
			chromosome = chr6
		elif chr_main == 7:
			chromosome = chr7
		elif chr_main == 8:
			chromosome = chr8
		elif chr_main == 9:
			chromosome = chr9
		elif chr_main == 10:
			chromosome = chr10
		elif chr_main == 11:
			chromosome = chr11
		elif chr_main == 12:
			chromosome = chr12
		elif chr_main == 13:
			chromosome = chr13
		elif chr_main == 14:
			chromosome = chr14
		elif chr_main == 15:
			chromosome = chr15
		elif chr_main == 16:
			chromosome = chr16
		elif chr_main == 17:
			chromosome = chr17
		elif chr_main == 18:
			chromosome = chr18
		elif chr_main == 19:
			chromosome = chr19
		elif chr_main == 20:
			chromosome = chr20
		elif chr_main == 21:
			chromosome = chr21
		elif chr_main == 22:
			chromosome = chr22
		elif str(chr_main) == 'X':
			chromosome = chrX
		else:
			chromosome = chrY
						 
	#	print chromosome
		#find bucket size
		bucket_size = int(chromosome/1000)
		bucket_size_store = bucket_size
		#print bucket_size
		#start_main = start_main/1000

		#find main_num, between 1-100
		for i in range(1000):
			if(bucket_size > start_main):
				store_main = i
				break
			else:
				bucket_size = bucket_size + bucket_size_store
		#print "store_main: " + str(store_main)


		#get the locations of the genes in the rest of the gene family
		family = []
		sql_loc2 = "SELECT chr, start_loc, name, summary FROM " + families[0] + " WHERE name <> " + "'" + gene + "'" + ";"
		#print sql_loc2
		try:
		   	# Execute the SQL command
			cursor.execute(sql_loc2)
			# Fetch all the rows in a list
			results = cursor.fetchall()
			#print results
		except:
		   print "Error: unable to fetch data 4"	   

		for row in results:
			bucket_size = bucket_size_store
			store_sib = 0
			chr_sib = int(row[0])
			#print "one " + str(row[0])
			start_sib = int(row[1])
			#print "two " + str(row[1])
			if (chr_sib == chr_main):
				chr_same = 1
				#determine the bucket that the gene belongs in
				for i in range(1000):
					if(bucket_size > start_sib):
						store_sib = i
						break
					else:
						bucket_size = bucket_size + bucket_size_store
				chr_dist = (1000 - abs(store_main - store_sib))
				#print chr_dist
			else:
				chr_same = 0
			name = row[2]
			summary = row[3]
			#equation to determine distance metric of 
			family.append([chr_sib, start_sib, chr_same, chr_dist, name, summary])

		print family
		

		seqs = []
		for fam in family:
			#print fam[4]
			if(fam[2] == 0):
				fam[3] = 100
			
			#get sequences (nuc and aa) for each gene
			sql_seqs = "SELECT nuc_seq, aa_seq FROM " + fam[4] + ";"
			#print sql_seqs
			try:
			   	# Execute the SQL command
				cursor.execute(sql_seqs)
				# Fetch all the rows in a list
				results = cursor.fetchall()
				#print results
			except:
				print "Our database does not contain the sequences necessary for the visualization. Please try another gene."
				return
			for row in results:
				#print row
				store_nuc = row[0]
				store_aa = row[1]
				#compare sequences!!!!!!!!!!!!!!!
				nuc_score = local_alignment.loc_align(store_nuc, nuc_main, 1, -3, -2, -1)
				#print nuc_score
				#print "store_aa: " + store_aa
				#print "aa_main: " + aa_main
				#compare amino acid sequences
				aa_score = local_alignment.loc_align(store_aa, aa_main, 1, -3, -2, -1)
				#aa_score = local_alignment.loc_align(store_aa, aa_main, 1 -2, -1.5, -1)
				#print aa_score
				#appending gene name, chromosome, nucleotide sequence, nuc_score, amino acid sequence, aa_score
				#seqs.append(fam[4], fam[0], store_nuc, nuc_score, store_aa, aa_score)
				try:
					#use an ftp client to download emboss?
					seqs.append([fam[4], fam[0], store_nuc, nuc_score, store_aa, aa_score])
					#print "successfully added"
				except:
					print "couldn't append to seq"

		print seqs
		try:
			#create main dictionary object
			obj = {}

			#to track node numbers
			tracker = {}
			count = 1
			#create node list of dictionary
			node = []
			#first, make the initial zero node, all will be attached to it
			node.append({'name':name_main, 'size':10000, 'chromosome':(chr_main)})
			#start by making all of the inital distance nodes
			for i in family:
				#create individual dictionaries for each node
				node.append({'name':i[4], 'size':(i[3]*10), 'chromosome':(i[0])})
				#create a dictionary to keep name and node number!
				tracker[i[4]] = count
				count = count + 1
			#create link list of dictionary
			link = []
			#start by linking all nodes in family to node [0]
			#put names in nuc and protein in order to be able to link them
			counter = 0
			for i in family:
				counter = counter + 1
				#create individual dictionaries for each link
				link.append({'source':0, 'target':(counter), 'value':(3)})

			node_num = len(node)
			try:
				#create loop for seq; maybe two for nuc and aa
				for i in seqs:
					#keep a counter to know numbers of these nodes to link them
					node.append({'name':(i[0] + " transcript"), 'size':(i[3]*300), 'chromosome':i[1]})
					link.append({'source':tracker[i[0]], 'target':(node_num), 'value':(3)})
					node.append({'name':(i[0] + "protein"), 'size':(i[5]*300), 'chromosome':i[1]})
					link.append({'source':(node_num), 'target':(node_num + 1), 'value':(3)})
					#must change back to 2
					node_num = node_num + 2
			except:
				print "couldnt do sequences"


			#create links betweeen all of the different levels

			#add node and link into obj
			obj['nodes'] = node
			obj['links'] = link

			#print obj, write to json file
			#print obj
			json.dump(obj, f)
		except:
			print "couldn't build object"
		#insert into database
		sql_insert = "INSERT INTO existing (gene, object, chr_main, start_main, nuc_main, aa_main, family, seqs) VALUES " + '("%s","%s","%d","%d","%s","%s","%s","%s");' % (gene, obj, chr_main, start_main, nuc_main, aa_main, family, seqs)
		#print sql_insert
		try:
				cursor.execute(sql_insert)
				db.commit()
			#	print "success2"
		except:
			db.rollback()	
			print "fail"

#actual stuff
#print "half"
try:
	get_seqs(mygene)
	#get_seqs("CDH11")
#	print "success"
except:
	print "fail"

#print "done"
