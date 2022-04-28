file="./myfile2.txt"
with open(file,'a') as my_file:
    my_file.write("this is the first line \n")
    my_file.write("this is the second line \n")
print("file is written and closed")    