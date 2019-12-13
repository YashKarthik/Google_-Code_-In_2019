import nltk
import re
import textdistance
from operator import itemgetter

class SpellCheakr:
    def __init__(self, english, dicL, wrong, convr, lisL, m, i, l, str1, checkED, file_1, string_1, string_2 ):
        self.english = english
        self.dicL = dicL
        self.wrong = wrong
        self.convr = convr
        self.lisL = lisL
        self.m = m
        self.i = i
        self.l = l
        self.str1 = str1
        self.checkED = checkED
        self.file_1 = file_1
        self.string_1 = string_1
        self.string_2 = string_2


    def main(self):
        with open("dict.txt", "r") as f:
            english = {word.strip() for word in f}
            dicL = [line.rstrip('\n') for line in open('dict.txt')]
        with open("checkthem.txt", "r") as f:
            wrong = (x.strip() for x in f if x.strip() not in english)
            for key, word in enumerate(wrong):
                convr = ("{}: {}\n".format(key, word))
                print(convr)
                lisL = (convr.split()) 
                print("List of the words in file provided: ", lisL)
                print("The list of words in the dictionary:", dicL)

    def logic(self):
        m = 0                       #For string_1
        i = 0                    #For string_2
        l = len(lisL)

        while m != l:
            i = 0
            while i!= 20:
                string_1 = itemgetter(m)(lisL)
                string_2 = itemgetter(i)(dicL)
                if (textdistance.levenshtein(string_1, string_2)) < 3 :
                    lisL.remove(string_1)
                    lisL.insert(m, string_2)
                    print("----------------------->")
                else:
                    print("Checking......")
                i += 1

    
    def print_2_File(self):
                                                # return string  
        str1 = '' 
        checkED = (str1.join(lisL)) 
        print('The corrected string is:  ', checkED)

        #Writing the correct statement to an output file(output.txt)
        file_1 = open("output.txt","a+")#append mode 
        file_1.write(checkED) 
        file_1.close() 

    main(self=None)
    