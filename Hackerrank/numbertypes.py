n = int(input())
l1 = len(bin(n)[2:])
for i in range(1, n+1):
    print(str(i).rjust(l1, ' '), end=' ')
    print(oct(i).lstrip('0o').rjust(l1, ' '), end=' ')
    print(hex(i).lstrip('0x').rjust(l1, ' ').upper(), end=' ')
    print(bin(i).lstrip('0b').rjust(l1, ' '), end=' ')
    print('')