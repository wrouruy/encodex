def CaesarCipher(string, shifting):
    result = ''
    for i in string:
        result += chr(ord(i) + shifting)
    return result
# print(CaesarCipher('Ifmmp-!xpsme"', -1)) # output: Hello, world!

def atbashCipher(string):
    def transform(char, start, end):
        return chr(start + end - ord(char))
    result = ''

    for char in string:
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

def mirrorCipher(string):
    return ''.join(list(string)[::-1])
# print(mirrorCipher('!dlrow ,olleH')) # output: Hello, world!
