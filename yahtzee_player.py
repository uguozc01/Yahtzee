class Player:
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
        'Printing all the values in the scoreboard.'

        adjust_len = 25
        for key, value in self._scoreboard.items():
            print(f'\t{key:<{adjust_len}} : {value}')

        self._total_score = self.get_bottom_score() + self.get_top_score()

        print('\n')
        print(f'\t{"Total Upper Score":<{adjust_len}} : {self.get_top_score()}')
        print(f'\t{"Total Bottom Score":<{adjust_len}} : {self.get_bottom_score()}')
        print(f'\t{"GRAND TOTAL":<{adjust_len}} : {self._total_score}')
        print('\n')

    # Logging - Could actually use decorator to make only one method
    def create_log(self,message_log,param1,param2):
        k = param2
        print('|-----------------------------------------------------|')
        print(f'|   {message_log:<{k}}|')
        print(f'|   {param1:<{k}}|')
        print('|-----------------------------------------------------|')

    def create_log2(self,parameter1,parameter2):
        print('|_____________________________________________________|')
        print('|                                                     |')
        print(f'|   {parameter1}{parameter2}            |')
        print('|_____________________________________________________|')