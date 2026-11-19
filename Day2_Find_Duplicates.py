def find_duplicates(text):
    seen = set()
    duplicates = []

    for ch in text.lower():
        if ch not in seen:
           seen.add(ch)
        else:
            duplicates.append(ch)
        
    return duplicates
print(find_duplicates("Programming"))            