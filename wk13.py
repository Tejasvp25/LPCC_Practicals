EMOT = ['STOP', 'ADD', 'SUB', 'MULT', 'MOVER', 'MOVEM', 'COMP', 'BC', 'DIV', 'READ', 'PRINT', 'START', 'END',
        'ORIGIN', 'EQU', 'LTORG', 'DS', 'DC', 'AREG', 'BREG', 'CREG', 'EQ', 'LT', 'GT', 'NE', 'LE', 'GT', 'ANY']

symbolTable = []


def processInput(str):

    str = str.replace(',', " ")
    output = str.split(' ')
    for op in output:
        op = op.replace('\n', '')
        if(op not in symbolTable and op not in EMOT and "'" not in op):
            symbolTable.append(op)


fileName = input("Enter Input file name : ")
file = open(fileName)
lines = file.readlines()
for line in lines[1:]:
    processInput(line.upper())

print("Symbol Table : ")
for sym in symbolTable:
    print(sym)
