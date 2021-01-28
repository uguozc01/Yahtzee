import random
import re
from collections import Counter 

class Roll:
    def __init__(self):

        self._current_dice_list = []
        self._current_kept_dice = []

    #this section focuses on the rolling of dice logic.

    def roll_dice(self):
        'Returns random integer values between 1 to 6 and returns list'

        self._current_kept_dice.clear()
        self._current_dice_list = [random.randint(1,6) for die in range(0,5)]
        print (f'|  You rolled     {self._current_dice_list} !                   |')
        return self._current_dice_list

    def keep_dice(self):
        '''
        Rolls dice again depending on returned dice
        Stores the dice in a separate list which user wants to keep and Returns list
        '''        
        while True:

            keep_input = input('|  Which dice do you want to keep (E.g: 2,2,4)? ')
            print('|                                                     |')

            if keep_input:
                normalised = keep_input.replace(" ","")
                if len(normalised) > 9 or not normalised.replace(",","").isdigit() or normalised[-1] == ',' or (len(re.findall(',', normalised)) and (len(re.findall(',', normalised)) != ((len(normalised) - 1) / 2))):
                    print('Please enter correct input e.g. : 2,2,4 ')
                    continue

                elif len(normalised) <= 9 and len(normalised) >= 1 and normalised.replace(",","").isdigit() and normalised[-1] != ',':
                    split_input = normalised.split(',')
                    try:
                        split_input_int = [int(item) for item in split_input if all(0 < int(x) < 7 for x in split_input)]
                    except ValueError:
                        continue
                    else:
                        if len(split_input_int):
                            # get counts of two lists
                            count_first = Counter(self._current_dice_list) 
                            count_second = Counter(split_input_int) 
                            # check if count of elements exists in first list
                            is_entered_numbers_in_current_dice_list = all(count_second[key] <= count_first[key] for key in count_second)

                            if is_entered_numbers_in_current_dice_list:
                                # iterate through the list that user wants to keep (so remove them from current dice list)
                                [self._current_dice_list.remove(value) for value in split_input_int if value in self._current_dice_list]
                                [self._current_kept_dice.append(die) for die in split_input_int]
                            else:
                                continue
                        else:
                            continue
                    return self._current_dice_list
                else:
                    print('Welldone, you find a possibility to fail all input verification checks!')
                    continue
            else:
                # if the user press Enter without choosing any numbers, keep all:
                return self._current_dice_list

    def roll_again(self, dice_list):
        '''
        Returns current dice list.
        This time it uses the returned list after the player keeps some dice.
        '''
        self._current_dice_list = [random.randint(1,6) for die in range(0,(len(dice_list)))]
        print (f'|  You rolled     {self._current_dice_list} ! ')

        return self._current_dice_list

    def get_current_dice(self):
        'Returns the current dice as a list'

        return self._current_dice_list

    def get_dice_kept(self):
        'Returns the current dice kept as a list'

        return self._current_kept_dice

    def forced_keep(self,dice_list):
        'Forces to keep the last roll'

        for die in dice_list:
            self._current_kept_dice.append(die)

    #this section focuses on the checkup of dice values.

    def upper_calc(self,dice_list,check_value):
        '''
        This method returns the roll score which is based on single value checks (checks only an integer).
        This is for the top part of the game where you roll aces, twos etc. Returns a list
        '''
        roll_score = 0
        roll_score = sum([die for die in dice_list if die == check_value])
        return roll_score

    def lower_calc(self,dice_list,check_value):
        '''
        This method returns the roll score which is based on multiple value checks (checks multiple integer).
        This is for the lower part of the game
        '''
        roll_score = 0
        if (check_value == '2 PAIRS' and self.is_twoPairs(dice_list)) or (check_value == '3 OF A KIND' and self.is_threeKind(dice_list)) or (check_value == '4 OF A KIND' and self.is_fourKind(dice_list)) or (check_value == 'CHANCE' and self.take_aChance(dice_list)):
            roll_score = sum(dice_list)
        if check_value == 'FULL HOUSE' and self.is_fullHouse(dice_list):
            roll_score = 25
        if check_value == 'LOW STRAIGHT' and self.is_lowStraight(dice_list):
            roll_score = 30
        if check_value == 'HIGH STRAIGHT' and self.is_highStraight(dice_list):
            roll_score = 40
        if check_value == 'YAHTZEE' and self.isYahtzee(dice_list):
            roll_score = 50
        if check_value == '':
            roll_score = 0

        return roll_score

    def is_twoPairs(self, dice_list):

        dice_list.sort()
        if (dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]) or (dice_list[0] == dice_list[1] and dice_list[3] == dice_list[4]) or (dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]):
           return True
        return False

    def is_threeKind(self, dice_list):

        dice_list.sort()
        if dice_list[0] == dice_list[2] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]:
            return True
        return False

    def is_fourKind(self, dice_list):

        dice_list.sort()
        if dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
            return True
        return False

    def is_fullHouse(self,dice_list):

        dice_list.sort()

        #if the set returns 2 for the list, we might have a full house.
        if (len(set(dice_list))) != 2:
            return False

        # we have to check to differentiate it from four of a kind as it also returns 2:
        elif dice_list[0] != dice_list[3] and dice_list[1] != dice_list[4]:
            return True

        return False

    def is_lowStraight(self, dice_list):

        dice_list.sort()
        if (len(set(dice_list)) == 4 and ((dice_list[0] == 1 and  dice_list[4] == 4) or (dice_list[0] == 2 and  dice_list[4] == 5) or (dice_list[0] == 3 and  dice_list[4] == 6))) or (len(set(dice_list)) == 5 and ((dice_list[0] == 1 and dice_list[3] == 4) or (dice_list[1] == 3 and dice_list[4] == 6))):
            return True

        return False

    def is_highStraight(self, dice_list):

        dice_list.sort()
        if len(set(dice_list)) == 5 and ( (dice_list[0] == 1 and dice_list[4] == 5) or (dice_list[0] == 2 and dice_list[4] == 6) ):
            return True

        return False

    def isYahtzee(self, dice_list):

        if len(set(dice_list)) == 1:
            return True

        return False

    def take_aChance(self, dice_list):
        'no need to check anything'
        return True
