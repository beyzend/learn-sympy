def f(n):
    if n % 2 == 0:
        return n // 2
    return 3*n + 1  


def computeSequenceToOne(a_0):
    a_i = a_0
    k = 0
    sequence=list([a_i])
    while a_i != 1:
        #print("a_{}:={}, ".format(k, a_i))
        a_i = f(a_i)
        sequence.append(a_i)
        k+=1
    #print("a_{}:={}\n".format(k, a_i))
    #print("{} numbers in sequence.\n".format(k))
    return sequence

#compute a_i = f(a_{i-1}) for 0 <= i < k
#for i in range(k):
#    sequence.append(f(sequence[i]))
n = 100
indexLimit = 100
sequences=list()
for i in range(1, n+1):
    sequences.append(computeSequenceToOne(i))
    print("a_0:= {}".format(i))
    if (len(sequences[-1]) >= indexLimit):
        print("sequence contain more than {} member".format(indexLimit))
        print(sequences[-1])
    else:
        print(sequences[-1])



