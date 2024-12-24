import re

DEBUG = False

def main(input_file):
    # new strategy:
    # combine all lines into one string
    complete_string = ""
    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            complete_string += line

    # regex search for do() or don't() or mul(###,###) and put in a list
    #keyword_regex = re.compile(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")
    keyword_regex = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
    my_list = keyword_regex.findall(complete_string)

    # search through list, keeping track of do()/don't() ordering. Perform multiplications as necessary. Add to total
    do_multiplications = True
    #value_regex = re.compile(r"\d{1,3}")
    value_regex = re.compile(r"\d+")
    total = 0
    for item in my_list:
        if item == r"don't()":
            do_multiplications = False
            continue
        elif item == r"do()":
            do_multiplications = True
            continue

        if do_multiplications:
            multiplication_values = value_regex.findall(item)
            total += int(multiplication_values[0]) * int(multiplication_values[1])

    print("Total of all valid multiplications: {0}".format(total))


if __name__ == '__main__':
    if DEBUG:
        main("ExampleData2")
    else:
        main("SampleData")