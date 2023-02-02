import csv

def findNumberOfData(fileName):
    with open(fileName) as dataFile:
        lineCount = 0
        for line in dataFile:
            lineCount += 1
    return lineCount


def findDate(fileName):
    with open(fileName) as dataFile:
        date = dataFile.readlines()[-1].split(",")[1].split("-")
        return [date[0], date[1], str(int(date[2]) + 1)]


def getData(fileName, column):
    data = []
    rowNumber = 0
    with open(fileName) as dataFile:
        for row in dataFile:
            if rowNumber != 0:
                row = row.split(",")
                data.append(row[column])
            else:
                rowNumber += 1
    return [float(x) for x in data]


def addToFile(dataToAdd, fileName):
    dataToAdd = ["BTC"] + ["-".join(findDate(fileName))] + dataToAdd
    with open(fileName, "a") as dataFile:
        writer = csv.writer(dataFile)
        writer.writerow(dataToAdd)