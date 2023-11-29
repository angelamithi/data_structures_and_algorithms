import string

def word_frequency(sentence):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.lower().translate(translator)
    words = cleaned_sentence.split()
    dict_frequency = {}

    for word in words:
        if word in  dict_frequency:
             dict_frequency[word] += 1
        else:
             dict_frequency[word] = 1

    return  dict_frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
