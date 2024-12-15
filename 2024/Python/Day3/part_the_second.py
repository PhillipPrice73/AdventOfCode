import re

DEBUG = False

def main(input_file):
    #finding multiply instructions that should be ignored in the middle of lines
    inactive_multiplies = re.compile(r"don't\(\).*?do\(\)")
    # if the last valid instruction in a line is don't(), want to ignore everything after that
    trailing_inactive_multiplies = re.compile(r"don''t\(\).*")
    multiply_regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    value_regex = re.compile(r"\d{1,3}")
    total = 0
    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            active_multiplies = re.sub(inactive_multiplies, "", line)
            active_multiplies = re.sub(trailing_inactive_multiplies, "", active_multiplies)

            multiply_instances = multiply_regex.findall(active_multiplies)
            for item in multiply_instances:
                multiplication_values = value_regex.findall(item)
                total += int(multiplication_values[0]) * int(multiplication_values[1])

    print("Total of all valid multiplications: {0}".format(total))


if __name__ == '__main__':
    if DEBUG:
        main("ExampleData2")
    else:
        main("SampleData")