import csv

salesfile = open('sales.csv','r')

sales = csv.reader(salesfile, delimiter=',')

#to skip a line if the file contains a header record
next(sales)

cust_total = 0
custID = ''

for record in sales:
    if record[0] != custID:
        if custID:
            print(f"Customer ID: {custID}")
            print(f"Customer total: ${cust_total:,.2f}")
            print()
            print()
        cust_total = 0
        custID = record[0]
        
    subtotal = float(record[3])
    tax = float(record[4])
    freight = float(record[5])
    total = subtotal + tax + freight
    cust_total += total


print(f"Customer ID: {custID}")
print(f"Customer total: ${cust_total:,.2f}")
    

    
    


