def count_vowels(words):
  vowels = "aeiou"
  count = 0
  for ch in words.lower():
    if ch in vowels:
      count += 1
  return count
print(count_vowels("Python Automation"))
print(count_vowels("HELLO WORLD"))
print(count_vowels("AEIOU"))