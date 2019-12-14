file_to_crack = input("Which file to crack?   1)1stcrackme, 2)2ndcrackme, 3)3rdcrackme, enter file name:  ")
   
with open(file_to_crack, "rb") as file:
    data = file.read(8)

with open("out_passW.txt", "a+") as f:
    f.write('Password extracted from ' + file_to_crack + ' is: ')
    f.write(''.join(map(str, data)))
    f.write("\n")
    print("---------------Check your output file for the password ---------------")

