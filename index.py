import csv

with open("Salary_dataset.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
