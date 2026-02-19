function ProcessData(input)
	data = Nothing()
	open(input) do file
		data = readlines(file)
		data = PadData(data)
		data = map(CharVectorFromString, data)
	end # open file
	data
end # ProcessData

"""
    PadData(data_vector)

Want to pad the data array with an 'empty' border for ease of checking neighbors
data_vector is a vector of strings. We want to add an empty border to this data,
meaning an extra line at the top and bottom and extra elements at the beginning
and end of each string in the middle. 
"""
function PadData(data_vector)
	blank_string = String("")
	for i in 1:(length(data_vector[1]) + 2)
		blank_string = blank_string * '.'
	end # for

	data = [""]
	data[1] = blank_string

	idx = 2
	for line in data_vector
		padded_line = String("")
		padded_line = padded_line * '.'
		for element in line
			padded_line = padded_line * element
		end # for
		padded_line = padded_line * '.'
		push!(data, padded_line)
		idx += 1
	end # for

	push!(data, blank_string)

	data
end # PadData

function CharVectorFromString(some_string)
	data = Char[]
	for char in some_string
		append!(data, char)
	end # for
	data
end # CharVectorFromString


function IdentifyAccessibleRolls(data_array)
	numRows = length(data_array)
	numCols = length(data_array[1])
	data = deepcopy(data_array)
	for row in 2:(numRows-1)
		for col in 2:(numCols-1)
			data[row][col] = NeighborCheck(data_array, row, col)
		end # for [col]
	end # for [row]
	data
end # IdentifyAccessibleRolls


"""
    NeighborCheck(data_array, row_idx, col_idx)

Taking a shortcut here. I know that I don't have to worry about boundary conditions, so no need to check them.
"""
function NeighborCheck(data_array, row_idx, col_idx)
	# if we aren't investigating a paper roll, do nothing
	if data_array[row_idx][col_idx] != '@'
		return data_array[row_idx][col_idx]
	end

	neighboring_rolls = 0
	# North
	if data_array[row_idx+1][col_idx] == '@'
		neighboring_rolls += 1
	end
	# North-East
	if data_array[row_idx+1][col_idx+1] == '@'
		neighboring_rolls += 1
	end
	# East
	if data_array[row_idx][col_idx+1] == '@'
		neighboring_rolls += 1
	end
	# South-East
	if data_array[row_idx-1][col_idx+1] == '@'
		neighboring_rolls += 1
	end
	# South
	if data_array[row_idx-1][col_idx] == '@'
		neighboring_rolls += 1
	end
	# South-West
	if data_array[row_idx-1][col_idx-1] == '@'
		neighboring_rolls += 1
	end
	# West
	if data_array[row_idx][col_idx-1] == '@'
		neighboring_rolls += 1
	end
	# North-West
	if data_array[row_idx+1][col_idx-1] == '@'
		neighboring_rolls += 1
	end

	if neighboring_rolls < 4
		'x'
	else
		data_array[row_idx][col_idx]
	end # if-else

end # NeighborCheck

function CountAccessibleRolls(data_array)
	accessible_rolls = 0
	for (_, line) in pairs(data_array)
		accessible_rolls += count(==('x'), line)
	end # for
	accessible_rolls
end # CountAccessibleRolls

function RemoveMovableRolls!(data_array)
	rolls_moved = 0
	for (i, line) in pairs(data_array)
		for (j, _) in pairs(line)
			if data_array[i][j] == 'x'
				data_array[i][j] = '.'
				rolls_moved += 1
			end # if
		end # for
	end # for
	rolls_moved > 0
end # RemoveMovableRolls!

function Solve(input)
	data = ProcessData(input)
	data = IdentifyAccessibleRolls(data)
	data = CountAccessibleRolls(data)
	data
end # Solve

function FullSweep(input)
	data = ProcessData(input)
	total_rolls_moved = 0
	rolls_to_move = true
	while (rolls_to_move)
		data = IdentifyAccessibleRolls(data)
		total_rolls_moved += CountAccessibleRolls(data)
		rolls_to_move =  RemoveMovableRolls!(data)
	end # while
	total_rolls_moved
end # FullSweep