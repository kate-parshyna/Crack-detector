import csv

def create_table(path):
    with open(path + 'result.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image', 'Rust', 'Crack', 'Nothing'])

def add_to_table(path, filename, rust, crack, nothing):
    fields = [filename, rust, crack, nothing]

    with open(path + r'result.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)