from string import ascii_lowercase


def is_pangram(sentence):
    return all(chr in sentence.lower() for chr in ascii_lowercase)
