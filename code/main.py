from preprocess import *
from regression import *

done = 0
while not done:
    fileName = input("Enter name and path of the data file: ")
    try:
        currentDate = findDate(fileName)
        date = input("Enter the date to predict price on (enter \"T/t\" for tomorrow): ")
        if date != "T" and date != "t":
            difference = int(date.split()[2]) - int(currentDate[2])
            if difference > 0:
                for j in range(difference):
                    addToFile(doTheProces(fileName), fileName)
                done = 1
            else:
                print("\nDate is not valid!")
        else:
            done = 1
    except (FileNotFoundError):
        print("\nFile Not Found!")
        done = 0

finalResults, finalNorms = [0] * 4, [100] * 4
for numberOfWindow in range(1, findNumberOfData(fileName) + 1):
    try:
        result, norms = doTheProces(fileName, numberOfWindow)
    except:
        continue

    for k in range(4):
        if norms[k] < finalNorms[k]:
            finalNorms[k] = norms[k]
            finalResults[k] = result[k]

print("\n\nPredicted Price on (", *currentDate, ") :\n")

label = ["Closing Price (USD)", "24h Open (USD)", "24h High (USD)", "24h Low (USD)"]

print(*[label[i] + ": " + str(finalResults[i]) + "   " + "norm2: " + str(finalNorms[i] * 100) + " %" for i in range(4)],sep="\n")