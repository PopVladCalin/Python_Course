# testing several conditions usig elif


name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name))) # only integers can be tasted, for ex. Twenty will raise an error
print (age)

# if age >= 18: #condition
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18: #condition
    print("Please come back in {0} years".format(18 - age))
elif age==900:
    print("Sorry....died")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")