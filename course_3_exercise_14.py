shift = 1
phrase = "😀🙏😇"


def scrambler(a, b):
    encrypted_phrase = ""
    for letter in b:
        encrypted_phrase += chr((((ord(letter) - 128512) + a) % 80) + 128512)
    return encrypted_phrase


print('Result: "%s"' % scrambler(shift, phrase))


