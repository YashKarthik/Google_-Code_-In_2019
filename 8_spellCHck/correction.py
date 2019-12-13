from spellchecker import SpellChecker

spell = SpellChecker()

dicL = [line.rstrip('\n') for line in open('dict.txt')]
print("The dictionary specified is: ", dicL)
file = open('check_them.txt', 'r')
speL = list()
speL = list(file.read().split())

# find those wrongs that may be misspelled
misspelled = spell.unknown(speL)

#def var for the following loop
i = 0
l = len(speL)

for wrong in misspelled:
    correct = (spell.correction(wrong))

    #Check if correction is in dict 
    if correct in dicL:
        print("Correction of ", wrong, " is: "  , correct)
    else:
        print(wrong, "+++++++NOT IN DICTIONARY+++++++")
    i += 1

    #Insert the correction at the place of the wrong one
    inde = speL.index(wrong)                             
    speL.remove(wrong)
    speL.insert(inde, correct)

#Convert the list with corrections into str
listToStr = ' '.join([str(elem) for elem in speL]) 
f = open('output.txt', 'w+')
f.write(listToStr)
print("--------------------------    Check your 'output.txt' file for the full para/sentence   -----------------------------")
  