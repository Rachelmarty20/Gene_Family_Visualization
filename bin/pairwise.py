#!/usr/bin/python
import os
import sys
import subprocess
import Bio
from Bio.Emboss.Applications import WaterCommandline
cmd = WaterCommandline(gapopen=10, gapextend=0.5)
cmd.asequence = "asis:TCCATTAGGGATGCTTTTTTATAATGCCAACTTTGTACAAAAAAGTTGGCATGAAGGAGAACTACTGTTTACAAGCCGCCCTGGTGTGCCTGGGCATGCTGTGCCACAGCCATGCCTTTGCCCCAGAGCGGCGGGGGCACCTGCGGCCCTCCTTCCATGGGCACCATGAGAAGGGCAAGGAGGGGCAGGTGCTACAGCGCTCCAAGCGTGGCTGGGTCTGGAACCAGTTCTTCGTGATAGAGGAGTACACCGGGCCTGACCCCGTGCTTGTGGGCAGGCTTCATTCAGATATTGACTCTGGTGATGGGAACATTAAATACATTCTCTCAGGGGAAGGAGCTGGAACCATTTTTGTGATTGATGACAAATCAGGGAACATTCATGCCACCAAGACGTTGGATCGAGAAGAGAGAGCCCAGTACACGTTGATGGCTCAGGCGGTGGACAGGGACACCAATCGGCCACTGGAGCCACCGTCGGAATTCATTGTCAAGGTCCAGGACATTAATGACAACCCTCCGGAGTTCCTGCACGAGACCTATCATGCCAACGTGCCTGAGAGGTCCAATGTGGGAACGTCAGTAATCCAGGTGACAGCTTCAGATGCAGATGACCCCACTTATGGAAATAGCGCCAAGTTAGTGTACAGTATCCTCGAAGGACAACCCTATTTTTCGGTGGAAGCACAGACAGGTATCATCAGAACAGCCCTACCCAACATGGACAGGGAGGCCAAGGAGGAGTACCACGTGGTGATCCAGGCCAAGGACATGGGTGGACATATGGGCGGACTCTCAGGGACAACCAAAGTGATGATCACACTGACCGATGTCAATGACAACCCACCAAAGTTTCCGCAGAGCGTATACCAGATGTCTGTGTCAGAAGCAGCCGTCCCTGGGGAGGAAGTAGGAAGAGTGAAAGCTAAAGATCCAGACATTGGAGAAAATGGCTTAGTCACATACAATATTGTTGATGGAGATGGTATGGAATCATTTGAAATCACAACGGACTATGAAACACAGGAGGGGGTGATAAAGCTGAAAAAGCCTGTAGATTTTGAAACCAAAAGAGCCTATAGCTTGAAGGTAGAGGCAGCCAACGTGCACATCGACCCGAAGTTTATCAGCAATGGCCCTTTCAAGGACACTGTGACCGTCAAGATCGCAGTAGAAGATGCTGATGAGCCCCCTATGTTCTTGGCCCCAAGTTACATCCACGAAGTCCAAGAAAATGCAGCTGCTGGCACCGTGGTTGGGAGAGTGCATGCCAAAGACCCTGATGCTGCCAACAGCCCGATAAGGTATTCCATCGATCGTCACACTGACCTCGACAGATTTTTCACTATTAATCCAGAGGATGGTTTTATTAAAACTACAAAACCTCTGGATAGAGAGGAAACAGCCTGGCTCAACATCACTGTCTTTGCAGCAGAAATCCACAATCGGCATCAGGAAGCCAAAGTCCCAGTGGCCATTAGGGTCCTTGATGTCAACGATAATGCTCCCAAGTTTGCTGCCCCTTATGAAGGTTTCATCTGTGAGAGTGATCAGACCAAGCCACTTTCCAACCAGCCAATTGTTACAATTAGTGCAGATGACAAGGATGACACGGCCAATGGACCAAGATTTATCTTCAGCCTACCCCCTGAAATCATTCACAATCCAAATTTCACAGTCAGAGACAACCGAGATAACACAGCAGGCGTGTACGCCCGGCGTGGAGGGTTCAGTCGGCAGAAGCAGGACTTGTACCTTCTGCCCATAGTGATCAGCGATGGCGGCATCCCGCCCATGAGTAGCACCAACACCCTCACCATCAAAGTCTGCGGGTGCGACGTGAACGGGGCACTGCTCTCCTGCAACGCAGAGGCCTACATTCTGAACGCCGGCCTGAGCACAGGCGCCCTGATCGCCATCCTCGCCTGCATCGTCATTCTCCTGGTCATTGTAGTATTGTTTGTGACCCTGAGAAGGCAAAAGAAAGAACCACTCATTGTCTTTGAGGAAGAAGATGTCCGTGAGAACATCATTACTTATGATGATGAAGGGGGTGGGGAAGAAGACACAGAAGCCTTTGATATTGCCACCCTCCAGAATCCTGATGGTATCAATGGATTTATCCCCCGCAAAGACATCAAACCTGAGTATCAGTACATGCCTAGACCTGGGCTCCGGCCAGCGCCCAACAGCGTGGATGTCGATGACTTCATCAACACGAGAATACAGGAGGCAGACAATGACCCCACGGCTCCTCCTTATGACTCCATTCAAATCTACGGTTATGAAGGCAGGGGCTCAGTGGCCGGGTCCCTGAGCTCCCTAGAGTCGGCCACCACAGATTCAGACTTGGACTATGATTATCTACAGAACTGGGGACCTCGTTTTAAGAAACTAGCAGATTTGTATGGTTCCAAAGACACTTTTGATGACGATTCTTACCCAACTTTCTTGTACAAAGTTGGCATTATAAGAAAGCATTGCTTATCAA"
a = "asis:ACCCGGGCGCGGT"
cmd.bsequence = "asis:AGAAGCTAACTGGGGACGTGGGCAGCCCTGACGTGATGAGCTCAACCAGCAGAGACATTCCATCCCAAGAGAGGTCTGCGTGACGCGTCCGGGAGGCCACCCTCAGCAAGACCACCGTACAGTTGGTGGAAGGGGTGACAGCTGCATTCTCCTGTGCCTACCACGTAACCAAAAATGAAGGAGAACTACTGTTTACAAGCCGCCCTGGTGTGCCTGGGCATGCTGTGCCACAGCCATGCCTTTGCCCCAGAGCGGCGGGGGCACCTGCGGCCCTCCTTCCATGGGCACCATGAGAAGGGCAAGGAGGGGCAGGTGCTACAGCGCTCCAAGCGTGGCTGGGTCTGGAACCAGTTCTTCGTGATAGAGGAGTACACCGGGCCTGACCCCGTGCTTGTGGGCAGGCTTCATTCAGATATTGACTCTGGTGATGGGAACATTAAATACATTCTCTCAGGGGAAGGAGCTGGAACCATTTTTGTGATTGATGACAAATCAGGGAACATTCATGCCACCAAGACGTTGGATCGAGAAGAGAGAGCCCAGTACACGTTGATGGCTCAGGCGGTGGACAGGGACACCAATCGGCCACTGGAGCCACCGTCGGAATTCATTGTCAAGGTCCAGGACATTAATGACAACCCTCCGGAGTTCCTGCACGAGACCTATCATGCCAACGTGCCTGAGAGGTCCAATGTGGGAACGTCAGTAATCCAGGTGACAGCTTCAGATGCAGATGACCCCACTTATGGAAATAGCGCCAAGTTAGTGTACAGTATCCTCGAAGGACAACCCTATTTTTCGGTGGAAGCACAGACAGGTATCATCAGAACAGCCCTACCCAACATGGACAGGGAGGCCAAGGAGGAGTACCACGTGGTGATCCAGGCCAAGGACATGGGTGGACATATGGGCGGACTCTCAGGGACAACCAAAGTGATGATCACACTGACCGATGTCAATGACAACCCACCAAAGTTTCCGCAGAGCGTATACCAGATGTCTGTGTCAGAAGCAGCCGTCCCTGGGGAGGAAGTAGGAAGAGTGAAAGCTAAAGATCCAGACATTGGAGAAAATGGCTTAGTCACATACAATATTGTTGATGGAGATGGTATGGAATCATTTGAAATCACAACGGACTATGAAACACAGGAGGGGGTGATAAAGCTGAAAAAGCCTGTAGATTTTGAAACCAAAAGAGCCTATAGCTTGAAGGTAGAGGCAGCCAACGTGCACATCGACCCGAAGTTTATCAGCAATGGCCCTTTCAAGGACACTGTGACCGTCAAGATCGCAGTAGAAGATGCTGATGAGCCCCCTATGTTCTTGGCCCCAAGTTACATCCACGAAGTCCAAGAAAATGCAGCTGCTGGCACCGTGGTTGGGAGAGTGCATGCCAAAGACCCTGATGCTGCCAACAGCCCGATAAGGTATTCCATCGATCGTCACACTGACCTCGACAGATTTTTCACTATTAATCCAGAGGATGGTTTTATTAAAACTACAAAACCTCTGGATAGAGAGGAAACAGCCTGGCTCAACATCACTGTCTTTGCAGCAGAAATCCACAATCGGCATCAGGAAGCCAAAGTCCCAGTGGCCATTAGGGTCCTTGATGTCAACGATAATGCTCCCAAGTTTGCTGCCCCTTATGAAGGTTTCATCTGTGAGAGTGATCAGACCAAGCCACTTTCCAACCAGCCAATTGTTACAATTAGTGCAGATGACAAGGATGACACGGCCAATGGACCAAGATTTATCTTCAGCCTACCCCCTGAAATCATTCACAATCCAAATTTCACAGTCAGAGACAACCGAGATAACACAGCAGGCGTGTACGCCCGGCGTGGAGGGTTCAGTCGGCAGAAGCAGGACTTGTACCTTCTGCCCATAGTGATCAGCGATGGCGGCATCCCGCCCATGAGTAGCACCAACACCCTCACCATCAAAGTCTGCGGGTGCGACGTGAACGGGGCACTGCTCTCCTGCAACGCAGAGGCCTACATTCTGAACGCCGGCCTGAGCACAGGCGCCCTGATCGCCATCCTCGCCTGCATCGTCATTCTCCTGGTCATTGTAGTATTGTTTGTGACCCTGAGAAGGCAAAAGAAAGAACCACTCATTGTCTTTGAGGAAGAAGATGTCCGTGAGAACATCATTACTTATGATGATGAAGGGGGTGGGGAAGAAGACACAGAAGCCTTTGATATTGCCACCCTCCAGAATCCTGATGGTATCAATGGATTTATCCCCCGCAAAGACATCAAACCTGAGTATCAGTACATGCCTAGACCTGGGCTCCGGCCAGCGCCCAACAGCGTGGATGTCGATGACTTCATCAACACGAGAATACAGGAGGCAGACAATGACCCCACGGCTCCTCCTTATGACTCCATTCAAATCTACGGTTATGAAGGCAGGGGCTCAGTGGCCGGGTCCCTGAGCTCCCTAGAGTCGGCCACCACAGATTCAGACTTGGACTATGATTATCTACAGAACTGGGGACCTCGTTTTAAGAAACTAGCAGATTTGTATGGTTCCAAAGACACTTTTGATGACGATTCTTAACAATAACGATACAAATTTGGCCTTAAGAACTGTGTCTGGCGTTCTCAAGAATCTAGAAGATGTGTAAACAGGTATTTTTTTAAATCAAGGAAAGGCTCATTTAAAACAGGCAAAGTTTTACAGAGAGGATACATTTAATAAAACTGCGAGGACATCAAAGTGGTAAATACTGTGAAATACCTTTTCTCACAAAAAGGCAAATATTGAAGTTGTTTATCAACTTCGCTAGAAAAAAAAAACACTTGGCATACAAAATATTTAAGTGAAGGAGAAGTCTAACGCTGAACTGACAATGAAGGGAAATTGTTTATGTGTTATGAACATCCAAGTCTTTCTTCTTTTTTAAGTTGTCAAAGAAGCTTCCACAAAATTAGAAAGGACAACAGTTCTGAGCTGTAATTTCGCCTTAAACTCTGGACACTCTATATGTAGTGCATTTTTAAACTTGAAATATATAATATTCAGCCAGCTTAAACCCATACAATGTATGTACAATACAATGTACAATTATGTCTCTTGAGCATCAATCTTGTTACTGCTGATTCTTGTAAATCTTTTTGCTTCTACTTTCATCTTAAACTAATACGTGCCAGATATAACTGTCTTGTTTCAGTGAGAGACGCCCTATTTCTATGTCATTTTTAATGTATCTATTTGTACAATTTTAAAGTTCTTATTTTAGTATACATATAAATATCAGTATTCTGACATGTAAGAAAATGTTACGGCATCACACTTATATTTTATGAACATTGTACTGTTGCTTTAATATGAGCTTCAATATAAGAAGCAATCTTTGAAATAAAAAAAGATTTTTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
b = "asis:ACCCGAGCGCGGT"
cmd.outfile = "test.txt"
cmd
