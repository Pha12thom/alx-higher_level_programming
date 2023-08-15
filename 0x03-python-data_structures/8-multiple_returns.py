#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_1 = ""
    for word in sentence:
        if sentence is None:
            return None
        else:
            sentence_1 += word
    return (len(sentence_1), sentence_1[0])
