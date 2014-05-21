#!/usr/bin/python
import os
import sys
import subprocess
import Bio
from Bio.Emboss.Applications import WaterCommandline
cmd = WaterCommandline(gapopen=10, gapextend=0.5)
cmd.asequence = "asis:ACCCGGGCGCGGT"
cmd.bsequence = "asis:ACCCGAGCGCGGT"
cmd.outfile = "temp_water.txt"
#cline.outfile = sys.stdout
print cmd
subprocess.call(cmd)
#cmd
