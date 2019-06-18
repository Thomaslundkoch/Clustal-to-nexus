#!/usr/bin/env python3
__author__="Thomas Lund Koch"

import os
import sys
import re

argv=sys.argv[1:]

if ".aln" in argv[0]:
    file_name=argv[0][:-4]

if argv[1] in ['DNA','Protein']:
    data_type = argv[1]

nexus_file = f"{file_name}.nexus"
if not os.path.exists(nexus_file):
    os.mknod(nexus_file)

with open(argv[0],'r') as in_f:
    sequences = {}
    for line in in_f:
        if line.startswith("CLUSTA"):
            continue
        elif re.match(r"[a-zA-Z0-9]",line):
            mes=line.split()
        else:
            continue

        if mes[0] not in sequences:
            sequences.update({mes[0]:mes[1]})
        else:
            sequences.update({mes[0]:sequences.get(mes[0])+mes[1]})

ntax=len(sequences)
nchar=len(list(sequences.values())[0])


with open(nexus_file,'w') as out_f:
    out_f.write("#NEXUS\nbegin data;\n")
    out_f.write(f"\tdimensions ntax={ntax} nchar={nchar};\n")
    out_f.write(f"\tformat datatype={data_type} missing=? gap=- interleave;\n")
    out_f.write("matrix\n")
    for key,item in sequences.items():
        out_f.write(f"{key} \t {item}\n")
    out_f.write(";\n")
    out_f.write("end;")


