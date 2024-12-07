def main():
    # load lists
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    # sort lists (wlog in ascending order)
    list1.sort()
    list2.sort()

    totalDiff = 0
    for i in range(len(list1)):
        totalDiff += abs(list1[i] - list2[i])
    print(totalDiff)


if __name__ == '__main__':
    main()