def count_character(text):
    freq={}

    for char in text:
        if char.isalpha():
            char= char.lower()

            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    sorted_freq={}

    for key in sorted(freq):
        sorted_freq[key]=freq[key]
    return sorted_freq

text = "Namrata Anabhavane 123"
print(count_character(text))
