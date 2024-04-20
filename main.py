def make_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

string = input("What would you like to decipher? (this is a shift cipher, at shift 100)")
make_cipher(string, 100)
print (make_cipher(string, 100))