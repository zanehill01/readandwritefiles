# program that reads the file customers.csv and produces a new file containing the customer and country they are from. (customer_country.csv)
# ID,FirstName,LastName,City,Country,Phone

import csv
CUSTOMER = 'customers.csv'
CUSTOMER_COUNTRY = 'customer_country.csv'

#

infile = open(CUSTOMER, 'r', newline='')
reader = csv.reader(infile)
next(reader)

outfile = open(CUSTOMER_COUNTRY, 'w', newline='')
writer = csv.writer(outfile, delimiter=',')

#

for row in reader:

    customers = [row[1], row[2], row[4]]
    writer.writerow(customers)
