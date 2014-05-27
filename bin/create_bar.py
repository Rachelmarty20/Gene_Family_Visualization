#!/usr/bin/python

import csv
import local_alignment


def bar(gene, chr_main, start_main, nuc_main, aa_main, family, seqs):
	myfile = open('../data/genes.csv', 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

	#family.append([chr_sib, start_sib, chr_same, chr_dist, name, summary])
	#seqs.append([name, chr, store_nuc, nuc_score, store_aa, aa_score])

	#remove all genes in family and seqs that are on a different chromosome
	for fam in family:
		if(fam[0] != chr_main):
			family.remove(fam)

	for seq in seqs:
		if(seq[1] != chr_main):
			seqs.remove(seq)

	print family

	#sort by starting location of start_sib
	family.sort(key=lambda x: x[1])

	print family

	#create a diction of seqs so they are searchable
	seqs_lib = {}
	for seq in seqs:
		seq_lib[seq[0]] = seq

	seqs_sorted = []
	#sort seqs according to names in family
	for fam in family:
		seqs_sorted.append(seqs_lib[fam[4]])

	#create header list and insert into csv
	header_list = []
	header_list.append("Gene and Location")
	for fam in family:
		header_list.append(fam[4] + "-" + fam[1])
	wr.writerow(header_list)

	for fam in family:
		dist_list = []
		dist_list.append(fam[4] + "-" + fam[1])
		counter = 0
		for i in family:
			if i != fam:
				nuc_score = local_alignment.loc_align(seqs_sorted[counter][2], nuc_main, 1, -3, -2, -1)
				dist_list.append(nuc_score)
			else:
				dist_list.append(0)	
			counter = counter + 1
		wr.writerow(dist_list)	

















