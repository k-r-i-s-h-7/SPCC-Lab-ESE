pname = input("Enter program name: ")

start = int(input("Enter starting address in hex: "), 16)

length = int(input("Enter program length in hex: "), 16)

n = int(input("Enter number of symbols: "))

symtab = {}

for i in range(n):
    sym = input("Enter symbol name: ")

    addr = int(input("Enter symbol address in hex: "), 16)

    symtab[sym] = addr

print("\nH RECORD")
print("H^" + pname + "^" +
      format(start, '06X') + "^" +
      format(length, '06X'))

print("\nSYMBOL TABLE")
print("Symbol\tValue")

for sym, addr in symtab.items():
    print(sym, "\t", format(addr, '06X'))

print("\nE RECORD")
print("E^" + format(start, '06X'))