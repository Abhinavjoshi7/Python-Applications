from random import randint

class Actor:
    def __init__(self, name, level):
        self.name = name 
        self.level = level
        self.hp = 100 * level
        
    def is_alive(self):
        return 'Actor: {}, Level: {}'.format(self.name, self.level)
    
    def get_attack_power(self):
        return randint(1,100) * self.level

    def __repr__(self):
        return ('<Actor: {} at Level {}>' .format(self.name, self.level)) 
    
    def attacks(self, other):
        raise NotImplementedError()
    
class Player(Actor):
    
    def heal(self):
        self.hp +=10
    
    def attacks(self, enemy):
        power = self.get_attack_power()
        print('{} attacks {}'.format(self.name, enemy.kind))
        print('{} has {} '.format(self.name, power))
        enemy.hp -= power
        
class Enemy(Actor):
    def __init__(self, name, level, kind):
        super().__init__(name,level) #Extends Actor class
        self.kind = kind
        
    def attacks(self, player):
        print('{} the {} attack {}'.format(self.name, self.kind, self.player))
        e_power = self.get_attack_power()
        print('{} has {} attack power'.format(self.name, e_power))
        player.hp -= e_power
    
class Ogre(Enemy):
    def __init__(self, name, level, size, ):
        super().__init__(name, level, 'Ogre')  
        self.size = size #Extends Enemy class
    #Overide the attack power 
    def get_attack_power(self):
        return randint(1,50) * self.size * self.level
        
class Imp(Enemy):
    def __init__(self, name, level):
        super().__init__(name, level, 'Imp') #Only Inherits the class  
      
    def get_attack_power(self):
        return super().get_attack_power() / 4
    
# if __name__ == '__main__' lets us execute the code only if this file solely is executed. If it is imported then this code will not run
if __name__ == '__main__':
    player = Player('Me', 1)
    print(player)
    ogre  = Ogre(name='Bob',level =1, size=1)
    print(ogre.hp)
    player.attacks(ogre)
    print(ogre.hp)
    player.heal()
    print(player.hp)