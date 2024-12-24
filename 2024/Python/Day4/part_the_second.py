DEBUG = False

import part_the_first

class XMasBox:
    def __init__(self, fd, bd):
        self._forward_diagonal = fd
        self._backward_diagonal = bd

    def ContainsXMas(self):
        one_mas = self._forward_diagonal == "MAS" or self._forward_diagonal == "SAM"
        another_mas = self._backward_diagonal == "MAS" or self._backward_diagonal == "SAM"
        return one_mas and another_mas


def GenerateXMasBoxList(input_data):
    xmas_box_list = []
    row_count = len(input_data)
    col_count = len(input_data[0])
    for row in range(row_count - 2):
        for col in range(col_count - 2):
            forward_diagonal = input_data[row][col] + input_data[row+1][col+1] + input_data[row+2][col+2]
            backward_diagonal = input_data[row][col+2] + input_data[row+1][col+1] + input_data[row+2][col]
            xmas_box = XMasBox(forward_diagonal, backward_diagonal)
            xmas_box_list.append(xmas_box)
    return xmas_box_list


def CountXMasOccurences(list_of_x_mas_boxes):
    result = 0
    for item in list_of_x_mas_boxes:
        result += int(item.ContainsXMas())
    print("Number of X-MAS occurrences: {0}".format(result))


if __name__ == "__main__":
    if DEBUG:
        data = part_the_first.parseInput("ExampleData")
    else:
        data = part_the_first.parseInput("SampleData")

    my_list = GenerateXMasBoxList(data)
    CountXMasOccurences(my_list)
