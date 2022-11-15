def encode_nd(sequence: str):
    """
    Encodes nucleotide sequence to ND (nucleotide density).

    :param sequence:
    :return:
    """
    result = []

    for i in range(len(sequence)):
        result.append(sequence[:i].count(sequence[i]) / i + 1)

    return result
