text = "beautiful"

def get_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(filter(lambda char: char in vowels, text))


print(get_vowels(text))