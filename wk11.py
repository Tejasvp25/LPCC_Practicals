input_alp = input("Enter Input file name : ")
input_alp = input_alp.replace(',', " ")
output = input_alp.split(' ')
print("\nCount : ", len(output))
print("Output : ", "".join(output))
