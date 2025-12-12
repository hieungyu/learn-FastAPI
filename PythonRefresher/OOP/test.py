"""
Code have praticed property + setter 
"""

class Enemy_1:
    def __init__ (self, hp):
        self.__hp = hp

    @property
    def hp(self):
        return self.__hp
        

    @hp.setter
    def hp(self, value):
        if value < 0:
            print("M het HP roi do nha")
            value = 0
            # print(f'{value}')
        self.__hp =value
    
for i in range (10):
    if i % 2 == 0:
        print(i)    


z = Enemy_1 (100)
z.hp = -50
print(f'{z.hp} HP')
