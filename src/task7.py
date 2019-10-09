# #!/usr/bin/env python3


def verbing(word):
    if len(word) >= 3:
        if word[-3:] == "ing":
            return word[:-3] + "ly"
        else:
            return word + "ing"

    return word


def not_bad(text):
    return text[:text.find('not')] + 'good' + text[text.find('bad') + 3:]



