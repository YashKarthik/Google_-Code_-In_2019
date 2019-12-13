import nltk
import re
import textdistance
from operator import itemgetter


def main():
    

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
            else:
                print("Not in dictionary")
            i += 1

    
    # return string  
    str1 = '' 
    checkED = (str1.join(lisL)) 
    print('The corrected string is:  ', checkED)

    #Writing the correct statement to an output file(output.txt)
    file_1 = open("output.txt","a+")#append mode 
    file_1.write(checkED) 
    file_1.close() 

if __name__ == '__main__':
    main()