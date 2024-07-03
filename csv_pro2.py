import csv

people=[['Dan', 34, 'Bucharest'], ['Andrei',21, 'London'], ['Maria', 45, 'Paris']]

with open('people2.csv', 'w', newline='') as f:
    w= csv.writer(f, delimiter=':')

    csvdata=(['Name', 'Age', 'City'])
    w.writerow(csvdata)
    w.writerows(people)
with open('people2.csv', 'r') as f:
    reader=csv.reader(f, delimiter=':')
    for row in reader:
        print(row) 
    
    
