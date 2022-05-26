# ----------------------------------------------- First Anagram Test Start -----------------------------------------------

def find_anagram(str1, str2):
    str1 = 'Late'
    str2 = 'Hate'
    str1_anagram = sorted(str1)
    str2_anagram = sorted(str2)

    if str1_anagram == str2_anagram:
        return True
    else:
        return False

print(find_anagram('Late', 'Hate'))

#Anagram confirmation should return 'False'

# ----------------------------------------------- First Anagram Test End -----------------------------------------------



# ----------------------------------------------- Second Anagram Test End -----------------------------------------------

def find_anagram(str1, str2):
    str1 = 'Satan'
    str2 = 'Santa'
    str1_anagram = sorted(str1)
    str2_anagram = sorted(str2)

    if str1_anagram == str2_anagram:
        return True
    else:
        return False

print(find_anagram('Satan', 'Santa'))

#Anagram confirmation should return 'True'

# ----------------------------------------------- Second Anagram Test End -----------------------------------------------