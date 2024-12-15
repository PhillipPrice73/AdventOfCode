import re

DEBUG = False

def main(input_file):
    #print("Do something here")
    # Composing all separate lines into one string, as do/don't can happen between lines.
    complete_string = ""
    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            complete_string += line

    # input data starts with an implicit do()
    # Taking everything between don't() and do() and replacing with nothing
    p = re.compile(r"don't\(\).*?do\(\)")
    active_multiplies = re.sub(p, "", complete_string)

    # find all instances of mul(###,###), multiply all values, calculate and return total
    # same problem/algorithm as part 1
    multiply_regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    multiply_instances = multiply_regex.findall(active_multiplies)
    total = 0
    value_regex = re.compile(r"\d{1,3}")
    for item in multiply_instances:
        multiplication_values = value_regex.findall(item)
        total += int(multiplication_values[0]) * int(multiplication_values[1])

    print("Total of all valid multiplications: {0}".format(total))


if __name__ == '__main__':
    if DEBUG:
        main("ExampleData2")
    else:
        main("SampleData")