def encode_ncp(sequence: str):
    result = []
    for nucleotide in sequence:
        match nucleotide:
            case 'A':
                result += [1, 1, 1]
            case 'T':
                result += [0, 0, 1]
            case 'U':
                result += [0, 0, 1]
            case 'G':
                result += [1, 0, 0]
            case 'C':
                result += [0, 1, 0]

    return result
