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

# Exercises 5.4.6

# Exercise 1
#Take in input into inputStr and count occurrence of each letter in the input.
inputStr = input("Please enter a word!")
print("The input string is: ", inputStr)
inputDict = {}
for letter in inputStr:
    inputDict[letter] = inputDict.get(letter, 0) + 1 

print("Letter occurrence:")
for (key, val) in inputDict.items():
    print("{} : {}".format(key, val))


def addFruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return None

# Exercise 2
# Make these tests work
newInventory = {}
addFruit(newInventory, "strawberries", 10)
print("strawberries" in newInventory)
print(newInventory["strawberries"] == 10)
addFruit(newInventory, "strawberries", 25)
print(newInventory["strawberries"] == 35)

# Exercise 3
import fileinput
#Read from a stream to construct word count dictionary.
for line in fileinput.input():
    line = line.rstrip()
    print(line)