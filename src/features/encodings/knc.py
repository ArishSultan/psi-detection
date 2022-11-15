from typing import Generator
from itertools import product


def encode_knc(sequence: str, k: int, nucleotides: str = 'ATGC'):
    return encode_knc_with_kmers(sequence, generate_kmers(k, nucleotides))


def encode_knc_with_kmers(sequence: str, kmers: Generator[str]):
    nucleotide_count = len(sequence)
    for kmer in kmers:
        yield sequence.count(kmer) / nucleotide_count


def generate_kmers(k: int, nucleotides: str):
    for pair in product(*(['AUCG'] * k)):
        yield ''.join(pair)
