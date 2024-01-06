#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character"""
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
