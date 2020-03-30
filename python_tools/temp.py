def increment_string(strng):
    for i in range(len(strng)):
        if strng[-i] not in list(str(x) for x in range(10)):
            break
    if set(strng).intersection(set(str(x) for x in range(10))):
        return strng[:-i+1]+str(int(strng[-i+1:])+1).zfill(i-1)
    else:
        return strng + "1"


def rot13(message):
    d = dict(zip(list(x for x in range(97,123))+list(y for y in range(65,91)), list(x for x in range(110,123))+list(x for x in range(97,110))+list(y for y in range(78,91))+list(y for y in range(65,78))))
    return ''.join(chr(d[ord(i)]) if ord(i) in d.keys() else i for i in message)


def sum_pairs(ints, s):
    for x in range(len(ints)):
        for y in range(x):
            if ints[x]+ints[y] == s:
                return [ints[x], ints[y]]
    return None