
class Jumper:
    

    def __init__(self):
        
        self._jumper_list = ["  ___  ", ' /___\ ',' \   /', '  \ /', '   O   ','  /|\ ', '  / \ ', '','^^^^^^^^']
        self._jumper_over = ['   x   ','  /|\ ', '  / \ ', '','^^^^^^^^']
        self._drawing_jumper = []
        
    def complete_list(self):
        #A word is chosen from the list
        self._drawing_jumper = list(self._jumper_list)
        return self._drawing_jumper
    
    def draw_jumper(self,guy):
        #the man with the parachute is drawn
        for i in guy:
            print(i)
        
    def eliminate_element(self, guy):
        #If the guess is incorrect, a line is cut on the player's parachute.
        guy.pop(0)

    def draw_jumper_over(self):
        
        print("")
        for i in self._jumper_over:
            print(i)