def isPalindrome(input_string):
    '''
    :param input_string: str, case non included, lower and upper cases treated as equal
    :return: bool, True if input_string is palindrome, False otherwise
    '''
    # change string to lower case, put string to new variable to preserve input_string
    compare_string = input_string.casefold()
    # length of string, proposed for better code view
    length = len(compare_string)
    # loop to half the string, check with other half, return False if any failed, True if all ok
    for i in range(int(length//2)):
        if compare_string[i] != compare_string[length-1-i]:
            return False
    return True


print("is 'madam' palindrome? :", isPalindrome("madam"))
print("is 'MadDam' palindrome? :", isPalindrome("MadDam"))
print("is 'gentle man' palindrome? :", isPalindrome("gentle man"))

test_string = "QSTMaMtSq"
print("test_string before isPalindrome: ", test_string)
isPalindrome(test_string)
print("test_string after isPalindrome: ", test_string, ". No alternation done to the variable.")
