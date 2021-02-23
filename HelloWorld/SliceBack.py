#          012345678901234567890123456
#         654321098765432109876543210
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]    #Nu o sa returneze (mergem cu stepul de -1, de la 25 la 0 not included
print(backwards)

backwards = letters[25:-1:-1]    #Nu o sa returneze nimic(negative stop value count backwords from the end of the sequence,
                                # -1 means the last character in the string, ii ca si cum vrem sa mergem pana la z der Z ii not included
                                #dinasta nu o sa apara mimic
print(backwards)

backwards = letters[25::-1]    #returneaza, nu avem un stop value si atunci trece prin toate
print(backwards)


backwards1 = letters[16:13:-1]    #returneze
print(backwards1)

backwards2 = letters[4::-1]
print(backwards2)

backwards3 = letters[25:17:-1]
print(backwards3)

backwards3 = letters[:-9:-1]
print(backwards3)

#
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])