def processInput(str):
    str = str.replace(',', " ")
    output = str.split(' ')
    print("Count : ", len(output))
    print("Output : ", " ".join(output), "\n")


fileName = input("Enter Input file name : ")
file = open(fileName)
for line in file.readlines():
    processInput(line)
