'''
ROT13 Encode algorithms
'''
def rot13_1(message):
    
    d = dict(zip(list(x for x in range(97,123))+list(y for y in range(65,91)), list(x for x in range(110,123))+list(x for x in range(97,110))+list(y for y in range(78,91))+list(y for y in range(65,78))))
    return ''.join(chr(d[ord(i)]) if ord(i) in d.keys() else i for i in message)
def rot13_2(message):
    import codecs
    return codecs.encode(message, 'rot_13')