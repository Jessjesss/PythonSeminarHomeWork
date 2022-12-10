# 2. Создайте программу для игры в ""Крестики-нолики"".
# (в консоли происходит выбор позиции)

field = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Показать ячейки
def show_field():
    global field
    for i in range(0, len(field), 3):
        print(field[i], field[i+1], field[i+2])

# Сделать ход в ячейку
def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol
 
# Получить текущий результат игры
def result():
    win = ""
    for i in victories:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "Человек!"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "Компьютер!"
    return win
 
# Поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):
    step = ""
    for line in victories:
        o = 0
        x = 0
        for j in range(0, 3):
            if field[line[j]] == "O":
                o = o + 1
            if field[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if field[line[j]] != "O" and field[line[j]] != "X":
                    step = field[line[j]]          
    return step
 
# Выбор хода компьютера
def choice_step():        
    step = ""
    step = check_line(2, 0)
    if step == "":
        step = check_line(0, 2)        
    if step == "":
        step = check_line(1, 0)           
    if step == "":
        if field[4] != "X" and field[4] != "O":
            step = 5           
    if step == "":
        if field[0] != "X" and field[0] != "O":
            step = 1           
    return step

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

game_over = False
human = True

while game_over == False:
    show_field()
    if human == True:
        symbol = "X"
        step = int(input("Ходит человек: "))
    else:
        print("Ходит компьютер: ")
        symbol = "O"
        step = choice_step()
    if step != "":
        step_field(step, symbol) # делаем ход в указанную ячейку
        win = result() # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        game_over = True
        win = 'Ничья!'
    human = not(human)        
 
# Конец игры       
show_field()
print("Победитель:", win)