class Yacht:
    yachtName = ""
    length = 0.00
    speed = 0.00


def readData():
    inputFile = open("yachts.txt", "r")

    yachtsList = [] 

    for eachLine in inputFile:

        yt = eachLine.strip().split(",")

        record = Yacht()
        record.yachtName = yt[0]
        record.length = float(yt[1])
        record.speed = float(yt[2])

        yachtsList.append(record)

    inputFile.close()

    return yachtsList


def longestYacht(yachts):
    longest = yachts[0]  # store the complete yacht object

    for each in range(len(yachts)):
        print (yachts[each].length)
        if yachts[each].length > longest.length:
            longest = yachts[each]

    print (longest.yachtName + " is the longest yacht.")


def slowestYacht(yachts):
    slowest = yachts[0]  # store the complete yacht object
    position = 1

    while position < len(yachts):
        if yachts[position].speed < slowest.speed:
            slowest = yachts[position]
            print(slowest.speed)
        position = position + 1

    print(slowest.yachtName + " is the slowest yacht.")


listOfYachts = readData()
longestYacht(listOfYachts)
slowestYacht(listOfYachts)
