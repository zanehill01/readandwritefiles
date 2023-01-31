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

# iterate through sales.csv

id_subtotal = []

for row in reader:

    # calculate subtotals and identify customer id's

    subtotal = float(row[3]) + float(row[4]) + float(row[5])
    cust_id = row[0]
    found = False

    # adds subtotal if id is found within [totals]

    for sale in id_subtotal:
        if sale[0] == cust_id:
            sale[1] += subtotal
            found = True

    # fills [totals], storing id's and calculated subtotals

    if not found:
        id_subtotal.append([cust_id, subtotal])

# write values into csv, formatted

writer.writerow(['Customer | Total'])

for cust_id, sale in id_subtotal:
    writer.writerow([cust_id, format(sale, '>12.2f')])
