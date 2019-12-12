import zipfile 
 
filename = 'uncracked.zip' 
dictionary = 'PassW.txt.txt' 
 
password = None 
file_to_open = zipfile.ZipFile(filename) 
with open(dictionary, 'r') as f:
    for line in f.readlines():
        password = line.strip('\n')
        try:            
            globals
            file_to_open.extractall(pwd=password) 
            passwor = 'Password found: %s' % password 
            print(passwor) 
        except: 
            print("Failed, checking next")