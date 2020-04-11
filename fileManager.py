import csv
from time import strftime, localtime
from pathlib import Path

#a 'with' statement basically incloses  a 'try... finally' block that closes the
#file in the 'finally' statement. Therefore there's no need for an explicit close

#If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use \r\n linendings on write an extra \r will be added. It should always be safe to specify newline='', since the csv module does its own (universal) newline handling.

#writerow() expects a tuple or list of strings. If it only receives a string, it will interprete that string as a list of strings and print each character separated by a comma

readInName = 'memberList.csv'
backUpName = 'memberListBackup.csv'

def openList():
    skipRows = 2
    userDict = {}
    milkDict ={}
    with open(readInName, newline='') as f:
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

def writeToFile(file, memberDict, milkDict):
    date = strftime("%a, %d %b %Y", localtime())
    time = strftime("%H:%M:%S", localtime())
    dateHeader = (date, time)
    colHeader = ("name", "balance", "withMilk")
    nameList = sorted(memberDict.keys())
    with open(file, 'w', newline='') as f:
        fwriter = csv.writer(f, delimiter=",")
        fwriter.writerow(dateHeader)
        fwriter.writerow(colHeader)
        for name in nameList:
            balance = memberDict[name]
            milk = milkDict[name]
            values = (name, balance, milk)
            fwriter.writerow(values)
    return

def backup(memberDict, milkDict):
    writeToFile(backUpName, memberDict, milkDict)
    return

def export(memberDict, milkDict):

    backupFile = Path(backUpName)
    readInFile = Path(readInName)

    if not backupFile.is_file() and readInFile.is_file():
        readInFile.rename(backUpNamep)
        writeToFile(readInName, memberDict, milkDict)
    else:
        writeToFile(readInName, memberDict, milkDict)
    return
