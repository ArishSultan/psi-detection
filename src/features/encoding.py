import numpy as np


def ncp(sequence):
    ncps = []
    for n in sequence:
        ncps.extend(ncp_one(n))

    return np.array(ncps)


def ncp_one(nucleotide):
    return [
        1 if nucleotide == 'A' or nucleotide == 'G' else 0,
        1 if nucleotide == 'A' or nucleotide == 'C' else 0,
        1 if nucleotide == 'A' or nucleotide == 'U' else 0,
    ]


def nd(sequence):
    nds = []
    count = {'A': 0, 'C': 0, 'U': 0, 'G': 0}
    for index, n in enumerate(sequence):
        new_val = count[n] + 1
        count[n] = new_val

        nds.append(new_val / (index + 1))

    return nds


def pse_knc(sequence):
    ncps = []
    nds = nd(sequence)
    for index, n in enumerate(sequence):
        ncps.extend(ncp_one(n))
        ncps.append(nds[index])

    return ncps


__all__ = ['pse_knc', 'nd', 'ncp']
