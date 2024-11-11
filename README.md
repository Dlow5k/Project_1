import csv
open('FullData.csv',newline='') 
cvsfile:
reader= csv.DictReader(csvfile)
for row in reader:
    print(row)
