module Day1Part1
export ProcessInput, LoadData

# parsing individual entries to return equivalent numerical value
function ProcessInput(input)
    sign = input[1]
    value = parse(Int16, input[2:end])
    if (sign == 'L')
        -value
    else
        value
    end
end

# read in input file and output vector of entries (as strings, for feeding into ProcessInput)
function LoadData(input)
    data = Nothing()
    open(input, "r") do file
        data = readlines(file)
    end
    data
end

# parse all entries and add to initialValue
function CollectEntries(input, init)
    initialValue = Int16(init)
    zeroCount = UInt8(0)
    values = LoadData(input)
    for value in values
        initialValue += ProcessInput(value)
        if ((initialValue % 100) == 0)
            zeroCount += 1
        end
    end
    zeroCount
end

end