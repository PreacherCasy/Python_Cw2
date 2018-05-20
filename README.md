# Python_Cw2
## Description
Thi is a short CL-executable code for annotation of nameless assembly outputs. It performs BLAST search over NCBI Nucleotide database and sets best search result name for a quiery sequence.

## Code structure
As usual, this code comprises of two logical parts: the first part defines code functioning and the second embodies CL interface vi *argparse* module
Basically, the first part consist of one function named *blaster*. This function takes a *.fasta* file and performs BLAST search for each entry found there. If resulting search list is not empty, it takes the first entry's title and processes it so that only taxon name remains and allocates it as an id for a new SeqRecord object with sequence inherited a query entry. If there are more than one contig sharing the same name, *blaster* will write them one after another.
An *argparse* defines two flags for CL launching:
-**-i**: an input *.fasta* file flag;
-**-o**: an output *.fasta* file flag.

## Example
Launch a code against a suggested classwork dataset:
```
python Cw2_Malovichko.py -i classwork2.fasta -o Cw2_output.fasta
```
The resulting file can be found in this repository. As we can see, most of the queries turned out to belong to viral, bacterial or fungal genomes which is consistent with declared property of the dataset (human blood metagenome). At the same time, the last contig seems to be dubious because of its perfect alignment on duckbill's genome assembly; however, this one might be either missequence or data provider's sick joke.

## Acknowledgements
Eugene Bakin of Bioinformatics Institue for his Python crash course.
