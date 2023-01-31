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

    print([row, 'TOTAL PAY -> ', format(total, '.2f')])
    input('Press ENTER for next employee...')
