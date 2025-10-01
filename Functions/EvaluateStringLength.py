from StringLengthAdjust import *
def EvaluateStringLength(string,max_word_length=50,join=' '):
    words_in_text=string.split()
    words_in_text=list(map(StringLengthAdjust,words_in_text))
    string=join.join(words_in_text)
    return string
