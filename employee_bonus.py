# program that reads the EmployeePay.csv file and prints out details of each employee
# ID,EmpFName,EmpLName,Salary,Bonus

import csv
EMPLOYEE = 'employeepay.csv'

#

infile = open(EMPLOYEE, 'r', newline='')
reader = csv.reader(infile)
next(reader)

#

for row in reader:

    bonus = int(row[3]) * float(row[4])
    total = bonus + int(row[3])

    print('ID EmpFName     EmpLName     Salary     Bonus     Total Pay')
    print('-- ------------ ------------ ---------- --------- ---------')

    print(format(row[0], '<2'), format(row[1], '<12'), format(row[2], '<12'),
          format(row[3], '<10'), format(row[4], '<9'), format(total, '.2f'))

    input('\nPress ENTER for next employee...\n')
