def reverse_word(text):
    words = text.split()
    reversed_words = ""

    for word in words:
        reversed_string =""

        for ch in word:
            reversed_string = ch + reversed_string

        if reversed_words == "":
            reversed_words = reversed_string
        else:
            reversed_words = reversed_words + " " + reversed_string
    return reversed_words
print(reverse_word("I LOVE MYSELF"))

