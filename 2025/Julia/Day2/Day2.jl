# input is a single line, consisting of pairs of numbers separated by "-". We want to read in the line, separate by comma's, then separate the beginning and end of the range into it's own collection (tuple?), then spit out a vector of range start-end points. 
"""
    ProcessInput(inputFile)

inputFile is expected to be a single line containing comma-separated ranges of the form #####-#####,####-####,...
"""
function ProcessInput(inputFile)
    data = Nothing()
    open(inputFile, "r") do file
        data = readlines(file)
        # shortcut: We know there should only be one line read in
        data = split(data[1], ",")
    end # using file
    data
end # ProcessInput

"""
    SplitRange(rangeString)

taking in a range as a string of the form "###-###", we want to snipe off the lower and upper bound and return them as a tuple
Keeping the result as a string for easier manipulation later
"""
function SplitRange(rangeString)
    temp = split(rangeString, "-")
    (temp[1], temp[2])
end # SplitRange

"""
    GetRangeBounds(rangeString)

TBW
"""
function GetRangeBounds(rangeStrings)
    data = map(SplitRange, rangeStrings)
    data
end # GetRangeBounds


# From a range-tuple (as strings), we want to return the possible list of invalid IDs
"""
    GetPotentialInvalidIds(rangeTuple)

TBW
"""
function GetPotentialInvalidIds(rangeTuple)
    lowerLength = length(rangeTuple[1]) 
    upperLength = length(rangeTuple[2])

    # Want the first "half" of each incoming number. 
    # For odd-length numbers, we want to round up (111 -> 11).
    # adding one to the length b/c div rounds down for integer division (works for odd-length numbers, doesn't affect even-length numbers)
    # div(3,2) = 1, div(4,2) = 2  (111 -> 11)
    # div(4,2) = 2, div(5,2) = 2  (1111 -> 11)
    temp = ""
    # if the lower bound has an odd length, want to report the smallest possible number higher than the bound
    # e.g., lower bound = 111 -> 1010
    if (lowerLength % 2 != 0)
        temp = "1"
        for i = 1:((lowerLength-1)/2)
            temp *= "0"
        end # for
    else
        temp = SubString(rangeTuple[1], 1, div(lowerLength+1,2))
    end # if
    lowerBound = parse(Int128, temp)

    # similarly, if the higher bound has an odd length, want to report the highest possible value smaller than the bound
    # e.g., upper bound = 111 -> 99
    temp = ""
    if (upperLength % 2 != 0)
        for i = 1:((upperLength-1)/2)
            temp *= "9"
        end # for
    else
        temp = SubString(rangeTuple[2], 1, div(upperLength+1,2))
    end # if
    upperBound = parse(Int128, temp)

    values = []
    for i = lowerBound:upperBound
        valueAsString = string(i) * string(i)
        append!(values, parse(Int128, valueAsString))
    end # if
    values
end # GetPotentialInvalidIds

function Help(rangeTuples)
    data = map(GetPotentialInvalidIds, rangeTuples)
    data
end # Help


function FindInvalidIds(data)
    (dataRange, invalidIdRange) = data
    # dataRange = data[1]
    # invalidIdRange = data[2]
    # println(dataRange, "\t", invalidIdRange)
    temp = Int128[]
    for r = dataRange[1]:dataRange[2]
        if r in invalidIdRange
            append!(temp, r)
        end # if
    end #for
    temp
end # FindInvalidIds

function IntFromString(stringTuple)
    (parse(Int128, stringTuple[1]), parse(Int128, stringTuple[2]))
end # IntFromString

function Solve(input)
    rangeBounds = GetRangeBounds(ProcessInput(input))
    potentialInvalidIds = Help(rangeBounds)
    
    rangeBounds = map(IntFromString, rangeBounds)
    foo = zip(rangeBounds, potentialInvalidIds)
    bar = map(FindInvalidIds, foo)
    sum(map(sum, bar))
end # Solve


function FindInvalidIdsPart2(rangeBounds)
    values = Int128[]
    for i = rangeBounds[1]:rangeBounds[2]
        numLength = length(string(i))
        for j = 1:(div(numLength, 2))
            if ((numLength%j) != 0)
                continue
            end # if
            temp = SubString(string(i), 1, j)
            if i == parse(Int128, temp ^ div(numLength, j))
                append!(values, i)
                break
            end # if
        end # for(j)
    end # for(i)
    values
end # FindInvalidIdsPart2

function SolvePart2(input)
    rangeBounds = map(IntFromString, GetRangeBounds(ProcessInput(input)))
    sum(map(sum, map(FindInvalidIdsPart2, rangeBounds)))
end # SolvePart2


function ForLoopDebug()
    sum = 0
    for i = 1:1
        sum += i
    end #for
    sum
end # ForLoopDebug