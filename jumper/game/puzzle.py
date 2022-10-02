import random
from game.jumper import Jumper
class Puzzle:
    """The puzzle is a secret word randomly chosen from a list.  
    
    Attributes:
        _word_list (string): a word is chosen from the list.
    """
    def __init__(self):  
        """Constructs a hide word.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._word_list = ["cat", "table", "horse"]
        self._word_selected = ""
        self._word_guess = ["_ "] * len(self._word_selected)
        self._word_new_word = ""
        self._jumper = Jumper()
        self.mistakes = 0
        
    
    def _select_word(self):
        #The puzzle is a secret word randomly chosen from a list.
        self._word_selected = random.choice(self._word_list)
        return self._word_selected

    def draw_word_guess(self, guess_letter):
        #If the guess is correct, the letter is revealed.
        self._word_new_word += guess_letter
        self.flag = False
        self.failure=0
        for i in self._word_selected:
            if i in self._word_new_word:
                print (i, end ="")
            else:
                print("_", end="")
                self.failure +=1
        if self.failure == 0:
            self.flag = True
            print ("\nyou win!!!")
    
    def process_guess(self,guess_letter,guy):
        #If the player has no more parachute the game is over.
        if guess_letter not in self._word_selected:
            self._jumper.eliminate_element(guy)
            self.mistakes += 1
        if self.mistakes == 4:
            self._jumper.draw_jumper_over()
            self.flag = True
            print ("\nyou lost!!!")

    def can_keep_guessing(self):
         if self.flag == True:
            return True

    def game_over(self):
         if self.flag == True:
            return True
        