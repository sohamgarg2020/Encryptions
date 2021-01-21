alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def vignere_encrypt(text, number):
    char_letter = ""
    for word in text.split():
        for char in word:
            if not(char.isalpha()):
                return f"Make sure you only use letters when you want to encrypt"
            char_num = int(alpha_list.index(char.lower()))
            new_char_num = int(char_num + int(number))
            new_char_num %= 26
            char_letter += str(alpha_list[int(new_char_num)])
        char_letter += " "
    return f"Encrypted text is: {char_letter.rstrip()}"

print(vignere("text", "5"))