# Lucas Kobashi dos Anjos
# lucas.kobashi@cs.usask.ca

def Add(numbers):
    '''
    Adds all numbers
    :param numbers: String, numbers separated by a comma
    :return: Int, sum of numbers
    '''

    # empty string
    if numbers == "":
        return 0

    # set up delimiter
    customDelimiter = False
    delimiter = ","

    ## enable custom delimiter
    if numbers[0:2] == "//":
        customDelimiter = True

    if customDelimiter:
        delimiter = "" # reset delimiter
        counter = 0

        for char in numbers:
            if char == "\n":
                break
            else:
                delimiter += char
                counter += 1

        delimiter = delimiter[2:]
        numbers = numbers[counter:]

    numList = numbers.strip().split(delimiter)
    total = 0
    for n in numList:
        total += int(n)

    return total

# test drivers

if Add("") != 0:
    print("Error! test with empty string")

if Add("1") != 1:
    print("Error! test with single item")

if Add("11") != 11:
    print("Error! test with double-digit item")

if Add("1,2,5") != 8:
    print("Error! test with items separated without space")

if Add("1, 3, 5") != 9:
    print("Error! test with items separated with single space")

if Add("2,  4,  6") != 12:
    print("Error! test with items separated with multiple spaces")

if Add("1\n,2,3") != 6:
    print("Error! test with single new line included")

if Add("1\n,2\n,3\n") != 6:
    print("Error! test with multiple new line included")

if Add("1\n ,2\n ,3\n") != 6:
    print("Error! test with multiple new line and single spaces included")

if Add("1 \n  ,2 \n  ,3 \n ") != 6:
    print("Error! test with multiple new line and multiple spaces included")

if Add("//$\n1$2$3") != 6:
    print("Error! test with custom delimiter")

if Add("//@\n1@ 2@ 3") != 6:
    print("Error! test with custom delimiter and single space")

if Add("//!\n  1!   2!    3") != 6:
    print("Error! test with custom delimiter and multiple spaces")

if Add("//v\n  1\nv  \n 2v    \n3") != 6:
    print("Error! test with custom delimiter, multiple spaces, and new lines")