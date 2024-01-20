import re

filepath = "C:\\Users\\dateuser\\Desktop\\input.txt"

word_to_number = {
    'zero' : 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
def find_digits(string):
   
    substrings_with_indices = []

    for word in word_to_number.keys():
        index = string.find(word)
        #Finding the index and digits
        while index != -1:
            substrings_with_indices.append((word, index))
            index = string.find(word, index + 1)
            
    #Sorting based on the indices
    substrings_with_indices.sort(key=lambda x: x[1])

    #list of sorted keys, I think i   need it! I should check!
    substrings_translated = [word_to_number[word] for word, _ in substrings_with_indices]
    
    #finding the first and last digits
    if len(substrings_translated) > 0:
        a = substrings_translated[0]
        b = substrings_translated[-1]
        return a*10 + b
    else:
        return 0


if __name__ == '__main__':
    f = open(filepath, "r")
    file_data = f.read()
    #split the file based on the lines
    text_line = file_data.splitlines()
    sum1 = 0
    for line in text_line:
       digits = find_digits(line)
       sum1 += digits
    print(sum1)
