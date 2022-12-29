import csv


def get_data():
    with open('seminar7/base.csv', 'r', encoding='utf-8') as f:
        reader = f.read()
        return reader
       
       
def rec_data(record: list):
    with open('seminar7/base.csv', 'a', encoding='utf-8') as f:
        f_writer = csv.writer(f, delimiter=';', lineterminator= '\n')
        return f_writer.writerow([record])


