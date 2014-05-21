#!/usr/bin/python
import os
import sys
import subprocess
import Bio
from Bio.Emboss.Applications import WaterCommandline
cmd = WaterCommandline(gapopen=10, gapextend=0.5)
cmd.asequence = "asis:ACCCGGGCGCGGT"
a = "asis:ACCCGGGCGCGGT"
cmd.bsequence = "asis:ACCCGAGCGCGGT"
b = "asis:ACCCGAGCGCGGT"

cmd.outfile = "temp_water.txt"
#cline.outfile = sys.stdout
#print cmd
#subprocess.call(["water", "-temp_water.txt", "-asequence="+a, "-bsequence"+b, "-gapopen=10", "-gapextend=0.5"])
cmd
