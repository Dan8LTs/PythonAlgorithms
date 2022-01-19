# binary: 0bnumber; bin(number)
x = 0b1101
# octal:   0onumber; oct(number)
y = 0o0732
# hexadecimal: 0xnumber; hex(number)
z = 0xFA0B
print(z)
print(hex(z))

t = int('423F', base = 36)
print(t)


# according to Horner's scheme
base = 7
x = int(input())
d = []
while x > 0:
	digit = x % base 
	d.append(digit)
	x //= base
d.reverse()
for i in d:
	print(i, end="")

