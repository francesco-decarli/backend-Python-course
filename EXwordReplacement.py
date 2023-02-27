loop = True

print("Hello, this is a simple script which gives you the possibility to replace a word (or more) in a sentence you'll give as input.")
sentence = input("Write your sentence, please: ")
print("Thank you, now that I've stored it you can replace whatever you want of your sentence with whatever else you want.\n",
    "I'll keep running until you'll say to me to stop. As a matter of fact I'll, keep asking you if you want to stop after every replacement.")
while loop != False:
    print("Current sentence:", sentence)
    toRep = input("It has to perfectly match in order to do it. So, what do you want to replace in your sentence? ")
    rep = input("With what do you want to replace it? Write it, please: ")
    print("Replacing...")
    sentence = sentence.replace(toRep, rep)
    print("Here your new string: ", sentence)
    check = input("Do you want to replace something else? Type 'yes' or 'no'\n")
    if check != "no" and check != "yes":
       print("Sorry, I couldn't comprehend the answer you gave me. Now Exiting the script.")
       break
    elif check == "no":
        loop = False
    else:
        print("Okay, let's keep going, then.")
print("See you!\nFin")