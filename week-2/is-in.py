def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False

    if len(aStr) == 1:
        return aStr == char

    middleIndex = len(aStr)//2
    middleChar = aStr[middleIndex]
    print(middleChar, middleIndex, aStr[middleIndex:])
    if char == middleChar:
        return True
    elif char < middleChar:
        return isIn(char, aStr[:middleIndex])
    else:
        return isIn(char, aStr[middleIndex+1:])


print(isIn('a', 'abcdefghijklmnopqrstuvwxyz'))


# abcdefghijklmnopqrstuvwxyz
