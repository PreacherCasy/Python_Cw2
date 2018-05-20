from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse
from collections import defaultdict
import re

def blaster(file, dest):
    record = SeqIO.parse(file, format="fasta")
    output_dict = defaultdict()
    output_list = []
    for entry in record:
        print(entry)
        result_handle = NCBIWWW.qblast("blastn", "nt", entry.seq, url_base='https://blast.ncbi.nlm.nih.gov/Blast.cgi')
        blast_record = list(NCBIXML.read(result_handle).alignments)[0]
        if blast_record:
            new_name = str(blast_record.title)
            if True:
                new_name = re.sub('gi\|[A-Za-z0-9|.]{1,}\| ', '', new_name, flags=re.IGNORECASE)
                new_name = re.sub('(,? complete [A-Za-z0-9.,: ]{0,})|(,? chromosome [A-Za-z0-9.,: ]{0,}) | (,? genome [A-Za-z0-9.,: ]{0,}) | (,? mRNA [A-Za-z0-9.,: ]{0,})', '', new_name, flags=re.IGNORECASE)
                print(new_name)
            output_dict[new_name] = str(entry.seq)
    for key in output_dict.keys():
        try:
            output_list.append(SeqRecord(Seq(output_dict[key]), id=key))
        except:
            for val in output_dict[key]:
                output_list.append(SeqRecord(Seq(val), id=key))
    SeqIO.write(output_list, dest, "fasta")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Contig namer')
    parser.add_argument('-i', help='Specify name/path to your input fasta file', metavar='File',
                        type=str, required=True)
    parser.add_argument('-o', help='Specify name/path to your output file')

    args = parser.parse_args()

    i, o = args.i, args.o
    blaster(i, o)