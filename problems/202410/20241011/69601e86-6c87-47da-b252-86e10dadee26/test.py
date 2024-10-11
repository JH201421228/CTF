from pwn import *

# 지정 호스트의 지정 포트로 원격 접속
r = remote("host3.dreamhack.games", 9925)

# 서버에서 rand 값 받기
r.recvuntil(b"number: ")
rand = r.recvn(10)

print("rand : ", rand)

# 16진수로 변환한 후 XOR 연산
x = int(rand, 16) ^ 0x7d1c4b0a
# 문자열로 변환 후 바이트 형식으로 인코딩
x = str(x).encode()

# Input?이란 문자열이 나올 때 값을 전송
r.sendlineafter(b"Input? ", x)
print(x)

# 프로그램 제어(입출력 등)를 사용자에게 넘김
r.interactive()