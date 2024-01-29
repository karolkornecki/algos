import re


# idea how it works
# it works only for alphabet
def compress(text):
    if text is None:
        return text
    if len(text) == 0:
        return ""
    if len(text) == 1:
        return "1" + text[0]
    encoded = ""
    i = 1
    c = 1
    prev = text[0]
    while i < len(text):
        if text[i] == prev:
            c += 1
        else:
            encoded += (str(c) + prev)
            prev = text[i]
            c = 1
        i += 1
    encoded += str(c) + prev
    return encoded


def uncompress(code):
    if code is None:
        return code
    r = re.findall("\\d+[A-Z]", code)
    text = ""
    for i in r:
        for _ in range(int(i[:len(i) - 1])):
            text += i[-1]
    return text


if __name__ == "__main__":
    print(uncompress("4D1A3E"))
