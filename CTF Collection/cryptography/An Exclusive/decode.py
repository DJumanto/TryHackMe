str1 = "44585d6b2368737c65252166234f20626d"
str2 = "1010101010101010101010101010101010"
res = hex(int(str1,16)^int(str2,16))[2:]
print(bytearray.fromhex(res))



