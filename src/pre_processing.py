import nltk
import unicodedata
import re


hashtag_mention_matcher = re.compile(r'\S*(#|@)(?:\[[^\]]+\]|\S+)')
url_matcher = re.compile(r'[A-Za-z]+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&~\?\/.=]+')


def normalize(string):
    if string is not None:
        return ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))
    else:
        return ''


def tokenize(string, lower=True):
    if lower:
        return nltk.wordpunct_tokenize(string.lower().strip())
    else:
        return nltk.wordpunct_tokenize(string.strip())


def tokenize_and_normalize(string, lower=True):
    if lower:
        return nltk.wordpunct_tokenize(normalize(string).lower().strip())
    else:
        return nltk.wordpunct_tokenize(normalize(string).strip())


def prepare_char_ngram(string):
    if string is not None:
        return re.sub(r'\s', '_', string) + '$'
    else:
        return u''


def prepare_word_ngram(string):
    return [token for token in tokenize_and_normalize(string) if len(token) > 1]


def remove_hashtags_and_mentions(string):
    if string is not None:
        return hashtag_mention_matcher.sub('', string)


def remove_links(string):
    if string is not None:
        return url_matcher.sub('', string)


def remove_line_breaks(string):
    return re.sub(r'(\n|\r)', ' ', string)
