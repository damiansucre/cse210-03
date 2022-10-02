from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.
    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self.guy = []
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        secret_word = self._puzzle._select_word()
        guess_letter = " "
        self._puzzle.draw_word_guess(guess_letter)
        self.guy = self._jumper.complete_list()
        
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Draw the jumper and writter the letter .

        Args:
            self (Director): An instance of Director.
        """
        
        print('')
        guy = self.guy
        self._jumper.draw_jumper(guy)
        self.guess_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle.draw_word_guess(self.guess_letter)
       
    def _do_updates(self):
        """Parts of the parachute are removed.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.process_guess(self.guess_letter,self.guy)
        
    def _do_outputs(self):
        """If the puzzle is solved the game is over.
        If the player has no more parachute the game is over.

        Args:
            self (Director): An instance of Director.
        """
        if self._puzzle.can_keep_guessing() == True:
            self._is_playing = False 
        
        if self._puzzle.game_over() == True:
            self._is_playing = False