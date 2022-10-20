# If name is less than 3 characters long
# name must be atleast 3 characters
# otherwise if its more than 50 characters
# name can be maximum of 50 char
# otherwise
# name looks good
#
#
#
name = input("please enter your name: ")

if(len(name)<3):
    print("Name must be atleast 3 characters")
elif(len(name)>50):
    print("Name should not be more than 50 char")
else:
    print("Name looks good")