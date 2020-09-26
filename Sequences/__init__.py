# Should these be their own modules?
from termcolor import colored


class Battle:
    def __init__(self, entityList):
        i = 0
        #enemy = []  # Enemy array
        enemyText = ''
        for e in entityList:
            if e.getType() == 'Player':
                player = e
            else:
                #print(f'i = {i}')
                enemy = e
                enemyText += enemy.name + ' '
                i += 1

        print('A battle has started!')
        print(f'{player.name} vs. {enemyText}')
        while player.isAlive() and enemy.isAlive():
            # print(f'{player.name} is alive: {player.isAlive()}')
            # print(f'{enemy.name} is alive: {enemy.isAlive()}')
            while True:
                print('What would you like to do?')
                print('Type opt for options')
                answer = input('> ')
                if answer == 'opt':
                    print('a = Perform attack')
                    print('r = Run')
                    #print('w = View equipped weapon')
                    #print('ar = View equipped armor')
                elif answer == 'a' or answer == 'r':
                    break
                else:
                    print('Invalid input')

            if answer == 'r':
                print('You ran away!')
                break

            if answer == 'a':
                pAtk = player.attack()
                enemy.loseHP(pAtk)
                print(f'{player.name} attacked')
                print(colored(f'{pAtk} damage', 'red'))
                print(f"{enemy.name}'s HP = {enemy.hp}")

                if not enemy.isAlive():
                    print(f'You dealt a fatal blow to {enemy.name}!')
                    break

            eAtk = enemy.attack()
            player.loseHP(eAtk)
            print(f'{enemy.name} attacked')
            print(colored(f'{eAtk} damage', 'red'))
            print(f"{player.name}'s HP = {player.hp}")

        if player.isAlive() and not answer == 'r':
            print('You won the battle!')

        self.stats()

    def stats(self):
        print('This will display battle statistics in the future!')


class Respawn:
    pass