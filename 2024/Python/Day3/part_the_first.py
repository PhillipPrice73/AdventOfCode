import re

DEBUG = False

def main(input_file):
    # wanting to match patterns of the form "mul(###,###)"
    multiply_regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    multiply_instances = []

    # extract all patterns matching 'mul(###,###) into a list
    with open(input_file) as f:
        for line in f:
            multiply_instances.append(multiply_regex.findall(line))

    # want to find (up to) 3 digit numbers "###"
    value_regex = re.compile(r"\d{1,3}")
    total = 0
    for sublist in multiply_instances:
        for item in sublist:
            multiplication_values = value_regex.findall(item)
            # here, I'm using the fact that I know there will be 2 and only 2 entries.
            # Is there a more resilient way to do this?
            total += int(multiplication_values[0]) * int(multiplication_values[1])

    print("Total value of all multiplications: {0}".format(total))


if __name__ == '__main__':
    if DEBUG:
        main("ExampleData")
    else:
        main("SampleData")