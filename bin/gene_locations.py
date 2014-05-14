#!/usr/bin/python
import cgi
print "Content-type: text/html\n\n"

# Goal: create Json files from database data to be parsed by d3
import MySQLdb
import Bio
#import os
from Bio import Entrez
import json 


form = cgi.FieldStorage()
mygene = form.getvalue("mygene")
#mygene = "CD28"
print mygene
print 'hello'


def get_seqs(gene):
	#open file to write json
	f = open('./data/flare.json', 'w')
	print gene
	#to be removed later
	#gene = 'CDH11'

	#connect to db
	db = MySQLdb.connect("localhost","root","quaker22", "gene")

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

	#assign variables that will be given real values later
	chr_main = 0
	start_main = 0
	chr_sib = 0
	start_sib = 0
	bucket_size = 0
	chr_dist = 0
	store_main = 0
	store_sib = 0
	name = ''
	summary = ''

	families = []
	#return the family_abrev of the gene
	sql_families = "SELECT family_abrev FROM gene_fam WHERE gene = " + "'" + gene + "'" + ";"
	print sql_families
	try:
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
	sql_loc = "SELECT chr, start_loc FROM " + families[0] + " WHERE name = " + "'" + gene + "'" + ";"
	print sql_loc 
	try:
	   	# Execute the SQL command
		cursor.execute(sql_loc)
		# Fetch all the rows in a list
		results = cursor.fetchall()
		#print results
		#print len(results)
		for row in results:
			chr_main = int(row[0])
			start_main = int(row[1])
#			print row[0]
	except:
	   print "Error: unable to fetch data"

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
					 
	print chromosome
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
	print sql_loc2
	try:
	   	# Execute the SQL command
		cursor.execute(sql_loc2)
		# Fetch all the rows in a list
		results = cursor.fetchall()
		#print results
	except:
	   print "Error: unable to fetch data"	   

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
			#print "bucket: " + str(bucket_size)
			#print "start_main: " + str(start_main)
			#print "start_sib: " + str(start_sib)
			#print "store_sib: " + str(store_sib)
			#determine size based on subtraction of main_num and sib_num
			#print abs(store_main - store_sib)
			chr_dist = (1000 - abs(store_main - store_sib))
			#print chr_dist
		else:
			chr_same = 0
		name = row[2]
		summary = row[3]
		#equation to determine distance metric of 
		family.append([chr_sib, start_sib, chr_same, chr_dist, name, summary])

	print family

	for fam in family:
		if(fam[2] == 0):
			fam[3] = 30

	#print " "
	#print family

	#create main dictionary object
	obj = {}
	obj['name'] = gene
	temp_main = []
	temp_sub = {}
	#create the dictionary that will be the child of the main gene
	for i in family:
		#create individual dictionaries for each gene
		temp_main.append({'name':i[4], 'size':(i[3]*10)})
	obj['children'] = temp_main

	#print obj, write to json file
	print obj
	#json.dump(obj, f)
	f.write(str(obj))
	return obj



#actual stuff
print "half"
print get_seqs(mygene)
#print get_seqs("CDH11")
print "done"





