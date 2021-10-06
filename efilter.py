# An Email Filter
# This code is used to filter duplicate emails from an email list provided in a csv file
# The csv file should be in the format such that the emails are in the first column of the sheet
# Every inputed file must have the .csv format
# Feel free to make your own clone of this project and add any cool update of feature you like ;), and also make a request for it to be added to the main
# Feel free to follow me on github if you find this script usefull :)
# The "email2.csv" and "email.csv" files are just example email list that you can use to test this code. note that all emails where gotten from free emails available online.

import csv

emails = []
with open("email2.csv") as f: #you can change this file to your desired file name, make sure the csv file is in the same folder as the python file
    content = csv.reader(f)
    for i in content:
        emails += i

email_list = []
count = 0
duplicate = []
# Filter duplicate emails from email list
print("Filtering duplicate emails from the email list...")
for i in emails:
    if i in email_list:
        count +=1
        duplicate.append(i)  # add the emails that appeared more than once to this list
    else:
        email_list.append(i)  # new list to collect the filtered email list

print("\nHere's the email list\n")
print(email_list)

if count>0:
    print(email_list + " emails where removed because they appeared more than ones\n")
    print(duplicate)
else:
    print("\nThere is no duplicate email in this list\n")

# A functon to export the new list i.e without any duplicate email
def export_file():
    global email_list
    while True:
        name = input("Enter the name you want the file to be(make sure to use the .csv extension): ")
        try:
            with open(name, "w", newline = "") as h:
                handler = csv.writer(h, delimiter=",")
                for i in range(len(email_list)):
                    handler.writerow([email_list[i]])
                print("Your file has been created")
            break
        except:
            print("Enter a proper file name and make sure you use the .csv extension")


x = input("do you want to export the new list to a .csv file?(enter Yes or No) ")
if x.lower() == "yes":
    export_file()
else:
    print("Ok")

# if you want to import another set of emails to add to the previous list
# this second set of emails will be added to the previous list and filtered to get rid of duplicates
new_emails = []
print("\nDo you want to import new emails? \nEnter 'yes' or 'no' ")
q = input("> ").lower()

if q == "yes":
    print("make sure it's a .csv file")
    file = input("enter the name of the file with it's extension: ")
    try:
        with open(file) as g:
            file_content = csv.reader(g)
            for i in file_content:
                new_emails += i 
   
        print("\nHere are the new added emails\n")
        print(new_emails)

        email_list += new_emails

      
        update = []
        # Filter duplicate emails from new email list
        print("\nFiltering duplicate emails from the new email list...")
        for i in email_list:
            if i in update:
                pass
            else:
                update.append(i)

        email_list = update

        print("Here is the full updated list (No repeation of email here)\n")
        print(email_list)

        x = input("\ndo you want to export this second list to a .csv file?(enter Yes or No) ")
        if x.lower() == "yes":
            export_file()
        else: 
            print("Ok, you can go now")
    except:
        print("Enter a proper file name and make sure you use the .csv extension")

else:
    print("Thank you, Have a nice day")
