import csv
import datetime
currentDate = datetime.datetime.now()

filename = 'csv_birthdaywisher.csv'
row = []
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    fields = next(csv_reader)
    for row in csv_reader:
        if (row != []):
            names = row[0]
            date = row[1]

            date2 = datetime.datetime.strptime(date, '%d/%m/%Y')

            if currentDate.day == date2.day and currentDate.month == date2.month:
                print("Happy Birthday", row[0], "!!!")