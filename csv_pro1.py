import csv

people=[['Dan', 34, 'Bucharest'], ['Andrei',21, 'London'], ['Maria', 45, 'Paris']]

with open('people.csv', 'w', newline='') as f:
    w= csv.writer(f)

    csvdata=(['Name', 'Age', 'City'])
    w.writerow(csvdata)
    w.writerows(people)
with open('people.csv', 'r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row) 
    
    
