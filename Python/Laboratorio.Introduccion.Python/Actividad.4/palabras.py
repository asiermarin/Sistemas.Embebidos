readString = None
words_string_list = []
CONSTANT = "fin"

while (readString != CONSTANT):
    readString = input('Enter a word: ')
    words_string_list.append(readString)

for i in range(len(words_string_list)):
    print(f"{words_string_list[i]} + ------> + {len(words_string_list[i])}")