print('''
`````(_\````/_)
```````))``((
`````.-"""""""-.``
`/^\/``_.```_.``\/^\\
`\(```/__\`/__\```)/        <------ "Здравствуй Землянин, я представитель расы Оликов, и мне нужна твоя помощь.
``\,``\o_/_\o_/``,/                 Однажды в межгалактическом баре я играл в игру с другим представителем космической расы - Иксиком
````\````(_)````/                   В игру под названием "Иксики против Оликов" и к моему сожалению проиграл ему.
``````-.'==='.-'                    Теперь Иксик меня преследует, помоги мне победить его, и может быть тогда он от меня отстанет!
``````__)`-`(__
`````/```~~~```\\
````/``/`````\``\\
````\`:```````;`/
`````\|==(*)==|/
``````:```````:
```````\``|``/
`````___)=|=(___
````{____/`\____}''')  # до 48 строки кода представление игры
space_string = input('Нажмите на Enter, чтобы продолжить')
print('''~~~~~~~~~~~~\nДобро пожаловать в игру "Иксики и Олики"
Вы уже слышали о ней, только под другим названием ("Крестики и Нолики")
Правила игры простые, но их надо соблюдать:
1. Первые ходят Иксики (x), так как Олики очень мирная раса, они защищаются, а Иксики нападают;
2. Дважды ходить Иксиками или Оликами запрещается;
3. В игре есть только Иксики (х) и Олики (о) и никого другого;
4. Если введена не правильная координата игра заканчивается и проигравшим является тот, кто ввёл не правильную координату, будьте внимательны;
5. Побеждает тот, кто соберет 3 в ряд одинаковых представителей рас.
В случае если один из игроков нарушит правила, игрок, нарушивший правила проигрывает''')
space_string = input('Нажмите на Enter, чтобы продолжить')
print('''~~~~~~~~~~~~\nПример ввода в игре "Иксики и Олики":
Вам дано поле, цифры по вертикали: от 1 до 3. Цифры по горизонтали: от 0 до 2.
Символы "-" - означают, что это пустое поле.
По вертикали и горизонтали цифры, указывающие на координаты поля, ввод координат осуществляется так: 1-0 или 1-1 и так далее.
  0 1 2
1 - - -
2 - - -
3 - - -
Далее вас просят: 
Выберите сторону Иксиков или Оликов
Ваш выбор упал на - {сюда вводить или х или о (Ввод поддерживает как английские буквы, так и русские)}}
Далее вас по просят ввести координаты:
Введите координаты - {сюда вводить координаты по формату: 1-0, 1-1, 1-2, 2-0 и так далее}
После чего другой игрок ходит, ходит он по такому же принципу.
Напоминаю: побеждает тот, кто первым соберёт три в ряд, удачи Вам!''')
space_string = input('Нажмите на Enter что бы начать играть!\n~~~~~~~~~~~~')


def start():  # объявление игрового поля
    start_place = [['  0 1 2']]
    for i in range(3):
        start_place.append(list('-' * 3))
    return start_place


start_game = start()  # присвоил переменной start_game игровое поле в виде массива


def show_map(list_start):  # функция отвечающая за отображения начального поля игры
    for i in range(len(start_game)):
        if i:
            print(i, *start_game[i])
        else:
            print(*start_game[i])


show_map(start_game)  # показываю начальное поле для лучшей ориентации игроков в игре


def game_close(basic_place, x_or_o,
               users_cords):  # "закрытый" код игры, использовал для того, что бы вносить изменения, не видимые игроку
    for i in range(len(basic_place)):
        for j in range(len(basic_place[i])):
            if users_cords[0] == i and users_cords[1] == j:
                if basic_place[i][j] in ['x', 'х', 'о', 'o']:
                    return None
                else:
                    basic_place[i][j] = x_or_o
                    return basic_place


def game_open(basic_place, x_or_o, users_cords):  # "открытый" код, вывод игрового поля, когда игрок вводит х или о
    for i in range(len(basic_place)):
        if not i:
            print(*basic_place[i])
        else:
            print(i, end=' ')
            for j in range(len(basic_place[i])):
                if users_cords[0] == i and users_cords[1] == j:
                    basic_place[i][j] = x_or_o
                    print(*basic_place[i][j], end=' ')
                else:
                    print(*basic_place[i][j], end=' ')
            print()


def winner_winner_chicken_dinner(basic_place):  # описание победы игроков
    x_symbol, count_x_diagonal, count_x_back_diagonal = ['x', 'х'], 0, 0
    o_symbol, count_o_diagonal, count_o_back_diagonal = ['o', 'о'], 0, 0
    count_all_step = 0
    for i in range(1, len(basic_place)):
        count_x_line, count_x_column = 0, 0
        count_o_line, count_o_column = 0, 0
        for j in range(len(basic_place[i])):
            if basic_place[i][j] in x_symbol or basic_place[i][j] in o_symbol:  # описание победы игроков по вертикали
                count_all_step += 1
                if basic_place[i][j] in x_symbol:
                    count_x_line += 1
                    if count_x_line == 3:
                        return ixiki()
                else:
                    count_o_line += 1
                    if count_o_line == 3:
                        return oliki()
            if basic_place[j + 1][i - 1] in x_symbol or basic_place[j + 1][
                i - 1] in o_symbol:  # описание победы игроков по горизонтали
                if basic_place[j + 1][i - 1] in x_symbol:
                    count_x_column += 1
                    if count_x_column == 3:
                        return ixiki()
                else:
                    count_o_column += 1
                    if count_o_column == 3:
                        return oliki()
            if i - 1 == j and (basic_place[i][j] in x_symbol or basic_place[i][
                j] in o_symbol):  # описание победы игроков по главной диагонали
                if basic_place[i][j] in x_symbol:
                    count_x_diagonal += 1
                    if count_x_diagonal == 3:
                        return ixiki()
                else:
                    count_o_diagonal += 1
                    if count_o_diagonal == 3:
                        return oliki()
            if j == 3 - i and (basic_place[i][j] in x_symbol or basic_place[i][
                j] in o_symbol):  # описание победы игроков по обратной диагонали
                if basic_place[i][j] in x_symbol:
                    count_x_back_diagonal += 1
                    if count_x_back_diagonal == 3:
                        return ixiki()
                else:
                    count_o_back_diagonal += 1
                    if count_o_back_diagonal == 3:
                        return oliki()
            if count_all_step == 9:  # в случае, если игроки не пришли к победе объявляется ничья
                return draw_game()


