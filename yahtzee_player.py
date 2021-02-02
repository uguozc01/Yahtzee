class Player:

    dash = '-' * 80
    under_ = '_' * 80
    spaces = ' ' * 80

    def __init__(self, name):

        self._name = name
        self._scoreboard = {}
        self._top_score = 0
        self._bottom_score = 0
        self._bonus_bottom = 0
        self._total_score = 0

    def add_rolled(self, rolled_type , value):
        'Adding scores to the player scoreboard'

        self._scoreboard[rolled_type] = value

    def add_top_score(self,value):
        'Adding a rolled score to the top part score.'

        self._top_score += value

    def add_top_bonus(self):
        'Checks for top part score. If it is high enough, a bonus is added to the scoreboard.'

        #keep this a variable for easy updates.
        needed_score_for_bonus = 63

        if self.get_top_score() >= needed_score_for_bonus:
            self._scoreboard['TOP_BONUS'] = 50
        else:
            self._scoreboard['TOP_BONUS'] = 0

        self._top_bonus = self._scoreboard['TOP_BONUS']

    def get_top_score(self):
        'Returning current top part score'
        
        return self._top_score

    def add_bottom_score(self,value):
        'Now calculate the bottom (2nd part) of the game score . Add a rolled score to the top part score.'

        self._bottom_score += value
    
    def add_bottom_bonus(self):
        'Checkfor bottom score. If it is high enough, a bonus is added to the scoreboard.'

        #keep this a variable for easy updates.
        needed_score_for_bonus_bottom = 80

        if self.get_bottom_score() >= needed_score_for_bonus_bottom:
            self._scoreboard['BOTTOM_BONUS'] = 100
        else:
            self._scoreboard['BOTTOM_BONUS'] = 0

        self._bottom_bonus = self._scoreboard['BOTTOM_BONUS']

    def get_bottom_score(self):
        'Returning current top part score'

        return self._bottom_score

    def print_scoreboard(self):

        print(f'|{self.dash}|')
        for key, value in self._scoreboard.items():
            print(f'|{key:>38} : {value:<39}|')
        
        self._total_score = self.get_bottom_score() + self.get_top_score()

        print(f'|{self.dash}|')
        print(f'|{"Total Upper Score":>38} : {self.get_top_score():<39}|')
        print(f'|{self.dash}|')
        print(f'|{"Total Bottom Score":>38} : {self.get_bottom_score():<39}|')
        print(f'|{self.dash}|')
        print(f'|{"GRAND TOTAL":>38} : {self._total_score:<39}|')
        print(f'|{self.under_}|')

    def logging(self, p1, p2, p3):

        def wrapper(p1, p2, m1, m2, p3):
            print(f'|{p1}|\n|{p2}|')
            print(f'|   {str(m1)}{str(m2):<{p3}}|')
            print(f'|{p1}|')
        return wrapper

    def print_games(self, game_dict):

        for key, value in game_dict.items():
            print(f'|{value:>38} : {key:<39}|')
            print(f'|{self.dash}|')
