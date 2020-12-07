fp = open('blakepoems.txt', 'r')
fp1 = fp.readlines()
fp2 = []
for line in fp1:
    fp2.append(line.lower().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))
print(fp2)