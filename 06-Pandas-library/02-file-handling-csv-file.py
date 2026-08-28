import csv
filename = "06-Pandas-library\employees.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile :
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % csvreader.line_num)

print('Filed names are: '+' , '.join(fields))

print('\nFirst 5 rows are: \n')
for rows in rows[:5]:
    for col in row:
        print("%10s" % col, end=" ")

    print('\n')