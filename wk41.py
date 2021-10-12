EMOT = {'STOP': {'class': "1", 'opcode': "00"}, 'ADD': {'class': "1", 'opcode': "01"}, 'SUB': {'class': "1", 'opcode': "02"}, 'MULT': {'class': "1", 'opcode': "03"}, 'MOVER': {'class': "1", 'opcode': "04"}, 'MOVEM': {'class': "1", 'opcode': "05"}, 'COMP': {'class': "1", 'opcode': "06"}, 'BC': {'class': "1", 'opcode': "07"}, 'DIV': {'class': "1", 'opcode': "08"}, 'READ': {'class': "1", 'opcode': "09"}, 'PRINT': {'class': "1", 'opcode': "10"}, 'START': {'class': "3", 'opcode': "01"}, 'END': {'class': "3", 'opcode': "02"},
        'ORIGIN': {'class': "3", 'opcode': "03"}, 'EQU': {'class': "3", 'opcode': "04"}, 'LTORG': {'class': "3", 'opcode': "05"}, 'DS': {'class': "2", 'opcode': "01"}, 'DC': {'class': "2", 'opcode': "02"}, 'AREG': {'class': "4", 'opcode': "01"}, 'BREG': {'class': "4", 'opcode': "02"}, 'CREG': {'class': "4", 'opcode': "03"}, 'EQ': {'class': "5", 'opcode': "01"}, 'LT': {'class': "5", 'opcode': "02"}, 'GT': {'class': "5", 'opcode': "03"}, 'NE': {'class': "5", 'opcode': "04"}, 'LE': {'class': "5", 'opcode': "05"}, 'GT': {'class': "5", 'opcode': "06"}, 'ANY': {'class': "5", 'opcode': "07"}}
STATEMENTS = {
    '1': 'IS',
    '2': 'DL',
    '3': 'AD',
    '4': 'RG',
    '5': 'CC'
}

symbolTable = []
lc = {}
lcVal = 0
literalTable = []
literalList = []
poolTable = []
ilt = 0
ipt = 0
idx = 0
poolTable.append(0)


def processInput(str):
    global lcVal, ilt, idx
    str = str.replace(',', " ")
    if('ORIGIN' in str):
        temp = str.split(' ')[1].split('+')[0]
        lcVal = int(symbolTable[findInSymbolTable(temp)][temp]
                    ) + int(str.split('+')[1])
        return
    if('LTORG' in str):
        assignLoc()
        idx += 1
        return
    output = str.replace('\n', '').split(' ')
    if(findInSymbolTable(output[0]) == -1 and output[0] not in EMOT):
        symbolTable.append({output[0]: lcVal})
    if(len(output) == 2 and findInSymbolTable(output[1]) != -1):
        lc[output[1]] = lcVal
    if(len(output) == 3 and '=' in output[2]):
        literalTable.append({int(output[2].split("'")[1]): ""})
        literalList.append(int(output[2].split("'")[1]))
        ilt += 1
    if(len(output) == 3 and '=' not in output[2] and output[2] not in EMOT and findInSymbolTable(output[2]) == -1):
        symbolTable.append({output[2]: lcVal})
    if(len(output) == 4 and '=' in output[3]):
        literalTable.append({int(output[3].split("'")[1]): ""})
        literalList.append(int(output[3].split("'")[1]))
        ilt += 1
    if(len(output) == 4 and '=' not in output[3] and output[3] not in EMOT and findInSymbolTable(output[3]) == -1):
        symbolTable.append({output[3]: lcVal})
    lcVal = lcVal+1


def findInSymbolTable(query):
    global symbolTable
    for it in range(len(symbolTable)):
        if(query in symbolTable[it].keys()):
            return it
    return -1


def findInLiteralTable(query, kek=False):
    global literalTable
    for it in range(len(literalTable)):
        # if kek:
        #     print(literalTable[it], query, query in literalTable[it].keys(
        #     ), query in literalTable[it])
        if(str(query) in literalTable[it].keys()):
            return it
    return -1


