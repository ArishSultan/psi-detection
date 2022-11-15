def encode_nd(sequence: str):
    result = []

    for i in range(len(sequence)):
        result.append(sequence[:i].count(sequence[i]) / (i + 1))

    return result


def nd(seq):
    seq_length = len(seq)
    nd_list = [None] * seq_length
    for j in range(seq_length):
        if seq[j] == 'A':
            nd_list[j] = round(seq[0:j].count('A') / (j + 1), 3)
        elif seq[j] == 'U':
            nd_list[j] = round(seq[0:j].count('U') / (j + 1), 3)
        elif seq[j] == 'C':
            nd_list[j] = round(seq[0:j].count('C') / (j + 1), 3)
        elif seq[j] == 'G':
            nd_list[j] = round(seq[0:j].count('G') / (j + 1), 3)
    return nd_list

print(nd('UCAAGUGUAGUAUCUGUUCUU'))
print(encode_nd('UCAAGUGUAGUAUCUGUUCUU'))
