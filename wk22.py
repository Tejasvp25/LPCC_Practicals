EMOT = {'STOP': {'class': "1", 'opcode': "00"}, 'ADD': {'class': "1", 'opcode': "01"}, 'SUB': {'class': "1", 'opcode': "02"}, 'MULT': {'class': "1", 'opcode': "03"}, 'MOVER': {'class': "1", 'opcode': "04"}, 'MOVEM': {'class': "1", 'opcode': "05"}, 'COMP': {'class': "1", 'opcode': "06"}, 'BC': {'class': "1", 'opcode': "07"}, 'DIV': {'class': "1", 'opcode': "08"}, 'READ': {'class': "1", 'opcode': "09"}, 'PRINT': {'class': "1", 'opcode': "10"}, 'START': {'class': "3", 'opcode': "01"}, 'END': {'class': "3", 'opcode': "02"},
        'ORIGIN': {'class': "3", 'opcode': "03"}, 'EQU': {'class': "3", 'opcode': "04"}, 'LTORG': {'class': "3", 'opcode': "05"}, 'DS': {'class': "2", 'opcode': "01"}, 'DC': {'class': "2", 'opcode': "02"}, 'AREG': {'class': "4", 'opcode': "01"}, 'BREG': {'class': "4", 'opcode': "02"}, 'CREG': {'class': "4", 'opcode': "03"}, 'EQ': {'class': "5", 'opcode': "01"}, 'LT': {'class': "5", 'opcode': "02"}, 'GT': {'class': "5", 'opcode': "03"}, 'NE': {'class': "5", 'opcode': "04"}, 'LE': {'class': "5", 'opcode': "05"}, 'GT': {'class': "5", 'opcode': "06"}, 'ANY': {'class': "5", 'opcode': "07"}}

symbolTable = []
lc = {}
lcVal = 0
literalTable = {}


def processInput(str):
    global lcVal
    str = str.replace(',', " ")
    output = str.split(' ')
    for op in output:
        op = op.replace('\n', '')
        if('=' in op and op not in literalTable):
            literalTable[op.split("'")[1]] = lcVal
    lcVal = lcVal+1


def assignLoc():
    global lc, lcVal
    for val in literalTable:
        literalTable[val] = lcVal
        lcVal += 1


fileName = input("Enter Input file name : ")
file = open(fileName)
lines = file.readlines()
if(len(lines[0].split(" ")) == 2):
    lcVal = int(lines[0].split(" ")[1])
else:
    lcVal = 100

for line in lines[1:-1]:
    processInput(line.upper())
assignLoc()

print("\nLiteral Table : ")
for key, val in literalTable.items():
    print(key, " : ", val)
