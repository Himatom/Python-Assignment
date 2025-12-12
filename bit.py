val = 0xCAFE

last4 = val & 0xF
at_least_three = bin(last4).count("1") >= 3

reversed_bytes = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)

rotated = (val >> 4) | ((val & 0xF) << 12)

print(at_least_three)
print(hex(reversed_bytes))
print(hex(rotated))