import random


class LotoCard:
    def __init__(self, name):
        self.name = name
        list_numb = [x for x in range(1, 91)]
        list_sample = random.sample(list_numb, 15)
        self.list_card = list()
        for i in range(0, 3):
            list_temp = list()
            for j in range(0, 9):
                list_temp.append('')
            self.list_card.append(list_temp)

        for i, line in enumerate(self.list_card):
            list_index = [x for x in range(0, 9)]
            for j in range(0, 5):
                spam_numb = random.choice(list_sample)
                list_sample.remove(spam_numb)
                spam_index = random.choice(list_index)
                list_index.remove(spam_index)
                self.list_card[i][spam_index] = spam_numb

    def __str__(self):
        spam = ''
        for line in self.list_card:
            for elem in line:
                if elem == '':
                    spam += str(elem) + '   '
                elif elem == '--':
                    spam += str(elem) + ' '
                elif int(elem) % 10 != 0 and int(elem) // 10 == 0:
                    spam += str(elem) + '  '
                else:
                    spam += str(elem) + ' '
            spam += '\n'
        return spam
        # return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.list_card])


class LotoGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def star_game(self):
        loto_numb = [x for x in range(1, 91)]
        start_game = True
        while start_game:
            random_keg = random.sample(loto_numb, 1)
            loto_numb.remove(random_keg[0])
            print(f'Новый бочонок: {random_keg[0]}(осталось {len(loto_numb)})')
            print(f'-------- {self.player1.name} card -------')
            print(self.player1)
            print(f'------ {self.player2.name} card -----')
            print(self.player2)
            user_answer = input('Зачеркнуть цифру? (y/n)')
            chek_numb = self.chek_numb(random_keg[0])
            if (chek_numb == True and user_answer == 'y') or (chek_numb == False and user_answer == 'n'):
                self.cross_out(random_keg[0])
            else:
                print('Вы проиграли')
                start_game = False

    def chek_numb(self, numb):
        for line in self.player1.list_card:
            for el in line:
                if el == numb:
                    return True
        return False

    def cross_out(self, numb):
        for i, line in enumerate(self.player1.list_card):
            for j, el in enumerate(line):
                if el == numb:
                    self.player1.list_card[i][j] = '--'
                    break

        for i, line in enumerate(self.player2.list_card):
            for j, el in enumerate(line):
                if el == numb:
                    self.player2.list_card[i][j] = '--'
                    break


user_card = LotoCard('User')
comp_card = LotoCard('Computer')

game = LotoGame(user_card, comp_card)
game.star_game()
