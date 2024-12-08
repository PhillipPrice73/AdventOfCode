DEBUG = True

def checkIfSafe(myList):
    isTrulySafe = True
    monotonicallyIncreasing = int(myList[0]) < int(myList[1])

    firstUnsafeLevel = None
    for i in range(len(myList)-1):
        difference = int(myList[i]) - int(myList[i+1])
        # adjacent levels must be different
        if difference == 0:
            isTrulySafe = False
            firstUnsafeLevel = myList[i+1]
            break
        elif monotonicallyIncreasing:
            if difference not in range(-3, 0):
                isTrulySafe = False
                firstUnsafeLevel = myList[i + 1]
                break
        else: # monotonically decreasing
            if difference not in range(1, 4):
                isTrulySafe = False
                firstUnsafeLevel = myList[i + 1]
                break

    # trying again, removing first level making report unsafe
    isPartiallySafe = True
    if not isTrulySafe:
        dampedReport = myList.copy()
        dampedReport.remove(firstUnsafeLevel)
        monotonicallyIncreasing = int(dampedReport[0]) < int(dampedReport[1])

        for i in range(len(dampedReport) - 1):
            difference = int(dampedReport[i]) - int(dampedReport[i + 1])
            # adjacent levels must be different
            if difference == 0:
                isPartiallySafe = False
                break
            elif monotonicallyIncreasing:
                if difference not in range(-3, 0):
                    isPartiallySafe = False
                    break
            else:  # monotonically decreasing
                if difference not in range(1, 4):
                    isPartiallySafe = False
                    break

    #return 1 if isSafe else 0
    return (int(isTrulySafe), int(isPartiallySafe))


def main(input_file):
    trulySafeReportCount = 0
    partiallySafeReportCount = 0
    with open(input_file) as f:
        entries = (t.split(sep=' ') for t in f)
        for entry in entries:
            #safeReportCount += checkIfSafe(entry)
            trulySafeIncrement, partiallySafeIncrement = checkIfSafe(entry)
            trulySafeReportCount += trulySafeIncrement
            partiallySafeReportCount += partiallySafeIncrement

    print('Number of Truly Safe Reports: {0}'.format(trulySafeReportCount))
    print('Number of Partially Safe Reports: {0}'.format(partiallySafeReportCount))


if __name__ == '__main__':
    if DEBUG:
        main('ExampleData')
    else:
        main('SampleData')