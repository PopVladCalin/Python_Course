#         012345678901234
parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])    # print the char from position 3 (starting with 0)
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print(parrot[-1])
print(parrot[-14])

print(parrot[-11])    # print the char from position 3 (starting with 0)
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print(parrot[3 - 14])    # print the char from position 3 (starting with 0)
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print(parrot[0:6])  # up  to 6 but not included Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

print(parrot[-4:-2])     #bl   de la b la u -2 dar u not included
print(parrot[-4:12])     #bl de la b pana la u 12 dar not included

print(parrot[0:6:2])    # nre - merge de la 0 la 6 (not included) cu pas de 2
print(parrot[0:6:3])    # nr - merge de la 0 la 6 (not included) cu pas de 3

number = "9,223;372:036 854,775;807"
print(number[1::4])

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])