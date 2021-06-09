from pwn import *
import sys
import re


def take_test(p):

    p.recvuntil('')

    # Extract the question/flag
    data = p.recvline().decode().strip().replace(" =", "")
    info('data: %s', data)

    try:
        answer = eval(data)
    except:
        # Flag?
        success("Flag is : %s", data)
        sys.exit(1)
    info('Answer: %s', answer)

    p.sendline(str(int(answer)))


    info('next')


# Connect to SANS server
p = remote('cgames-nm02.allyourbases.co', '9010')
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'info'

# repeat 100 times
for i in range(100):
    take_test(p)