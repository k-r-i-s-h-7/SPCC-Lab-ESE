mnt = {}

mdt = []

print("Enter Macro Definition")

macro = input("Macro Name: ")

params = input("Parameters: ").split(',')

n = int(input("Enter number of lines in macro body: "))

for i in range(n):
    line = input()

    for j in range(len(params)):
        line = line.replace(params[j], "?" + str(j + 1))

    mdt.append(line)

mnt[macro] = 0

print("\nMNT")
print(mnt)

print("\nMDT")

for line in mdt:
    print(line)

print("\nEnter Macro Call")

call = input().split()

actual = call[1].split(',')

print("\nExpanded Code")

for line in mdt:
    temp = line

    for i in range(len(actual)):
        temp = temp.replace("?" + str(i + 1), actual[i])

    print(temp)