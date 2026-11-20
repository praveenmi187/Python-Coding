#Two strings are anagrams if they contain the same characters with the same frequency, but in a different order.

def check_anagrams(str1, str2):
    str1_freq = {}
    str2_freq = {}
    cleared_str1 = ""
    cleared_str2 = ""

    for ch in str1.lower():
        if ch.isalnum():
            cleared_str1 += ch
            if ch in str1_freq:
                str1_freq[ch] += 1
            else:
                str1_freq[ch] = 1
    
    for char in str2.lower():
        if char.isalnum():
            cleared_str2 += char
            if char in str2_freq:
                str2_freq[char] += 1
            else:
                str2_freq[char] = 1
    if len(str1) != len(str2):
        return False

    return str1_freq == str2_freq
print(check_anagrams("Silent", "Listen"))
print(check_anagrams("Python 123!", "I love you 143!"))
print(check_anagrams("race", "care"))

