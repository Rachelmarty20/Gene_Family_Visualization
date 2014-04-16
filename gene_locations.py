#Script to find locations of genes in genome
# ~/anaconda/bin/python
from bio import

#input: gene family
#ouput: json or tsv file 


#http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
#access database containing gene families
#return all of the genes within that gene family
family = "AKR" 
gene1 = "AKR1C4"
gene2 = "AKR1D1"
# might want to put all of the genes in that gene family into a list


#seach using biopython to find locations of the genes on the genome

#store the locations