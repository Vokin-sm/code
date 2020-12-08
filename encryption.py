text = 'Day, mice. "Year" is a mistake!'


def caesar_cipher(original_phrase):
    result = ""
    symbols = "qwertyuioplkjhgfdsazxcvbnm "
    phrase_without = original_phrase
    for c in phrase_without:
        if c.lower() not in symbols:
            phrase_without = phrase_without.replace(c, "")
    phrase_without = phrase_without.split()
    original_phrase = original_phrase.split()
    for i in range(len(original_phrase)):
        if i > 0:
            result += " "
        for j in original_phrase[i]:
            if j.isalpha():
                if j.isupper():
                    result += chr((((ord(j) - ord("A")) + len(phrase_without[i])) % 26) + ord("A"))
                else:
                    result += chr((((ord(j) - ord("a")) + len(phrase_without[i])) % 26) + ord("a"))
            else:
                result += j
    return result


print(caesar_cipher(text))