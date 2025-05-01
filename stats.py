def  get_num_words(file_contents):
    if file_contents.strip() == "":
        return 0
    
    num_words = file_contents.split()
    return len(num_words)


def get_char_frequency(file_contents):
    if file_contents.strip() == "":
        return 0

    frequency = {}

    for char in file_contents.lower():
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def sort_on(char_frequency):
    return char_frequency["num"]

def char_frequency_to_sorted_list(char_frequency):
    frequency_sorted = []
    for char in char_frequency:
        frequency_sorted.append({"char": char, "num": char_frequency[char]})
    frequency_sorted.sort(reverse=True, key=sort_on)

    return(frequency_sorted)

