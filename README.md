import csv
open('"C:\Users\N1311381\Downloads\FullData.csv"'') 

reader= csv.DictReader(csvfile)
for row in reader:
    print(row)
