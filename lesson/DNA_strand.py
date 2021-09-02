"""
est.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
        test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
        test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
"""


def DNA_strand(dna):
    """Эта функция меняет последовотельность ДНК"""
    result = []
    for i in dna:
        if i == 'A': result.append('T')
        if i == 'T': result.append('A')
        if i == 'G': result.append('C')
        if i == 'C': result.append('G')

    return "".join(result)


"""Альтернативный метод"""

MAPPING = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna):

    rna = []
    for item in dna:
        rna.append(MAPPING[item])

    return ''.join(rna)
