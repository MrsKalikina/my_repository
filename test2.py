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

# цикл для проверки победителя

def check_result(s):
    if (bigline[1] == bigline[2] == bigline[3] == s) or \
            (bigline[1] == bigline[5] == bigline[9] == s) or \
            (bigline[1] == bigline[4] == bigline[7] == s) or \
            (bigline[2] == bigline[5] == bigline[8] == s) or \
            (bigline[3] == bigline[6] == bigline[9] == s) or \
            (bigline[4] == bigline[5] == bigline[6] == s) or \
            (bigline[7] == bigline[8] == bigline[9] == s) or \
            (bigline[3] == bigline[5] == bigline[7] == s):
            printbigline()
            print('Поздравляем игрока игравшего {} ! Победа ! Ура Ура Ура!'.format(s))
            quit()
    elif bigline[1] != " " and bigline[1] != " " and bigline[2] != " " and bigline[3] != " " and \
        bigline[4] != " " and bigline[5] != " " and bigline[6] != " " and bigline[7] != " " and \
        bigline[8] != " " and bigline[9] != " ":
            printbigline()
            print('Ничья!')
            quit()
    else:
        print('пока никто не победил, поехали дальше ')

# функция для компа, для проверки выйгрышной строки
def winline(nl, autobot):
    global bigline
    global choosewin
    if (bigline[nl[0]] == autobot and bigline[nl[1]] == autobot and bigline[nl[2]] == " ") or \
            (bigline[nl[0]] == autobot and bigline[nl[2]] == autobot and bigline[nl[1]] == " ") or \
            (bigline[nl[2]] == autobot and bigline[nl[1]] == autobot and bigline[nl[0]] == " "):
        print ('здесь есть линия для победы')
        if (bigline[nl[0]] == autobot and bigline[nl[1]] == autobot and bigline[nl[2]] == " "):
            choosewin = nl[2]
            choosewin = int(choosewin)
            printbigline()

        if (bigline[nl[0]] == autobot and bigline[nl[2]] == autobot and bigline[nl[1]] == " "):
            choosewin = nl[1]
            choosewin = int(choosewin)
            printbigline()

        if (bigline[nl[2]] == autobot and bigline[nl[1]] == autobot and bigline[nl[0]] == " "):
            choosewin = nl[0]
            choosewin = int(choosewin)
            printbigline()


    else:
        print('Строк для победы нет')
        choosewin = None

    return choosewin



def human_win (nl, person):
    global choosewin
    global bigline

    if (bigline[nl[0]] == person and bigline[nl[1]] == person and bigline[nl[2]] == " ") or \
            (bigline[nl[0]] == person and bigline[nl[2]] == person and bigline[nl[1]] == " ") or \
            (bigline[nl[2]] == person and bigline[nl[1]] == person and bigline[nl[0]] == " "):
        print ('ОПАСНОСТЬ! ЧЕЛОВЕК МОЖЕТ ПОБЕДИТЬ!')
        if (bigline[nl[0]] == person and bigline[nl[1]] == person and bigline[nl[2]] == " "):
            choosewin = nl[2]
            printbigline()

        if (bigline[nl[0]] == person and bigline[nl[2]] == person and bigline[nl[1]] == " "):
            choosewin = nl[1]
            printbigline()

        if (bigline[nl[2]] == person and bigline[nl[1]] == person and bigline[nl[0]] == " "):
            choosewin = nl[0]
            printbigline()

    else:
        print('линий для победы человека нет, можно ходить куда угодно')
        choosewin = None
        printbigline()

    return choosewin

def get_pos_auto (person,symbol):
    global bigline
    global choosewin
    cell_is_occupied = True
    while cell_is_occupied:

        choosewin = random.randint(1, 9)

        if bigline[choosewin] != " ":
            print(' Данная ячейка занята!')
        else:
            cell_is_occupied = False
            break
    return choosewin



#Здесь уже должен был цикл для игры, в котором цикл для проверки ходов робота.

going = True

while going:

    printbigline()
    bigline[get_pos('Первый','X')] = "X"

    check_result("X")
    check_result("O")

    printbigline()


    for line in all_lines:
        winline(line, 'O')
        if choosewin != None:
            bigline[choosewin] = "O"
        else:
            human_win(line, 'X')
            if choosewin != None:
                bigline[choosewin] = "O"
            else:
                bigline[get_pos_auto('Второй','O')] = "O"

    printbigline()

    check_result("X")
    check_result("O")

