#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_1 = ""
    if sentence is None:
        sentence[0] = None
    else:
        for word in sentence:
            sentence_1 += word
    return sentence_1
