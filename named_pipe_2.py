import time
import struct

f = open(r'\\.\pipe\COM1', 'ab', 0)
i = 1

# 20.10
twenty = b'\x02\x34\x20\x22\x20\x20\x32\x30\x31\x30\x20\x20\x20\x30\x30\x30\x0d\x1b'
# 41.04
fourty = b'\x02\x34\x20\x22\x20\x20\x34\x31\x30\x34\x20\x20\x20\x30\x30\x30\x0d\x1b'

send = twenty

while True:
    s = 'Message[{0}]'.format(i)
    i += 1

    if (i % 20) == 0:
        if (send == twenty):
            print("Switching to Fourty")
            send = fourty
        else:
            print("Switching to Twenty")
            send = twenty

    bytes_written = f.write(send)   # Write str length and str
    print("Bytes " + str(send))
    f.seek(0)                               # EDIT: This is also necessary
    print('Wrote:', s)

    # n = struct.unpack('I', f.read(4))[0]    # Read str length
    # s = f.read(n)                           # Read str
    # f.seek(0)                               # Important!!!
    # print('Read:', s)

    time.sleep(0.1)
