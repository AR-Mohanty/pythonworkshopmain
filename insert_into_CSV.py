# Python program to demonstrate
# writing to CSV


import csv

# field names
# fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = []

# name of csv file
filename = "university_records.csv"

# writing to csv file
# with open(filename, 'a') as file:
#     # creating a csv writer object
#     csvwriter = csv.writer(file)
#     # writing the fields
#     # csvwriter.writerow(fields)
#
#     choice = 'yes'
#
#     while choice == 'yes':
#         stu_name = input("Enter name")
#         stu_branch = input("Enter student branch")
#         stu_year = input("Enter addmission year")
#         stu_CGPA = input("Enter your CGPA")
#         # writing the data rows
#         rows = [[stu_name,stu_branch,stu_year,stu_CGPA]]
#         csvwriter.writerows(rows)
#
#         print("One row is inserted")
#         choice = input("If you want to continue press yes otherwise no").lower()

print("Thanks for using our programe")
output = input("Want output of csv file [yes/no]:").lower()
if output == 'yes':
    with open('university_records.csv') as csv_file:
        data = csv.reader(csv_file)
        for rows in data:
            if rows != []:
                print(rows[1])