def assignLoc():
    global lc, lcVal, ipt
    for i in range(ipt, ilt):
        di = dict(literalTable[i])
        for key, _ in di.items():
            di[key] = lcVal
            literalTable[i] = di
        lcVal += 1
        ipt += 1
    poolTable.append(ipt)


def generateIC(str):
    global output_file
    str = str.replace('\n', '')
    ic = f"{str} -> "
    str = str.replace(',', " ").split(' ')
    if(len(str) == 3):
        if(str[0] in EMOT):
            ic += f"({STATEMENTS[EMOT[str[0]]['class']]},{EMOT[str[0]]['opcode']})"
        if(str[1] in EMOT):
            ic += f"({STATEMENTS[EMOT[str[1]]['class']]},{EMOT[str[1]]['opcode']})"
        if(findInSymbolTable(str[2]) != -1):
            ic += f"(S,{findInSymbolTable(str[2])})"
        if("=" in str[2] and int(str[2].split("'")[1]) in literalList):
            ic += "(L" + \
                literalList.index(int(str[2].split("'")[1])).__str__() + ")"
    if(len(str) == 4):
        if(str[1] in EMOT):
            ic += f"({STATEMENTS[EMOT[str[1]]['class']]},{EMOT[str[1]]['opcode']})"
        if(str[2] in EMOT):
            ic += f"({STATEMENTS[EMOT[str[2]]['class']]},{EMOT[str[2]]['opcode']})"
        if(findInSymbolTable(str[3]) != -1):
            ic += f"(S,{findInSymbolTable(str[3])})"
        if("=" in str[3] and int(str[3].split("'")[1]) in literalList):
            ic += "(L" + \
                literalList.index(int(str[3].split("'")[1])).__str__() + ")"
    if("ORIGIN" in str):
        ic += f"({STATEMENTS[EMOT[str[0]]['class']]},{EMOT[str[0]]['opcode']})"
        plusSplit = str[1].split('+')
        newAddress = int(symbolTable[findInSymbolTable(
            plusSplit[0])][plusSplit[0]]) + + int(plusSplit[1])
        ic += f"(C,{newAddress.__str__()})"
    if("LTORG" in str):
        ic += f"({STATEMENTS[EMOT[str[0]]['class']]},{EMOT[str[0]]['opcode']})"
    if("STOP" in str or "END" in str):
        ic += f"({STATEMENTS[EMOT[str[0]]['class']]},{EMOT[str[0]]['opcode']})"
    output_file.write(ic+"\n")
    # print(ic)


# fileName = input()
fileName = "s4.txt"
file = open(fileName)
output_file = open("output.txt", "w")
lines = file.readlines()
if(len(lines[0].split(" ")) == 2):
    lines[0] = lines[0].replace("\n", "")
    splited = lines[0].split(" ")
    lcVal = int(lines[0].split(" ")[1])
    output_file.write(
        f"{lines[0]} -> ({STATEMENTS[EMOT[splited[0]]['class']]},{EMOT[splited[0]]['opcode']})(C,{splited[1]})\n")
    # print(f"{lines[0]} -> ({STATEMENTS[EMOT[splited[0]]['class']]},{EMOT[splited[0]]['opcode']})(C,{splited[1]})\n")
else:
    output_file.write(
        f"{lines[0]} -> (AD,01)(C,100)")
    lcVal = 100
    line = lines[0].replace("\n", "")
    # print(f"{line} -> (AD,01)(C,100)")

for line in lines[1:-1]:
    processInput(line.upper())
# assignLoc()

for line in lines[1:-1]:
    generateIC(line.upper())

print("\nLiteral Table : ")
for val in literalTable:
    print(val)

print("\n Pool Table : ")
print(poolTable[0:idx])

print("\n Symbol Table : ")
print(symbolTable)
