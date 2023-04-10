"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then 
sent over the network and is decoded back to the original list of strings.
"""
def encode(strs):
    encoded = ""
    for s in strs:
        if s != strs[-1]:
            encoded += s + ":;"
        else:
            encoded += s
    return decode(encoded)

def decode(str):
    array = []
    word = ""
    for c in str:
        if c != ':':
            if c != ';':
                word += c
            if c == ';':
                array.append(word)
                word = ""
    array.append(word)
    return array

strs = ["boss", "bitch"]
print(encode(strs))