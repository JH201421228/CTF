from pwn import *

host = remote('host3.dreamhack.games', 14908)

for i in range(50):
    e = host.recvline(1024)
    n = str(e).split("'")[1][0:-4].split("+")
    host.sendline(str(int(n[0])+int(n[1])))
    
print(host.recv(1024))