import csv

with open('test_csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open('test_csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
        print(row['Name'], row['Count'])
