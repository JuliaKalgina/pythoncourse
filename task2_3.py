import csv
with open('task_3.csv', 'w', encoding='utf-8') as ff:
    with open('stage3_test.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(ff, fieldnames=["Title", "Id", "Price"], lineterminator="\r")
        writer.writeheader()
        for row in reader:
            writer.writerow({"Title": row["Title"], "Id": row["Id"], "Price": row["Price"]})
