alphabet = " abcdefghijklmnopqrstuvwxyz"
shift = 27
phrase = "abc"


def scrambler(a, b):
    encrypted_phrase = ""
    for letter in b:
        encrypted_phrase += alphabet[(alphabet.find(letter) + a) % 27]
    return encrypted_phrase


print('Result: "%s"' % scrambler(shift, phrase))
