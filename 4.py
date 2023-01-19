def encode_rle(s: str) -> str:
    count = 1
    rle = ''
    prev = ''
    for i in s:
        if prev == '':
            prev = i
            continue
        if i == prev:
            count += 1
        else:
            rle = rle + str(count) + prev
            count = 1
            prev = i
    return rle + str(count) + prev


def decode_rle(encode_str):
    decode_str = ''
    for i in range(1, len(encode_str), 2):
        decode_str = decode_str + encode_str[i] * int(encode_str[i - 1])
    return decode_str


if __name__ == '__main__':
    raw_str = 'aaabbb1111ccc   ddraaaddaa'
    encode_str = encode_rle(raw_str)
    print(f'{raw_str} - изначальная строка')
    print(f'{encode_str} - закодированная строка ')
    print(f'{decode_rle(encode_str)} - раскодированная строка')
