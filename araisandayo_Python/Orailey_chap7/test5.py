import binascii
hex_str = '4749463839610100010080000000000fffff21f9' + \
    '04010000000002c0000000001000100000020144003b'

gif = binascii.unhexlify(hex_str)
print(len(gif))

print(gif[:6] == b'GIF89a')

import struct

width, height = struct.unpack('<HH', gif[6:10])
print(width, height)