import random


print('Привет!'"\n"
      'Это игра в крестики-нолики для 2х игроков.')
#person_sigh = input('Пожалуйста, введите каким символом вы будете ходить, O или X:',)

bigline = [" " for x in range(10)]


def printbigline():
    print("\n")
    print("┏━━━┳━━━┳━━━┓")
    print("┃1  ┃2  ┃3  ┃")
    print("┃ " + bigline[1] + " ┃ " + bigline[2] + " ┃ " + bigline[3] + " ┃")
    print("┃   ┃   ┃   ┃")
    print("┃━━━╋━━━╋━━━┫")
    print("┃4  ┃5  ┃6  ┃")
    print("┃ " + bigline[4] + " ┃ " + bigline[5] + " ┃ " + bigline[6] + " ┃")
    print("┃   ┃   ┃   ┃")
    print("┣━━━╋━━━╋━━━┫")
    print("┃7  ┃8  ┃9  ┃")
    print("┃ " + bigline[7] + " ┃ " + bigline[8] + " ┃ " + bigline[9] + " ┃")
    print("┃   ┃   ┃   ┃")
    print("┗━━━┻━━━┻━━━┛")
    print("\n")


n0 = (1,2,3)
n1 = (1,5,9)
n2 = (1,4,7)
n3 = (2,5,8)
n4 = (3,6,9)
n5 = (4,5,6)
n6 = (7,8,9)
n7 = (3,5,7)

all_lines = [n0, n1, n2, n3, n4, n5, n6, n7]

# функция для человека
def get_pos(person,symbol):
    global bigline
    global choosewin
    cell_is_occupied = True
    while cell_is_occupied:

        choosewin = input(
                '{} игрок, введите целое число ячейки от 1-9, в какую ставить {}:'.format(person, symbol)
            )
        while type(choosewin) != int:
            try:
                choosewin = int(choosewin)
            except:
                print("Неправильно ввели!")
                choosewin = int(input("Введите целое число от 1 до 9: "))
        if bigline[choosewin] != " ":
            print(' Данная ячейка занята!')
        else:
            cell_is_occupied = False
            break
    return choosewin

# функция для упрощения всех проверок и победиля и нужной клетки для робота. здесь мы собираем списки
# с данными - в каких клетках уже стоит знак нолика или крестика, а какие клетки пустые.

#bigline[9] = "X"
#bigline[7] = "O"

def get_cells_info(line_number, our_sign, enemy_sign):
    global all_lines
    global enemy_cells
    global empty_cells
    global our_cells

    nl = all_lines[line_number]
    print(nl)
    empty_cells = []
    our_cells = []
    enemy_cells = []
    for pos in range(3):
        if bigline[nl[pos]] == " ":
            empty_cells.append(nl[pos])
        if bigline[nl[pos]] == our_sign:
            our_cells.append(nl[pos])
        if bigline[nl[pos]] == enemy_sign:
            enemy_cells.append(nl[pos])
    print (enemy_cells, our_cells, empty_cells)
    return enemy_cells, our_cells, empty_cells



def winner_check():
    global all_lines
    x = 0 #  та самая ошибка
    for i in range(8):
#        print('сейчас мы смотрим строку', i)
        get_cells_info(i, "O", "X")
#        print(enemy_cells, '-это вражеские ячейки', our_cells, '- это наши ячейки', empty_cells, '-пустые ячейки')
        if len(our_cells) == 3:
            print('ура, вновь роботы одержали вверх над человечеством')
            quit()
        if len(enemy_cells) == 3:
            print('Ураааа вновь человечество победило над роботами')
            quit()
        if len(empty_cells) == 0:
            x=x+1
            if x == 8:
                print ('НИЧЬЯ! Сегодня силы распределились в равной степени. Никто не сможет смеяться последним')
                quit()
            else:
                continue
        else:
            print('видимо тут нет победных строк - будем играть дальше')


def sear_number_for_step():
    global all_lines
    global number_for_win

    for i in range(8):
        print('сейчас мы смотрим строку', i)
        get_cells_info(i, "O", "X")
        print(enemy_cells, '-это вражеские ячейки', our_cells, '- это наши ячейки', empty_cells,
                      '-пустые ячейки')

        if len(our_cells) == 2 and len(empty_cells) == 1:
            print('круто, у нас есть шанс победить человечество, достаточно всего лишь поставить свой знак в', empty_cells[0])
            number_for_win = int(empty_cells[0])
            print(number_for_win)
            break

        if len(empty_cells) == 1 and len(enemy_cells) == 2:
            print('алярм, человек шибко умён и уже поставил в одну строку два своих символа')
            print('надо ставить свой роботовский значёк ', empty_cells[0])
            number_for_win = int(empty_cells[0])
            print(number_for_win)
            break

        if len(our_cells) == 1 and len(empty_cells) == 2:
            print('такс, линии для победы нет, опасных линий тоже нет, но есть линия где у меня есть возможность '
                  'создать себе победную комбинаци.',empty_cells[0])
            number_for_win = int(random.choice(empty_cells))
            print(number_for_win)
            break
        if len(empty_cells) == 3:
            number_for_win = int(random.choice(empty_cells))
            print(number_for_win)
            break

    return number_for_win
    print(number_for_win)



going = True

while going:
    printbigline()
    bigline[get_pos('Первый','X')] = "X"
    printbigline()
    winner_check()
    sear_number_for_step()
    bigline[number_for_win] = "O"
    printbigline()
    winner_check()
