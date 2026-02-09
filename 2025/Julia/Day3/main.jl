"""
    ProcessInput(inputFile)

inputFile - input file containing data

output - vector of a vectors of unsigned ints
"""
function ProcessInput(inputFile)
	data = Nothing()
	open(inputFile, "r") do file
		data = readlines(file)
		data = map(IntArrayFromString, data)
	end # file i/o
	data
end # ProcessInput

"""
    IntArrayFromString(inputString)

input - string to be converted.
	no error checking being done, assuming string is purely numeric (e.g., "12335412425")

output - vector of integers based on the input string
	e.g., "123456" -> [1, 2, 3, 4, 5, 6]
"""
function IntArrayFromString(inputString)
	output = Int16[]
	for char in inputString
		append!(output, parse(Int16, char))
	end # for
	output
end # IntArrayFromString

"""
    GetLargestJoltage(batteryBank)

input - battery bank as a vector of ints
numValues - number of batteries we want to grab from the battery bank

output - largest possible joltage producible by the battery bank as a single int
"""
function GetLargestJoltage(batterybank, numValues)
	idx = 1
	total = 0
	for i in range(1, numValues)
		intermediate = numValues-i
		batteryBankSubset = batterybank[idx:end-intermediate] # if we're finding the nth of m batteries, it can't be in the last m-n batteries
		value, newidx = GetHighestSingleJoltageBattery(batteryBankSubset)
		idx += newidx
		total += value * (10 ^ intermediate)
	end # for
	total
end

"""
    GetHighestSingleJoltageBattery(batteryBank)

input - battery bank as a vector of ints

output - highest joltage battery and the index of said battery
"""
function GetHighestSingleJoltageBattery(batteryBank)
	for i in range(start=9, step=-1, stop=1)
		idx = findfirst(isequal(i), batteryBank)
		if (!(isnothing(idx)))
			return i, idx
		end # if
	end # for
end # GetHighestSingleJoltageBattery

"""
    Solve(input, numBatteries)

input - path to input file
numBatteries - The number of batteries we need to get from the battery bank

output - solution to challenge
"""
function Solve(input, numBatteries)
	data = ProcessInput(input)
	data = map(GetLargestJoltage, data, fill(numBatteries, length(data)))
	sum(data)
end # Solve
