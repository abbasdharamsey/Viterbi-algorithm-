import math
import matplotlib.pyplot as plt

pi = []
with open("initialStateDistribution.txt", 'r') as f:
    for line in f:
        pi.append(float(line))

a = []
with open("hw5_transitionMatrix.txt", 'r') as f:
    for line in f:
        eachList = [float(i) for i in line.split()]
        a.append(eachList)


b = []
with open("hw5_emissionMatrix.txt", 'r') as f:
    for line in f:
        eachList = [float(i) for i in line.split()]
        b.append(eachList)
# print b

T = []
with open("hw5_observations.txt", 'r') as f:
    for line in f:
        T = line.split()



Matrix = [[0 for x in range(len(T))] for x in range(26)]
for i in range(26):
    cur = math.log(pi[i]) + math.log(b[i][0])
    Matrix[i][0] = cur
    # if cur > maxL:
    #     maxL = cur
# for i in range(26):
#     print Matrix[i][0]

# print math.log(b[int(T[0])][t+1])
# print len(T)

for t in range(len(T)-1):
    for j in range(26): #columns of a, rows of l* rows of b
        maxI = -10000000000
        maxi = 0
        for i in range(26): # rows of a
            cur = math.log(a[i][j]) + Matrix[i][t]
            if cur > maxI:
                maxI = cur
                maxi = i
        Matrix[j][t+1] = maxI + math.log(b[j][int(T[t+1])])
# for i in range(26):
#     print Matrix[i][len(T)-1] 


sMatrix = []
stPlusOne = 0
for t in reversed(range(len(T))):
    St = float(-10000000000000000000000000)
    Si = 0
    for i in range(26):
        if t != (len(T)-1 or len(T)):
            cur = Matrix[i][t] + math.log(a[i][stPlusOne])
            if cur > St:
                Si = i
                St = cur

        else:
            if float(Matrix[i][t]) > St:
                Si = i
                St = Matrix[i][t]
    sMatrix.append(Si)
    stPlusOne = Si

# print sMatrix
sActualMatrix = sMatrix[::-1]

list_of_45000 = []
for i in range(1, 45001):
    list_of_45000.append(i)

letters = 'abcdefghijklmnopqrstuvwxyz'
word = []

for i in range(len(sMatrix)):
    if i == 0:
        word.append(letters[sMatrix[i]])
    else:
        if letters[sMatrix[i]] != letters[sMatrix[i-1]]:
            word.append(letters[sMatrix[i]])

# print word



            



