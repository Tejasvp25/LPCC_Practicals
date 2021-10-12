EMOT = ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT', 'START', 'END',
        'ORIGIN', 'EQU', 'LTORG', 'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GT', 'NE', 'LE', 'GT', 'ANY']

symbolTable = []
lc = {}
lcVal = 0


def processInput(str):
    global lcVal
    str = str.replace(',', " ")
    output = str.split(' ')
    for i, op in enumerate(output):
        op = op.replace('\n', '')
        if(op in symbolTable and i != 2):
            lc[op] = lcVal
            continue
        if(op not in symbolTable and op not in EMOT and "'" not in op):
            symbolTable.append(op)
            lc[op] = lcVal
    lcVal = lcVal+1


fileName = input("Enter Input file name : ")
file = open(fileName)
lines = file.readlines()
if(len(lines[0].split(" ")) == 2):
    lcVal = int(lines[0].split(" ")[1])
else:
    lcVal = 100

for line in lines[1:]:
    processInput(line.upper())

print("Symbol Table : ")
for sym in symbolTable:
    print(sym)

print("\nLocation : ")

for key, val in lc.items():
    print(key, " : ", val)
