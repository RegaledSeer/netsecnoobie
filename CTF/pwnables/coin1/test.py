from pwn import *
import re

def get_weight(start,end,r):
    send_str = ""
    if start == end:
        r.sendline(str(start))
    else:
        for i in range(start,end + 1 ):
            send_str = send_str + str(i)+" "
        r.sendline(send_str)
    result = r.recvline()
    return int(result)

def choose_coin(num,chance,r):
    start = 0
    end = num -1
    weight = 0
    for i in range(0,chance  ):
        weight = get_weight(start,int(start+(end-start)/2),r)
        if weight%10 != 0:
            end = int(start+(end-start)/2)
        else:
            start = int(start+(end-start)/2 )+1
    r.sendline(str(end))
    print '[+]server: ',r.recvline()

r = remote('127.0.0.1',9007)
print r.recv()

for i in range(0,100):
    print '[*]','='*18," ",i," ","="*18 ,"[*]"
    recvword = r.recvline()
    print "[+]server: ",recvword
    p = re.compile(r'\d+')
    data = p.findall(recvword)
    num = int(data[0])
    chance = int(data[1])
    choose_coin(num,chance,r)
print r.recv()
