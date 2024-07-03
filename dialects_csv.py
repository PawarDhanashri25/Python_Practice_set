import csv

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')


with open('items.csv', 'r') as csvfile:
    reader=csv.reader(csvfile, dialect='hashes')

    for row in reader:
        print(row) 



with open('items.csv', 'a') as f:
    w=csv.writer(f, dialect='hashes')
    w.writerow(('spoon', 8, 20))
    
    
    
