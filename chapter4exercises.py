import turtle

numOfCols = 12

numbers = list(range(1, 13))
fields = "{:>7} "*numOfCols
header = fields.format(*range(1, numOfCols + 1))
print(header)
b = list(["-"*7]*numOfCols)
print(fields.format(*b))
for val in numbers:
    rowVal = [val * j for j in numbers]
    print(fields.format(*rowVal))
    

