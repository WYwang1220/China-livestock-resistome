from Bio import SeqIO
import sys

def count_snps(fasta_file):
    records = list(SeqIO.parse(fasta_file, "fasta"))
    if not records:
        print("No sequences found in the FASTA file.")
        return 0

    # Get the length of the first sequence
    seq_length = len(records[0].seq)
    snp_count = 0

    # Compare each position across all sequences
    for i in range(seq_length):
        bases = {record.seq[i] for record in records}
        if len(bases) > 1:
            snp_count += 1

    return snp_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_snps.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    snp_count = count_snps(fasta_file)
    print(f"Number of SNPs: {snp_count}")
