EMOT = {'STOP': {'class': "1", 'opcode': "00"}, 'ADD': {'class': "1", 'opcode': "01"}, 'SUB': {'class': "1", 'opcode': "02"}, 'MULT': {'class': "1", 'opcode': "03"}, 'MOVER': {'class': "1", 'opcode': "04"}, 'MOVEM': {'class': "1", 'opcode': "05"}, 'COMP': {'class': "1", 'opcode': "06"}, 'BC': {'class': "1", 'opcode': "07"}, 'DIV': {'class': "1", 'opcode': "08"}, 'READ': {'class': "1", 'opcode': "09"}, 'PRINT': {'class': "1", 'opcode': "10"}, 'START': {'class': "3", 'opcode': "01"}, 'END': {'class': "3", 'opcode': "02"},
        'ORIGIN': {'class': "3", 'opcode': "03"}, 'EQU': {'class': "3", 'opcode': "04"}, 'LTORG': {'class': "3", 'opcode': "05"}, 'DS': {'class': "2", 'opcode': "01"}, 'DC': {'class': "2", 'opcode': "02"}, 'AREG': {'class': "4", 'opcode': "01"}, 'BREG': {'class': "4", 'opcode': "02"}, 'CREG': {'class': "4", 'opcode': "03"}, 'EQ': {'class': "5", 'opcode': "01"}, 'LT': {'class': "5", 'opcode': "02"}, 'GT': {'class': "5", 'opcode': "03"}, 'NE': {'class': "5", 'opcode': "04"}, 'LE': {'class': "5", 'opcode': "05"}, 'GT': {'class': "5", 'opcode': "06"}, 'ANY': {'class': "5", 'opcode': "07"}}

symbolTable = {}
lc = {}
lcVal = 0
literalTable = []
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
        lcVal = int(symbolTable[temp]) + int(str.split('+')[1])
        return
    if('LTORG' in str):
        assignLoc()
        idx += 1
        return
    output = str.replace('\n', '').split(' ')
    if(output[0] not in symbolTable and output[0] not in EMOT):
        symbolTable[output[0]] = lcVal
    if(len(output) == 2 and output[1] in symbolTable):
        lc[output[1]] = lcVal
    if(len(output) == 3 and '=' in output[2]):
        literalTable.append({output[2].split("'")[1]: ""})
        ilt += 1
    if(len(output) == 4 and '=' in output[3]):
        literalTable.append({output[3].split("'")[1]: ""})
        ilt += 1
    lcVal = lcVal+1


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


fileName = input()
file = open(fileName)
lines = file.readlines()
if(len(lines[0].split(" ")) == 2):
    lcVal = int(lines[0].split(" ")[1])
else:
    lcVal = 100

for line in lines[1:-1]:
    processInput(line.upper())
# assignLoc()

print("\nLiteral Table : ")
for val in literalTable:
    print(val)

print("\n Pool Table : ")
print(poolTable[0:idx])

print("\n Symbol Table : ")
print(symbolTable)
