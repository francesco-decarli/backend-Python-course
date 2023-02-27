# Strings => NB: it's case sensitive!!
name = "Francesco"
print("First 'a' in Francesco is in [array] position: ", name.index("a"))

# Numbers
print("To get the remainder use \%. 7\%3 =", str(7%3))
print("In order to get the BINARY number of a number, use 'bin(number)'. Binary of 7 is", bin(7))

# Functions
## in order to pass an unknown amount of inputs, use '*' before the parameter definition
def greetings(*names):
    print("Welcome", names[1])

greetings("Francesco", "Giulio", "Tiziano", "Marcos")