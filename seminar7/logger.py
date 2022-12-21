import csv


def get_data():
    with open('seminar7\base.csv', 'r', encoding='utf-8') as f:
        return f.read()
       
       
def rec_data():
    with open('seminar7\base.csv', 'w', encoding='utf-8') as f:
        return f.write()

# def creating():
#     file = 'base.csv'
#     with open (file, 'w', encoding = 'utf-8') as f:
#         f.write(f'Фамилия;Номер телефона;\n')