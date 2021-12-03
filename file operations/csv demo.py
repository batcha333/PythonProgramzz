import csv
with open('demo.csv') as g:
    g_csv = csv.reader(g)
headers = next(g_csv)
for row in g:
    print(row)