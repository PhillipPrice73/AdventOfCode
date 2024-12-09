DEBUG = False

# Returns if the level is safe or not
def checkIfSafe(myList):
    monotonicallyIncreasing = int(myList[0]) < int(myList[1])
    for i in range(len(myList)-1):
        difference = int(myList[i]) - int(myList[i+1])
        # adjacent levels must be different
        if difference == 0:
            return False
        elif monotonicallyIncreasing:
            if difference not in range(-3, 0):
                return False
        else: # monotonically decreasing
            if difference not in range(1, 4):
                return False

    return True


def main(input_file):
    trulySafeReportCount = 0
    partiallySafeReportCount = 0
    with open(input_file) as f:
        entries = (t.rstrip().split(sep=' ') for t in f)
        for entry in entries:
            trulySafe = checkIfSafe(entry)
            trulySafeReportCount += int(trulySafe)
            if not trulySafe:
                partiallySafe = False
                for i in range(len(entry)):
                    copiedList = entry.copy()
                    del copiedList[i]
                    partiallySafe |= checkIfSafe(copiedList)
                partiallySafeReportCount += int(partiallySafe)

    print('Number of Truly Safe Reports: {0}'.format(trulySafeReportCount))
    print('Number of Partially Safe Reports: {0}'.format(partiallySafeReportCount + trulySafeReportCount))


if __name__ == '__main__':
    if DEBUG:
        main('EdgeCases')
    else:
        main('SampleData')