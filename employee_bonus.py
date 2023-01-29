# program that reads the EmployeePay.csv file and prints out details of each employee
# ID,EmpFName,EmpLName,Salary,Bonus


import csv
EMPLOYEE = 'employeepay.csv'

#

infile = open(EMPLOYEE, 'r', newline='')
reader = csv.reader(infile)

#

for row in reader:

    print(row)
