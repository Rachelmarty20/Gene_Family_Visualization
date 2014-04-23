#!/usr/bin/python

# Script to insert HGNC gene family data into mysql database
# input: genefam_list.txt
# output: gene families and genes in databse

import MySQLdb
import os

#connect to db
db = MySQLdb.connect("localhost","root","quaker22","gene" )

#setup cursor
cursor = db.cursor()

# open file to read
f = file('genefam_list.txt', 'r')

sql = "INSERT INTO gene_fam (gene, family_name, family_abrev) VALUES (%s, %s, %s);" 

# iterate over the lines in the file
for line in f:

    # split the line into a list of column values
    columns = line.split("	")

    #cursor.execute("INSERT INTO gene_fam (gene, family_name, family_abrev) VALUES (one, two, three);")

    # ensure the column has at least one value before printing
    if len(columns) > 2:
    	sql = "INSERT INTO gene_fam (gene, family_name, family_abrev) VALUES " + 
    		"('%s', '%s', '%s')" % (columns[3], columns[2], columns[1]) 

    try:
    	cursor.execute(sql)
    	db.commit()
    except:
    	db.rollback()	

db.commit()
db.close()