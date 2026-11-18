def check_palindrome(text):
  if not isinstance(text, str):
    raise TypeError("Input must be a string")

  cleaned_string =""
  reversed_string =""

  for ch in text:
    if ch.isalnum():
      cleaned_string = cleaned_string + ch.lower()
  for char in cleaned_string:
    reversed_string = char + reversed_string
  return cleaned_string == reversed_string
print(check_palindrome("Madam"))
print(check_palindrome("Race Car"))
print(check_palindrome("A man, a plan, a canal: Panama"))
print(check_palindrome("Hello World"))