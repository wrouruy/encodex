def CaesarCipher(string, shifting):
    endString = ''
    for i in string:
        endString += chr(ord(i) + shifting)
    return endString
# print(CaesarCipher('Ifmmp-!xpsme"', -1)) # output: Hello, world!

def atbashCipher(text):
    def transform(char, start, end):
        return chr(start + end - ord(char))
    result = ''

    for char in text:
        if 'A' <= char <= 'Z':
            result += transform(char, ord('A'), ord('Z'))
        elif 'a' <= char <= 'z':
            result += transform(char, ord('a'), ord('z'))
        elif 'А' <= char <= 'Я':
            result += transform(char, ord('А'), ord('Я'))
        elif 'а' <= char <= 'я':
            result += transform(char, ord('а'), ord('я'))
        else:
            result += char

    return result
# print(atbashCipher('Svool, dliow!')) # output: Hello, world!