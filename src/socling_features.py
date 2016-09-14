import pre_processing as pp
import username_utils as names
from regex import *


# Find if there is a male first name in the username a return its position (0 = not found)
def find_male_name(name_tokens):
    for token in name_tokens:
        if token in names.name_dict.keys() and names.name_dict[token] == 'M':
            return 1
    return 0


# Find if there is a male first name in the username a return its position (0 = not found)
def find_female_name(name_tokens):
    for token in name_tokens:
        if token in names.name_dict.keys() and names.name_dict[token] == 'F':
            return 1
    return 0


# Find if there is a male nickname name in the username a return its position (0 = not found)
def find_male_nickname(name_tokens):
    for token in name_tokens:
        if token in names.abrv_dict.keys() and names.abrv_dict[token] == 'M':
            return 1
    return 0


# Find if there is a female nickname name in the username a return its position (0 = not found)
def find_female_nickname(name_tokens):
    for token in name_tokens:
        if token in names.abrv_dict.keys() and names.abrv_dict[token] == 'F':
            return 1
    return 0


def find_male_key_word(name_tokens):
    for token in name_tokens:
        if token in names.key_words_dict.keys() and names.key_words_dict[token] == 'M':
            return 1
    return 0


def find_female_key_word(name_tokens):
    for token in name_tokens:
        if token in names.key_words_dict.keys() and names.key_words_dict[token] == 'M':
            return 1
    return 0


# Find if username starts with an o
# TODO mudar para regex de forma a ignorar caracteres especiais antes do 'o' (ex '-O Champ')
def starts_with_o(name_tokens):
    return 1 if 'o' == name_tokens[0] else 0


# Find if username starts with a
def starts_with_a(name_tokens):
    return 1 if 'a' == name_tokens[0] else 0


# Find repeated alphabets in username (ex Joanaaaaa)
def repeated_alphabet(name):
    if repeated_pattern.search(name) is not None:
        return 1
    else:
        return 0


# Find tokens in CAPS
def caps(name):
    if caps_pattern.search(name) is not None:
        return 1
    else:
        return 0


# Find bigrams that express possession ('ex meu perfil')
def possessive_bigrams(tokens):
    res = []
    i=0
    for token in tokens:
        if token in ['meu', 'minha', 'meus', 'minhas', 'my']:
            if len(tokens) > i+1:
                res += (token, tokens[i+1])
        i+=1

    return 1 if len(res) > 0 else 0


def find_snapchat_link(description):
    if snap_pattern.search(description) is not None:
        return 1
    else:
        return 0


def find_tumblr_link(description):
    if tumblr_pattern.search(description) is not None:
        return 1
    else:
        return 0


def find_instagram_link(description):
    if insta_pattern.search(description) is not None:
        return 1
    else:
        return 0


def find_ellipses(string):
    if ellipse_pattern.search(string):
        return 1
    else:
        return 0


def find_self_mentions(string):
    if self_pattern.search(string):
        return 1
    else:
        return 0


def find_affirmation(string):
    if yes_pattern.search(string):
        return 1
    else:
        return 0


def find_laughter(string):
    if laugh_pattern.search(string):
        return 1
    else:
        return 0


def find_exclaim(string):
    if exc_pattern.search(string):
        return 1
    else:
        return 0


def find_question(string):
    if question_pattern.search(string):
        return 1
    else:
        return 0


def extract_username_socling_features(username):
    normalized_tokens = pp.tokenize_and_normalize(username)

    if normalized_tokens:
        feature_list = [
            find_male_name(normalized_tokens),
            find_female_name(normalized_tokens),
            find_male_nickname(normalized_tokens),
            find_female_nickname(normalized_tokens),
            find_male_key_word(normalized_tokens),
            find_female_key_word(normalized_tokens),
            starts_with_o(normalized_tokens),
            starts_with_a(normalized_tokens),
            repeated_alphabet(pp.normalize(username)),
            caps(pp.normalize(username))
        ]
        return feature_list
    else:
        return [0] * 10


def extract_description_socling_features(description):
    if description is not None:
        normalized_tokens = pp.tokenize_and_normalize(description)

        feature_list = [
            find_male_name(normalized_tokens),
            find_female_name(normalized_tokens),
            find_male_nickname(normalized_tokens),
            find_female_nickname(normalized_tokens),
            find_male_key_word(normalized_tokens),
            find_female_key_word(normalized_tokens),
            repeated_alphabet(pp.normalize(description)),
            caps(pp.normalize(description)),
            possessive_bigrams(normalized_tokens),
            find_snapchat_link(pp.normalize(description)),
            find_instagram_link(pp.normalize(description)),
            find_tumblr_link(pp.normalize(description))
        ]
    else:
        feature_list = [0] * 12

    return feature_list


def extract_tweet_socling_features(tweet):
    if tweet is not None:
        text = pp.normalize(tweet)

        feature_list = [
            find_ellipses(text),
            possessive_bigrams(pp.tokenize_and_normalize(tweet)),
            find_self_mentions(text),
            caps(text),
            find_affirmation(text),
            find_laughter(text),
            find_exclaim(text),
            find_question(text),
            repeated_alphabet(text)
        ]
    else:
        feature_list = [0] * 9

    return feature_list


def get_socling_features(user, fields):
    res = []
    for f in fields:
        if f == 'name':
            res += extract_username_socling_features(user[f])
        elif f == 'description':
            res += extract_description_socling_features(user[f])
    return res


def get_socling_feature_names(field):
    if field is 'name':
        return ['male_name', 'male_nick', 'female_name', 'female_nick',
                'starts_o', 'starts_a', 'repeated_alphabet', 'caps']
    if field is 'description':
        return ['male_name', 'male_nick', 'female_name', 'female_nick',
                'repeated_alphabet', 'caps', 'possession', 'snapchat_link', 'instagram_link', 'tumblr_link']