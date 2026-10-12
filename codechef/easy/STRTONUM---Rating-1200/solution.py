def string_to_number(s):
    num = 0

    for ch in s:
        num = num * 10 + (ord(ch) - ord('0'))

    return num