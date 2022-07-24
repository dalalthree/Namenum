"""
ID: ryanada1
LANG: PYTHON3
TASK: namenum
"""


def getPossibleLetters(d):
    d -= 2
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return letters[d * 3: d * 3 + 3]

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')

din = open('dict.txt', 'r')

allowedNames = din.read().split()
number = fin.read().split()
digits = []
for i in range(len(number[0])):
    digits.append(int(number[0][i]))
names = []

wordlist = []
def makeWords(word, digits):
    global wordlist
    if len(digits) == 1:
        for i in range(3):
            wordlist.append(word + getPossibleLetters(digits[0])[i])
    else:
        for i in range(3):
            makeWords(word + getPossibleLetters(digits[0])[i], digits[1:])


makeWords('', digits)

allowed = []

for i in wordlist:
    for j in allowedNames:
        if i == j:
            allowed.append(i)
            break

output = ""
for i in range(len(allowed)):
    output += allowed[i]
    if i < len(allowed) - 1:
        output += " "
if output == "":
    output = "NONE"
fout.write(output + '\n')

fout.close()