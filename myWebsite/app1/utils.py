import secrets as sec
from math import floor

def parse_URL_param (url_param):
    return url_param.replace("_", " ")


def generateAccessKey(key_length, db_compatible):
    key = ""
    generator = sec.SystemRandom()
    if db_compatible:
        for i in range(key_length):
            number = floor(48 + 36 * generator.random())
            if (number > 57):
                number += 7

            key += chr(number)

    else:
        for i in range(key_length):
            key += chr(floor(93 * generator.random()) + 33)

    return key