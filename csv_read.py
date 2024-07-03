import csv

#Read the csv file content 
'''
with open('data.csv', 'r') as f:
    content=csv.reader(f)
    next(content)    # skipt the first line i.e. header
    year_1958=dict()
    
    for row in content:
        #print(row)
        year_1958[row[0]]=row[1]
    
    print(year_1958)

    max_1958=max(year_1958.values())
    print(max_1958)

'''
# read the csv file using the deliminator like(:)
'''
with open ('passwd', 'r') as f:
    reader=csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)
'''
# write the data to csv file
'''
with open('data.csv', 'a') as f:
    w=csv.writer(f)
    csv_data= ('SEP', 230, 450, 240)
    w.writerow(csv_data)
    
'''
#creating and writing the data to the file

with open('numbers.csv', 'w', newline='') as f:
    w=csv.writer(f)
    w.writerow(['x', 'x**2' , 'x**3', 'x**4'])
    for x in range(1, 10):
        w.writerow([x, x**2, x**3, x**4])



