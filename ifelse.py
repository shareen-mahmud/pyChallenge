# print("Enter name")
# name = input()
# print("Enter age")
# age = int(input())
# if (age>=18) and (age<30):
#     print("Please Enter")
# else:
#     print ("You do not meet the age requirement")

segment=1
charcount=0
print("Enter an IP address")
add=input()

for i in add:
    if i=='.':
        print("Segment {} contains {} characters".format(segment, charcount))
        segment+=1
        charcount=0
    else:
        charcount+=1
print("Segment {} contains {} characters".format(segment, charcount))