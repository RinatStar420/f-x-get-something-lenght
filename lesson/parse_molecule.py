import re

"""parse_molecule("H2O") ==> {'H': 2, 'O' : 1},
parse_molecule("Mg(OH)2") ==> {'Mg': 1, 'O' : 2, 'H': 2},
parse_molecule("K4[ON(SO3)2]2") ==> {'K': 4,  'O': 14,  'N': 2,  'S': 4}"""


def parse_molecule(formula):
    pattern = r'[A-Z][a-z]?'
    pattern2 = r'\d+'
    map_dict = {'(': ')', '{': '}', '[': ']'}
    i = 0
    temp_dict = {}
    while i < len(formula):
        ss = re.match(pattern, formula[i:])
        if ss is not None:
            if ss.group(0).isalpha():
                i += len(ss.group(0))
                ss2 = re.match(pattern2, formula[i:])
                if ss2 is not None:
                    if ss2.group(0).isdigit():
                        i += len(ss2.group(0))
                        temp_dict[ss.group(0)] = int(ss2.group(0)) + temp_dict.get(ss.group(0), 0)
                    else:
                        temp_dict[ss.group(0)] = 1 + temp_dict.get(ss.group(0), 0)
                else:
                    temp_dict[ss.group(0)] = 1 + temp_dict.get(ss.group(0), 0)
        elif formula[i] in map_dict:
            index = formula[i:].index(map_dict[formula[i]])
            temp_dict2 = parse_molecule(formula[i + 1:i + index])
            i += index + 1
            ss2 = re.match(pattern2, formula[i:])
            if ss2 is not None:
                if ss2.group(0).isdigit():
                    i += len(ss2.group(0))
                    for item in temp_dict2:
                        temp_dict2[item] *= int(ss2.group(0))
            for item in temp_dict2:
                temp_dict[item] = temp_dict2[item] + temp_dict.get(item, 0)
    return temp_dict


print(parse_molecule('(C5H5)Fe(CO)2CH3'))




from collections import Counter

def expand_str(m):
    return m.group(1) * int(m.group(2))

def parse_molecule (formula):
    formula = re.sub(r'\(([^\)]+)\)(\d+)',expand_str,formula)
    formula = re.sub(r'\[([^\]]+)\](\d+)',expand_str,formula)
    formula = re.sub(r'\{([^\}]+)\}(\d+)',expand_str,formula)
    formula = re.sub(r'([A-Z][a-z]?)(\d+)',expand_str,formula)
    m = re.findall(r'[A-Z][a-z]?',formula)
    return Counter(m)