def oliki():  # рисунок Олика в случае победы
    return '''\n\n\n`````(_\````/_)
```````))``((
`````.-"""""""-.``
`/^\/``_.```_.``\/^\\
`\(```/__\`/__\```)/        <------ "Поздравляю тебя друг, ты помог мне победить, теперь я могу свободно бороздить
``\,``\o_/_\o_/``,/                 просторы вселенной, спасибо тебе!
````\````(_)````/
``````-.'==='.-'
``````__)`-`(__
`````/```~~~```\\
````/``/`````\``\\
````\`:```````;`/
`````\|==(*)==|/
``````:```````:
```````\``|``/
`````___)=|=(___
````{____/`\____}'''


def ixiki():  # рисунок Иксика в случае победы
    return '''\n\n\n╱╱╱╱╱╱┓╱╱╱┏╱╱╱╱╱╱
╱╱╱╱╱┏┻━━━┻┓╱╱╱╱╱
╱╱╱╱┏┛┏┓┊┏┓┗┓╱╱╱╱
╱╱╱┏┫┊┗┛┊┗┛┊┣┓╱╱╱           <------- Ты никогда не победишь нас, Иксиков. Мы всегда побеждаем!!!
╱╱╱┃┣━━━━━━━┫┃╱╱╱
╱╱╱╱┗━╱╱╱╱╱━┛╱╱╱╱
    '''


def draw_game():  # в случае если ничья выводится обе картинки где каждый передает сообщение друг другу
    return '''\n\n\n`````(_\````/_)
```````))``((
`````.-"""""""-.``
`/^\/``_.```_.``\/^\\
`\(```/__\`/__\```)/                                                                        ╱╱╱╱╱╱┓╱╱╱┏╱╱╱╱╱╱
``\,``\o_/_\o_/``,/        Вы достойная раса, поздравляю, отличная была игра-------->       ╱╱╱╱╱┏┻━━━┻┓╱╱╱╱╱
````\````(_)````/          <--------Спасибо тебе за игру, не нападай больше ;)              ╱╱╱┏┫┊┗┛┊┗┛┊┣┓╱╱╱
``````-.'==='.-'                                                                            ╱╱╱┃┣━━━━━━━┫┃╱╱╱
``````__)`-`(__                                                                             ╱╱╱╱┗━╱╱╱╱╱━┛╱╱╱╱
`````/```~~~```\\
````/``/`````\``\\
````\`:```````;`/
`````\|==(*)==|/
``````:```````:
```````\``|``/
`````___)=|=(___
````{____/`\____}
    '''


def user_change_symbol_and_check():  # проверка на "дурака", на случай если игрок захочет ввести не Х или О
    user_change = input('Выберите сторону Иксиков или Оликов\nВаш выбор упал на - ').lower()
    if user_change in ['x', 'х', 'o', 'о']:
        return user_change
    else:
        print('Вы ввели не правильную сторону:\nСторона Иксиков - х\nСторона Оликов - о')
        return None


some_list = []
while True:  # сам игровой процесс состоящий из всех функции выше, так же ряд проверок на "дурака"
    user_change_x_or_o = user_change_symbol_and_check()
    some_list.append(user_change_x_or_o)
    if user_change_x_or_o:
        if len(some_list) % 2 == 1 and some_list[-1] in ['x', 'х']:
            user_change_cords = list(map(int, input('Введите координаты - ').split('-')))
            if game_close(start_game, user_change_x_or_o,
                          user_change_cords):  # проверка кооридант, в случае, если координата занята Иксиком или Оликом выведет конец игры
                game_open(start_game, user_change_x_or_o, user_change_cords)
                if winner_winner_chicken_dinner(start_game):
                    print(winner_winner_chicken_dinner(start_game))
                    break
            else:
                print('Вы ввели занятую координату, попробуйте выбрать снова!')
                continue
        elif len(some_list) % 2 == 0 and some_list[-1] in ['o', 'о']:
            user_change_cords = list(map(int, input('Введите координаты - ').split('-')))
            if game_close(start_game, user_change_x_or_o,
                          user_change_cords):  # проверка кооридант, в случае, если координата занята Иксиком или Оликом выведет конец игры
                game_open(start_game, user_change_x_or_o, user_change_cords)
                if winner_winner_chicken_dinner(start_game):
                    print(winner_winner_chicken_dinner(start_game))
                    break
            else:
                print('Вы ввели занятую координату, тот кто ввёл занятую координату проигрывает')
                break
        else:
            if some_list[-1] in ['x', 'х']:  # проверка в случае если были введены два подряд x или о
                print('Тот кто ввел "Иксик" нарушил правила игры и проиграл')
                break
            else:
                print('Тот кто ввёл "Олик" нарушил правила игры и проиграл')
                break
    else:
        some_list.pop()  # удаление последнего элемента в случае если символ введен не правильно
        continue
