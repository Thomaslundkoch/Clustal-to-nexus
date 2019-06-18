# Clustal to nexus

To do phylogenetic analyses in PAUP* you need to convert your MSA-file to nexus format. I often align using ClustalW, which results in a .aln file. This small python program converts the .aln file to a .nexus file that can be read by PAUP*.

## How to use

```
.\convert.py <file.aln> <data type = 'Protein' or 'DNA'>
```
