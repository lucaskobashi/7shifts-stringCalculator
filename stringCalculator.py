# Lucas Kobashi dos Anjos
# lucas.kobashi@cs.usask.ca

import re


def Add(numbers):
    """
    Adds all positive numbers.

    Remarks:
    Whitespace is ignored.
    Error message displays only the number that triggered the error.
    If multiple delimiters are included, they should be separated by a comma
    (therefore, a comma cannot be a custom delimiter).

    :param numbers: String, numbers separated by a delimiter
    :return: Int, sum of numbers
    """

    # empty string
    if numbers == "":
        return 0

    # set up delimiter
    delimiter = ""
    customDelimiter = False
    multipleDelimiters = False

    # enable custom delimiter
    if numbers[0:2] == "//":
        customDelimiter = True

    if customDelimiter:
        counter = 0

        for char in numbers:
            if char == "\n":
                break
            else:
                delimiter += char
                counter += 1

        delimiter = delimiter[2:]
        numbers = numbers[counter:]

        if "," in delimiter:
            multipleDelimiters = True

    # remove whitespace
    numbers = re.sub(r"\s", "", numbers)

    # deal with delimiters
    if multipleDelimiters:
        regexString = ""
        for i in delimiter.split(","):
            regexString += "[" + i + "]+|"
        numbers = re.sub(regexString[0:-1], ",", numbers)
    elif customDelimiter:
        regexString = "[" + delimiter + "]+"
        numbers = re.sub(regexString, ",", numbers)

    total = 0
    for n in numbers.split(","):
        if int(n) < 0:
            raise ValueError('Negatives not allowed, error thrown by %s' % n)
        elif int(n) < 1000:
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

try:
    worked = False
    Add("-1,2,3")
except ValueError:
    worked = True
if not worked:
    print("Error! test with negative number, error not being thrown")

try:
    worked = False
    Add("-1,-2,-3")
except ValueError:
    worked = True
if not worked:
    print("Error! test with all negative numbers")

try:
    worked = False
    Add("1,2,-3")
except ValueError:
    worked = True
if not worked:
    print("Error! test with last negative number")

if Add("2, 1001") != 2:
    print("Error! test with item greater than 1000")

if Add("//$$$\n1$$$2$$$3") != 6:
    print("Error! test with delimiter of arbitrary length")

if Add("//$,@\n1$2@3") != 6:
    print("Error! test with delimiter of arbitrary length")
