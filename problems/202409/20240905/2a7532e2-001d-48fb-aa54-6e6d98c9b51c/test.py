# 복호화할 encfile 파일을 읽습니다.
with open('encfile', 'r', encoding='utf-8') as f:
    enc_str = f.read()

# 00부터 FF까지의 16진수 리스트를 다시 생성합니다.
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

# 암호화된 문자열을 두 글자씩 잘라서 복호화 리스트를 만듭니다.
enc_list = [enc_str[i:i+2] for i in range(0, len(enc_str), 2)]

# 복호화된 데이터를 저장할 리스트를 생성합니다.
plain_list = list(range(len(enc_list)))

# 암호화된 데이터를 순차적으로 복호화합니다.
for i in range(len(enc_list)):
    hex_b = enc_list[i]
    index = hex_list.index(hex_b)
    # 복호화: 128을 빼고 다시 리스트 순환
    plain_list[i] = hex_list[(index - 128) % len(hex_list)]

# 복호화된 16진수 문자열을 다시 바이트로 변환합니다.
plain_bytes = bytes([int(hex_b, 16) for hex_b in plain_list])

# 복호화된 데이터를 원래 파일로 저장합니다.
with open('dec_flag.png', 'wb') as f:
    f.write(plain_bytes)

print("복호화 완료: dec_flag.png 파일로 저장되었습니다.")
