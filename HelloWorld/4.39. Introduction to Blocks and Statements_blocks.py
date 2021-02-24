#   PY doesn't use anything like that, but instead uses indentation to indicate when a new block starts
#   Turning on indentation  -> seting apearence
#   a block of codes cand have other blocks
#   When a line finish with :, PY will expect a new code block to follow it
            #try:
                #bla bla
            #else:
                #bla bla (=> this line is indented)

for i in range (1, 13):
    print("No. {} suared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print("*" * 80) # it is not part of the block, that's why we see it only once

for i in range (1, 13):
    print("No. {} suared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80) # it is not part of the block, that's why we see it only once