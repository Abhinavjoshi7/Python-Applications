from actors import *
import random

class Game:
    def __init__(self, player, enemies):
        self.player  = player
        self.enemies = enemies

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print('''
            Monster Slash!!!
            Ready Player One?
            [Press Enter Key to Continue]
            ''')
        input()
    def print_line_break(self):
        print()
        print(''.rjust(30,'*'))
        print()
                   
    def play(self):
        while True:
            next_enemy = random.choice(self.enemies)
            cmd = input('You see a {}, [r]un, [a]ttack, [p]ass '. format(next_enemy.kind))
            if cmd == 'r':
                print('{} runs away'.format(self.player.name))
                print('{} heals thyself!'. format(self.player.name))
                self.player.heal()
                print(self.player.hp)
            elif cmd == 'a':
                print('{} attacks the {}'.format(self.player.name, next_enemy.kind))
                if self.player.attacks(next_enemy):
                    self.enemies.remove(next_enemy)
                else:
                    print('{} hides to plan the next move'.format(player.name))

            elif cmd == 'p':
                print('You are still thinking about your next move...')

            else:
                print("Please chose a valid option")
            
            self.print_line_break()

            if not self.enemies:
                print('You have won! Congratulations!')
                break

if __name__ == '__main__':
    
    enemies = [
        Ogre('Bob',1,1),
        Imp('Alice', 2)
    ]
    player = Player('Abhinav', 1)
    game = Game(player, enemies)
    game1 = Game(player, enemies)
    game.main()
    # game1.main()