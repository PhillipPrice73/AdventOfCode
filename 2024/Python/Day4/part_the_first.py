DEBUG = False

def countXmas(input_data):
    result = 0
    xmas = "XMAS"
    samx = "SAMX"
    # counting horizontal instances
    horizontal_count = 0
    for item in input_data:
        for i in range(len(item) - 3):
            test_word = item[i] + item[i+1] + item[i+2] + item[i+3]
            if test_word == xmas or test_word == samx:
                horizontal_count += 1
    result += horizontal_count

    # counting vertical instances
    vertical_count = 0
    for row in range(len(input_data) - 3):
        for col in range(len(input_data[row])):
            test_word = input_data[row][col] + input_data[row+1][col] + input_data[row+2][col] + input_data[row+3][col]
            if test_word == xmas or test_word == samx:
                vertical_count += 1
    result += vertical_count

    # counting diagonal instances up-left to bot-right
    diagonal_count_ul_br = 0
    for row in range(len(input_data) - 3):
        for col in range(len(input_data[row]) - 3):
            test_word = input_data[row][col]\
                + input_data[row+1][col+1]\
                + input_data[row+2][col+2]\
                + input_data[row+3][col+3]
            if test_word == xmas or test_word == samx:
                diagonal_count_ul_br += 1
    result += diagonal_count_ul_br

    # counting diagonal instances up-right to bot-left
    diagonal_count_ur_bl = 0
    for row in range(3, len(input_data)):
        for col in range(len(input_data[row]) - 3):
            test_word = input_data[row][col] \
                        + input_data[row - 1][col + 1] \
                        + input_data[row - 2][col + 2] \
                        + input_data[row - 3][col + 3]
            if test_word == xmas or test_word == samx:
                diagonal_count_ur_bl += 1
    result += diagonal_count_ur_bl

    return result

def parseInput(input_file):
    #print("Do something else here")
    result = []
    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            result.append(line)
    return result


if __name__ == "__main__":
    if DEBUG:
        data = parseInput("ExampleData")
        my_count = countXmas(data)
    else:
        data = parseInput("SampleData")
        my_count = countXmas(data)

    print("Instances of 'XMAS' in word search: {0}".format(my_count))