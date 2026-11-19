def first_non_repeating(text):
    freq = {}

    for ch in text.lower():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for char in text.lower():
        if freq[char] == 1:
            return char
    return None
print(first_non_repeating("programming"))
print(first_non_repeating("aabbcc"))
print(first_non_repeating("swiss"))