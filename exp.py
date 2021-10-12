import re

emot = {1: {'STOP': 0, 'ADD': 1, 'SUB': 2, 'MULT': 3, 'MOVER': 4, 'MOVEM': 5, 'COMP': 6,
            'BC': 7, 'DIV': 8, 'READ': 9, 'PRINT': 10},
        2: {'DS': 1, 'DC': 2},
        3: {'START': 1, 'END': 2, 'ORIGIN': 3, 'EQU': 4, 'LTORG': 5},
        4: {'AREG': 1, 'BREG': 2, 'CREG': 3},
        5: {'EQ': 1, 'LT': 2, 'GT': 3, 'NE': 4, 'LE': 5, 'GE': 6, 'ANY': 7}}

_class = {
    1: "IS",
    2: "DL",
    3: "AD",
    4: "RG",
    5: "CC"
}

label_pattern = "[a-zA-Z]+[a-zA-Z0-9]*"
operation_pattern = "[a-zA-Z]+"
symbol_table = {}
list_symbols = []
literal_table = {}
list_literals = []
literal_index = 0
pool_table = []
output_file = open("output.txt", "a")


def generate_ic(tokens):
    len_emot = len(emot)

    for token in tokens:
        for class_number in range(1, len_emot + 1):
            if token is None:
                break
            elif token in emot[class_number]:
                output_file.write(
                    f"({_class[class_number]},{emot[class_number][token]})")
        if token is not None:
            if ord(token[0]) in range(ord('0'), ord('9')):
                if int(token) in list_literals:
                    output_file.write(f"(L,{list_literals.index(int(token))})")
            elif token in symbol_table:
                output_file.write(f"(S,{list_symbols.index(token)})")

    output_file.write("\n")


def generate_tokens(instruction):
    symbol_and_keyword = "([a-zA-Z]+[0-9]*)\\s+([a-zA-Z]+)"
    symbol = "[a-zA-Z]+[0-9]*"
    keyword = "[a-zA-Z]+"
    number = "[0-9]+"

    assembly_pattern1 = re.compile(
        f"\\s*{symbol_and_keyword}\\s+({keyword})\\W\\s*\\W*({symbol}|{number})\\W*")
    assembly_pattern2 = re.compile(
        f"\\s*({keyword})\\s+({symbol}|{keyword})\\W\\s*\\W*({symbol}|{number})\\W*")
    assembly_pattern3 = re.compile(f"\\s*({keyword}|{number})\\s*({keyword})?")

    four_string_pattern = assembly_pattern1.match(
        instruction)  # matches   " L1      MOVEM BREG, ='2'"
    three_string_pattern = assembly_pattern2.match(
        instruction)  # matches     "MOVEM AREG, X"
    two_string_pattern = assembly_pattern3.match(instruction)

    if four_string_pattern:
        return four_string_pattern.groups()
    elif three_string_pattern:
        return three_string_pattern.groups()
    elif two_string_pattern:
        return two_string_pattern.groups()


def symbol_pattern_match(instruction):
    line_pattern = f"({label_pattern})\\s+({operation_pattern})\\s+(.*$)"
    label_match = re.match(line_pattern, line)
    return label_match


def literal_pattern_match(instruction):
    literal_pattern = f"(.*)(='([0-9])')"
    match = re.match(literal_pattern, instruction)
    string_literal = 0
    if match:
        string_literal = match.group(3)
    return match, int(string_literal)


def evaluate_ltorg(location_count, list_literal, lit_index):
    pool_table.append(lit_index)
    for i in range(lit_index, len(list_literals)):
        literal_table[lit_index] = {location_count, list_literal[i]}
        lit_index += 1
        location_count += 1
    return lit_index, location_count


def evaluate_origin(instruction):
    origin_pattern = "\\s*(ORIGIN)\\s([a-zA-Z]+[0-9]*).([0-9])"
    match = re.match(origin_pattern, instruction)
    label = match.group(2)
    number = int(match.group(3))
    _lc = symbol_table[label][0] + number
    return _lc


def generate_symbol_table(instruction, lc):
    label = instruction.split()[0]
    for _class in range(1, len(emot) + 1):
        if label in emot[_class]:
            raise ValueError("Keyword can not be label")
    else:
        symbol_table[label] = [lc]
        list_symbols.append(label)


file = open("s4.txt")
location_counter = file.readline().split()
lc = int(location_counter[1])

for line in file:
    if symbol_pattern_match(line):
        generate_symbol_table(line, lc)
    pattern_match, literal_value = literal_pattern_match(line)
    if pattern_match:
        list_literals.append(literal_value)
    elif re.match('.*LTORG', line):
        literal_index, lc = evaluate_ltorg(lc, list_literals, literal_index)
        continue
    elif re.match('.*ORIGIN', line):
        lc = evaluate_origin(line)
    lc += 1
    tokens = generate_tokens(line)
    generate_ic(tokens)

file.close()
output_file.close()
print("symbol_table")
for symbol in symbol_table:
    print(f"{symbol}-->{symbol_table[symbol]}")

print()
print("literal_table")
for literal in literal_table:
    print(f"{literal}-->{literal_table[literal]}")
print()
print("pool_table")
print(pool_table)
