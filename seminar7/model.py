
def search_data(base, record):

    base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if record in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'Контакт {record} не найден!')
    return results