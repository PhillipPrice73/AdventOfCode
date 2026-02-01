module Day1Part1
export FindPassword, FindPasswordMethod2

# parsing individual entries to return equivalent numerical value
function ProcessInput(input)
    sign = input[1]
    value = parse(Int16, input[2:end])
    if (sign == 'L')
        -value
    else
        value
    end # if
end # ProcessInput


# read in input file and output vector of entries (as strings, for feeding into ProcessInput)
function LoadData(input)
    data = Nothing()
    open(input, "r") do file
        data = readlines(file)
    end # open file
    data
end # LoadData


# parse all entries and add to initialValue
function CollectEntries(input, init)
    initialValue = Int16(init)
    zeroCount = UInt8(0)
    values = LoadData(input)
    for value in values
        initialValue += ProcessInput(value)
        if ((initialValue % 100) == 0)
            zeroCount += 1
        end # if
    end # for
    zeroCount
end # CollectEntries


"""
    CountLandsOnZero(initValue, rotationValue)

Adds rotationValue to initValue.
If the remainder modulo 100 is 0, then the dial lands on zero and we return 1
Otherwise, the dial misses zero and we return 0
"""
function CountLandsOnZero(initValue, rotationValue)
    initValue += rotationValue
    zeroCount = 0
    if (initValue % 100) == 0
        zeroCount = 1
    end # if
    (zeroCount, initValue)
end # CountLandsOnZero


"""
    FindPassword(input)

Find the password using method described in Part 1
"""
function FindPassword(input)
    initialValue = Int16(50)
    zeroCount = UInt8(0)
    values = LoadData(input)
    for value in values
        (zeroCountChange, initialValue) = CountLandsOnZero(initialValue, ProcessInput(value))
        zeroCount += zeroCountChange
    end #for
    zeroCount
end # FindPassword


"""
    CountPointAtZero(initValue, rotationValue)

Adds rotationValue to initValue.
initValue is the starting point for the padlock, rotationValue is the number of clicks we turn the value left (-) or right (+).
initValue is then modified to be in the range [0, 100), recording the number of times the padlock dial would pass the zero tick mark.
"""
function CountPointAtZero(initValue, rotationValue)
    crossesZeroCount = 0

    initValueStartsAtZero = (initValue == 0)
    initValue += rotationValue

    # I think we should be able to use div and remainder for this, no?
    countChange, initValue = divrem(initValue, 100)
    crossesZeroCount += abs(countChange)
    if (initValue < 0)
        initValue += 100
        crossesZeroCount += 1
    end # if
    if initValue == 0
     crossesZeroCount += 1
    end # if

    if (initValueStartsAtZero && (rotationValue < 0))
        crossesZeroCount -= 1
    end # if

    (crossesZeroCount, initValue)
end # CountPointAtZero


function SimpleCountPointAtZero(initValue, rotationValue)
    crossesZeroCount = 0
    initValueStartsAtZero = (initValue == 0)
    initValueStartsAt100 = (initValue == 100)
    initValue += rotationValue
    while (initValue < 0)
        initValue += 100
        crossesZeroCount += 1
    end # while
    while (initValue > 100)
        initValue -= 100
        crossesZeroCount += 1
    end # while

    # taking care of boundary conditions
    if (initValue == 0) || (initValue == 100)
        crossesZeroCount += 1
    end # if
    if (initValueStartsAtZero && (rotationValue < 0))
        crossesZeroCount -= 1
    end # if
    if (initValueStartsAt100 && (rotationValue > 0))
        crossesZeroCount -= 1
    end # if

    (crossesZeroCount, initValue)
end # SimpleCountPointsAtZero


"""
    FindPasswordMethod2(input)

Find password using method described in Part 2
"""
function FindPasswordMethod2(input)
    initialValue = Int16(50)
    zeroCount = UInt8(0)
    values = LoadData(input)
    for value in values
        (zeroCountChange, initialValue) = SimpleCountPointAtZero(initialValue, ProcessInput(value))
        zeroCount += zeroCountChange
    end # for
    zeroCount
end # FindPasswordMethod2

end # module