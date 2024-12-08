DEBUG = True

def checkIfSafe(myList):
    isSafe = True
    monotonicallyIncreasing = int(myList[0]) < int(myList[1])

    for i in range(len(myList)-1):
        difference = int(myList[i]) - int(myList[i+1])
        # adjacent levels must be different
        if difference == 0:
            isSafe = False
        elif monotonicallyIncreasing:
            if difference not in range(-3, 0):
                isSafe = False
        else: # monotonically decreasing
            if difference not in range(1, 4):
                isSafe = False

    # Report is safe
    return 1 if isSafe else 0


def main(input_file):
    safeReportCount = 0
    with open(input_file) as f:
        entries = (t.split(sep=' ') for t in f)
        for entry in entries:
            safeReportCount += checkIfSafe(entry)

    print('Number of Safe Reports: {0}'.format(safeReportCount))


if __name__ == '__main__':
    if DEBUG:
        main('ExampleData')
    else:
        main('SampleData')