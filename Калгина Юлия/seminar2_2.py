import csv
i = 0
with open('stage3_test.csv', 'r') as csv_f:
    csv_reader = csv.DictReader(csv_f, delimiter=',')
    with open('newww.csv', 'w') as output_file:
        csv_writer = csv.DictWriter(output_file, delimiter=',', fieldnames=csv_reader.fieldnames)
    csv_writer.writeheader()

for row in csv_reader:
    i += 1

price = float(row['Price'])
if price > 10000:
    if price < 50000:
        csv_writer.writerow(row)
    else:
        pass