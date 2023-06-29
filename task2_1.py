import csv
with open('stage3_test.csv', 'r', encoding='utf-8') as st:
    reader = csv.DictReader(st)
    data = []
    for row in reader:
        rows = row['Images']
        if len(rows.split(',')) > 3:
            data.append(row)
with open('task2_1.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames, lineterminator="\r")
    writer.writerows(data)