import nltk
import re
import textdistance


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

    i = 0
    while i<20:

        if (textdistance.levenshtein(string_1, string_2)) < 3 :
            lisL.insert(string_2)
            lisL.pop(string_1)
            i += 1

    str1 = " " 
    
    # return string   
    print(str1.join(lisL)) 


if __name__ == '__main__':
    main()