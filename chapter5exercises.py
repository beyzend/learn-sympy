def Reverse(str):
    retStr = ""
    for i in range(-1, -len(str) - 1 , -1):
        retStr = retStr + str[i]
    return retStr
numOfCols=12
labels = ["{{{}:>5}}".format(i) for i in range(numOfCols)]
print("labels: {}".format(labels))
labels = "".join(labels)
print("{0:<2}".format("-"*2) + labels)
indices = list(range(1, numOfCols + 1))

#Print field labels
print("{0:<2}".format(" ") + labels.format(*indices))

labels = ["{0:<2}"] + ["{{{}:>5}}".format(i) for i in range(1, numOfCols + 1)]  
labels = "".join(labels)
print("".join(["-"*5]*(numOfCols + 1)))

for i in indices:
    vals = [i] + [i*j for j in indices]
    print(labels.format(*vals))

strs = "happy@Python@ @a"
strsReverse = "yppah@nohtyP@ @a"
for (str, strR) in zip(strs.split('@'), strsReverse.split('@')):
    print(Reverse(str) == strR)


