# with open("binary", 'bw') as binary_file:
#     for i in range(17):
#         binary_file.write(bytes([i]))
#
# with open("binary", 'br') as bin_file:
#     for j in bin_file:
#         print(j)

a = 65534       # FF EE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 00 2D C0 1E

with open("binary2", 'bw') as binw:
    binw.write(a.to_bytes(2, 'big'))
    binw.write(b.to_bytes(2, 'big'))
    binw.write(c.to_bytes(4, 'big'))
    binw.write(x.to_bytes(4, 'big'))
    binw.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as binr:
    e = int.from_bytes(binr.read(2), 'big')
    f = int.from_bytes(binr.read(2), 'big')
    g = int.from_bytes(binr.read(4), 'big')
    h = int.from_bytes(binr.read(4), 'big')
    i = int.from_bytes(binr.read(4), 'big')
    print( e, "\n", f, "\n", g, "\n", h, "\n",i)
