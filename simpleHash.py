import string

########################################################
#
# A simple hash so the admin password doesn't have to be stored in plain text
#
########################################################

def initDict():
    chars = list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    start = 11
    vals = list(range(start, len(chars)+start))
    hashDict = {}
    for i in range(len(chars)):
        hashDict[chars[i]] = vals[i]
    return hashDict

def passHash(str):
    hashDict = initDict()
    index = 1
    sum = 0
    for char in list(str):
        sum+= hashDict.get(char)*17*index
        index+=1
    return sum
