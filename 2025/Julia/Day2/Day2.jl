module Day2

export ProcessInput, GetRangeBounds, GetPotentialInvalidIds


# input is a single line, consisting of pairs of numbers separated by "-". We want to read in the line, separate by comma's, then separate the beginning and end of the range into it's own collection (tuple?), then spit out a vector of range start-end points. 
function ProcessInput(inputFile)
    data = Nothing()
    open(inputFile, "r") do file
        data = readlines(file)
        # shortcut: We know there should only be one line read in
        data = split(data[1], ",")
    end # using file
    data
end # function


# taking in a range as a string, we want to snipe off the lower and upper bound and return them as a tuple
function GetRangeBounds(rangeString)
    data = split(rangeString, "-")
    # want to keep as strings for easier manipulations later
    (data[1], data[2])
end # function


# From a range-tuple (as strings), we want to return the possible list of invalid IDs
function GetPotentialInvalidIds(rangeTuple)
    lower = parse(Int128, slice(rangeTuple[1], 1:2))
    upper = parse(Int128, slice(rangeTuple[2], 1:2))
    (lower, upper)
end # function


end # module