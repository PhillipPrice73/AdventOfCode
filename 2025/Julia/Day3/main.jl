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

output - largest possible joltage producible by the battery bank as a single int
"""
function GetLargestJoltage(batteryBank)
	largestValue, idx = GetHighestSingleJoltageBattery(batteryBank)
	secondValue, _ = GetHighestSingleJoltageBattery(batteryBank[idx+1:end], true)
	return (largestValue * 10) + secondValue
end # GetLargestJoltage

"""
    GetHighestSingleJoltageBattery(batteryBank)

input - battery bank as a vector of ints
secondPass - is this our second look at the battery bank?
	On the first pass, we need at least one additional battery. On the second pass, we don't care and can use the last battery

output - highest joltage battery and the index of said battery
	If the highest joltage battery is the last battery in the bank, we need to look again as we ultimately need two batteries
"""
function GetHighestSingleJoltageBattery(batteryBank, secondPass=false)
	for i in range(start=9, step=-1, stop=1)
		idx = findfirst(isequal(i), batteryBank)
		if (
			!(isnothing(idx)) # we found the item
			&& (idx != length(batteryBank) || secondPass) # if it's the first pass, we can't use the last battery. If it's the second pass, we can
			)
			return i, idx
		end 
	end # for
end # GetHighestSingleJoltageBattery

"""
    Solve(input)

input - path to input file

output - solution to challenge
"""
function Solve(input)
	data = ProcessInput(input)
	data = map(GetLargestJoltage, data)
	sum(data)
end # Solve
