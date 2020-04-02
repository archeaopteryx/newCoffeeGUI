#TODO : automated backup
#TODO: window closes: write file

import csv

skipRows = 2
userDict={}

#a 'with' statement basically incloses  a 'try... finally' block that closes the
#file in the 'finally' statement. Therefore there's no need for an explicit close

def openList():
    skipRows = 2
    userDict = {}
    milkDict ={}
    with open('memberList.csv', newline='') as f:
        fileReader = csv.reader(f, delimiter=",")
        for i in range(skipRows):
            fileReader.__next__()
        for row in fileReader:
            if len(row) == 2:
                userDict[row[0]] = int(row[1])
                milkDict[row[0]] = 0
            elif len(row) == 3:
                userDict[row[0]] = int(row[1])
                milkDict[row[0]] = int(row[2])
    return (userDict, milkDict)

def backup():
    print("todo")

def export(memberDict, milkDict):
    print("todo")
