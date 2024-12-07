from sys import set_int_max_str_digits

DEBUG = False

def updateDictionary(dictionary, key):
    if key in dictionary.keys():
        dictionary[key] += 1
    else:
        dictionary[key] = 1


def main():
    list1 = []
    list2 = []
    similarity_dict = {}

    # load lists
    if DEBUG:
        # example lists, useful for prototyping solutions
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]

    else:
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

    # Creating dictionary for similarity score
    for element in list2:
        updateDictionary(dictionary=similarity_dict, key=element)

    totalDiff = 0
    totalSimilarity = 0
    for i in range(len(list1)):
        totalDiff += abs(list1[i] - list2[i])
        # why did I have to convert to a string here, but leaving as an int was fine with example data?
        # ans: It had to do with how I was adding the key to the dictionary. There was a subtle difference in how I was handling the example data vs the sample data
        similarityFactor = 0 if list1[i] not in similarity_dict.keys() else similarity_dict[list1[i]]
        totalSimilarity += list1[i] * similarityFactor
    print('Total Distance: {0}'.format(totalDiff))
    print('Similarity Score: {0}'.format(totalSimilarity))


if __name__ == '__main__':
    main()