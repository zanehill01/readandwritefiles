# program that reads the sales.csv file and creates a new files with the customer ID and calculated total.
# CustomerID,OrderDate,ShipDate,SubTotal,TaxAmt,Freight

import csv
SALES = 'sales.csv'
SALES_REPORT = 'salesreport.csv'

# create read and write objects

infile = open(SALES, 'r', newline='')
reader = csv.reader(infile)
next(reader)

outfile = open(SALES_REPORT, 'w', newline='')
writer = csv.writer(outfile, delimiter=',')

# create list for id's and final subtotals

id_subtotal = []

# iterate through sales.csv

for row in reader:

    # calculate subtotals and identify customer id's

    subtotal = float(row[3]) + float(row[4]) + float(row[5])
    cust_id = row[0]
    found = False

    # create a list of id numbers and subtotals added from corresponding id's
    # this for loop updates the subtotal in the list by finding existing id's and adding their totals to the lists index

    for index in id_subtotal:
        if index[0] == cust_id:
            index[1] += subtotal
            found = True

    # adds [205, 1043.53] initially, then asks (for sale in id_subtotal) to complete the total and move to the next in sales.csv
    # adds initial value to the list, to be questioned then updated*

    if not found:
        id_subtotal.append([cust_id, subtotal])

# write values into .csv, formatted

writer.writerow(['Customer | Total'])

for cust_id, index in id_subtotal:
    writer.writerow([cust_id, format(index, '>12.2f')])
