from name_function import get_formatted_name

print("please hit q to break!\n")

while True:
    first=input("enter te first name:")
    if first=='q':
        break
    last=input("enter the last name:")
    if last=='q':
        break
    print("formatted name:",get_formatted_name(first,last))


