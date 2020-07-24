sentence = input("Enter a sentence: ")
dict_sentence = {}

for i in sentence:
    if i in dict_sentence:
        dict_sentence[i] += 1
    else:
        dict_sentence[i] = 1
print(dict_sentence)