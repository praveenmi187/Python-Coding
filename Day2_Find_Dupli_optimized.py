def find_duplicate(text):
    seen = set()
    duplicates = []

    for ch in text.lower():
        if ch in seen:
            if ch not in duplicates:
                duplicates.append(ch)
        else:
            seen.add(ch)
    return duplicates
print(find_duplicate("Programming"))