# Lucas Kobashi dos Anjos
# lucas.kobashi@cs.usask.ca

def Add(numbers):
    '''
    Adds all numbers
    :param numbers: String, numbers separated by a comma
    :return: Int, sum of numbers
    '''
    if numbers == "":
        return 0
    numList = numbers.strip().split(',')
    total = 0
    for n in numList:
        total += int(n)

    return total

# test drivers

if Add("") != 0:
    print("Error! test with empty string")

if Add("1") != 1:
    print("Error! test with single item")

if Add("1,2,5") != 8:
    print("Error! test with items separated without space")

if Add("1, 3, 5") != 9:
    print("Error! test with items separated with single space")

if Add("2,  4,  6") != 12:
    print("Error! test with items separated with multiple spaces")