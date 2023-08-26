# Caesar cipher
# Original alphabet: abcdefghijklmnopqrstuvwxyz
# Cipher alphabet:   defghijklmnopqrstuvwxyzabc
# Key: 3

def caesarCipher(s: str, k: int) -> str:
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    while k > 0:
        for i, ch in enumerate(s):
            if ch in alphabet:
                if ch == "z":
                    ch = "a"
                elif ch == "Z":
                    ch = "A"
                else:
                    ch = chr(ord(ch) + 1)
                s = s[:i] + ch + s[i + 1:]
        k -= 1
    return s

def caesarCipherFast(s: str, k: int):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i, c in enumerate(alphabet):
        shift = ord(c) + (k % 26)
        if shift > 122:
            shift = shift - 122 + 96
        alphabet[i] = chr(shift)

    for i, c in enumerate(s):
        if c.isalpha():
            if c.isupper():
                s = s[:i] + alphabet[ord(c) - 65].upper() + s[i + 1:]
            else:
                s = s[:i] + alphabet[ord(c) - 97] + s[i + 1:]
    return s

# input
s = "!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U"
k = 62
#print(caesarCipher(s, k))
print(caesarCipherFast(s, k))
