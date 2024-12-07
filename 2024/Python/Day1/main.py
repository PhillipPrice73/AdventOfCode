def main():
    # load lists
    list1 = []
    list2 = []
    with open('SampleData') as f:
        for line in f:
            line = line.rstrip()
            #I don't like this line.
            #Currently, my only alternative idea is to save data as a csv file and load that.
            el1, el2 = line.split(sep='   ')
            list1.append(int(el1))
            list2.append(int(el2))

    # sort lists (wlog in ascending order)
    list1.sort()
    list2.sort()

    totalDiff = 0
    for i in range(len(list1)):
        totalDiff += abs(list1[i] - list2[i])
    print(totalDiff)


if __name__ == '__main__':
    main()