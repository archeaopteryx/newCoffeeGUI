import csv
import sys
from time import strftime, localtime
from pathlib import Path
from simpleHash import passHash

#a 'with' statement basically incloses  a 'try... finally' block that closes the
#file in the 'finally' statement. Therefore there's no need for an explicit close

#If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use \r\n linendings on write an extra \r will be added. It should always be safe to specify newline='', since the csv module does its own (universal) newline handling.

#writerow() expects a tuple or list of strings. If it only receives a string, it will interpret that string as a list of strings and print each character separated by a comma

readInName = 'memberList.csv'
backUpName = 'memberListBackup.csv'

defaultCoffee = 20
defaultMilk = 5
defaultAdmin = passHash("coffeeTime!")

def checkConfig():
    os = sys.platform
    configFile = getConfigFile()
    if os != 'linux' and os != 'win32':
        os = 'other'
    if not configFile.exists():
        initConfig(os, configFile)

def initConfig(os, configFile):
    if os == 'linux':
        configDir = Path.home().joinpath('.coffeeGUI')
        if not configDir.exists():
            configDir.mkdir()
    elif os == 'other':
        configDir = Path.cwd().joinpath('config')
        configDir.mkdir()
    configFile.touch()
    with open(configFile, 'w', newline='') as f:
        fwriter = csv.writer(f,delimiter=",")
        fwriter.writerow(("CoffeePrice: ", defaultCoffee))
        fwriter.writerow(("MilkPrice: ", defaultMilk))
        fwriter.writerow(("Admin: ", defaultAdmin))

def getConfigFile():
    os = sys.platform
    if os == 'linux':
        configFile = Path.home().joinpath('.coffeeGUI', 'config.csv')
    elif os == 'win32':
        configFile = Path.home().joinpath('APPDATA', 'coffeeGUI.csv')
    else:
        configFile = Path.cwd().joinpath('config', 'config.csv')
    return configFile

def readConfig():
    valueDict = {}
    isDefault = True
    configFile = getConfigFile()
    with open(configFile, newline='') as f:
        fileReader = csv.reader(f, delimiter=",")
        for row in fileReader:
            if len(row) == 2:
                valueDict[row[0]] = int(row[1])
    coffeePrice = valueDict.get("CoffeePrice:") or defaultCoffee
    milkPrice = valueDict.get("MilkPrice:") or defaultMilk
    admin = valueDict.get("Admin:") or defaultAdmin
    if admin != defaultAdmin:
        isDefault = False
    return (coffeePrice, milkPrice, admin, isDefault)

def updateConfig(key, value):
    valueDict={}
    configFile = getConfigFile()
    with open(configFile, newline='') as f:
        fileReader = csv.reader(f, delimiter=",")
        for row in fileReader:
            if len(row) == 2:
                valueDict[row[0]] = int(row[1])
    if valueDict.get(key) != None:
        valueDict[key] = value
    with open(configFile, 'w', newline='') as f:
        fwriter = csv.writer(f,delimiter=",")
        fwriter.writerow(("CoffeePrice: ", valueDict.get("CoffeePrice:")))
        fwriter.writerow(("MilkPrice: ", valueDict.get("MilkPrice:")))
        fwriter.writerow(("Admin: ", valueDict.get("Admin:")))

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
