import re
import random
import time
from yahtzee_player import Player
from yahtzee_roll import Roll

def main():

    dash = '-' * 80
    under_ = '_' * 80
    spaces = ' ' * 80

    upper = {
        "1" : "ACES",
        "2" : "TWOS",
        "3" : "THREES",
        "4" : "FOURS",
        "5" : "FIVES",
        "6" : "SIXES"}
    # Create a dict comprehension to process so that we do not touch the main game dictionary.
    upper_comp = {k:v for (k,v) in upper.items()}

    lower = {
        "1" : "CHANCE",
        "2" : "2 PAIRS",
        "3" : "3 OF A KIND",
        "4" : "4 OF A KIND",
        "5" : "FULL HOUSE",
        "6" : "LOW STRAIGHT",
        "7" : "HIGH STRAIGHT",
        "8" : "YAHTZEE"}
    # Create a dict comprehension to process so that we do not touch the main game dictionary.
    # Note: Instead of using two dictionaries we can actually use only one dictionary and can use if-else inside dict comprehension to generate sub dicts..
    lower_comp = {k:v for (k,v) in lower.items()}

    # Create a player and a dice to play the game
    dice1 = Roll()
    player_name = str(input('Please enter your name by using only letters!:'))
    if player_name:
        if not player_name.replace(" ","").isalpha():
            player_name = str(input('Please enter your name by using only letters!:'))
            if player_name:
                if not player_name.replace(" ","").isalpha():
                    player_name = 'DUMMY_PLAYER'
                    player1 = Player(player_name)
                    print_wellcome = player1.logging(under_, spaces, 68)
                    print_wellcome("WELLCOME ", player_name)
                else:
                    player1 = Player(player_name)
                    print_wellcome = player1.logging(under_, spaces, 68)
                    print_wellcome("WELLCOME ", player_name)
        else:
            player1 = Player(player_name)
            print_wellcome = player1.logging(under_, spaces, 68)
            print_wellcome("WELLCOME ", player_name)
    else:
        player_name = 'DUMMY_PLAYER'
        player1 = Player(player_name)
        print_wellcome = player1.logging(under_, spaces, 68)
        print_wellcome("WELLCOME ", player_name)

    time.sleep(250 / 1000)

    # First (upper) part of the game starts here
    for i in range(len(upper)):

        print_rolling_dice = player1.logging(under_, spaces, 33)
        print_rolling_dice("ROLLING THE DICE NOW  ------------>  GAME : ", i+1)
        # 1st roll:
        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        # 2nd roll
        dice1.roll_again(keep1)
        keep2 = dice1.keep_dice()

        # 3rd roll:
        roll3 = dice1.roll_again(keep2)
        dice1.forced_keep(roll3)

        # The final roll collection of dice to check:
        final_collection = dice1.get_dice_kept()

        print_final_collection = player1.logging(under_, spaces, 54)
        print_final_collection("FINAL ROLL COLLECTION: ", final_collection)
        print_choose_game = player1.logging(dash, spaces, 62)
        print_choose_game("NOW WHICH GAME ", "DO YOU WANT TO CHOOSE?")
        player1.print_games(upper_comp)

        keep_game_no = input()

        if keep_game_no:
            if keep_game_no not in upper_comp.keys():
                print_bad_choice = player1.logging(under_, spaces, 49)
                print_bad_choice("THE CHOISE NOT IN THE LIST, ", "PLEASE CHOOSE AGAIN! ")

                player1.print_games(upper_comp)

                keep_game_no = input()
                if keep_game_no:
                    if keep_game_no not in upper_comp.keys():
                        lost_turn_value = list(upper_comp.values())[-1]
                        lost_turn_key = list(upper_comp.keys())[-1]
                        check_score1 = dice1.upper_calc(final_collection, int(lost_turn_key))
                        player1.add_rolled(lost_turn_value, check_score1)
                        player1.add_top_score(check_score1)
                        upper_comp.popitem()
                        print_lost_one_turn = player1.logging(under_, spaces, 40)
                        print_lost_one_turn("YOU NOW LOST ONE OF YOUR GAME TURNS: ", lost_turn_value)
                        continue
                    else:
                        print(f'\tYou Have Chosen  >----->  {upper_comp[keep_game_no]}\n\n')
                        item = upper_comp[keep_game_no]
                        check_score1 = dice1.upper_calc(final_collection, int(keep_game_no))
                        player1.add_rolled(item, check_score1)
                        player1.add_top_score(check_score1)
                        # Remove the played game from dict comprehension
                        upper_comp.pop(keep_game_no)
                else:
                    lost_turn_value = list(upper_comp.values())[-1]
                    lost_turn_key = list(upper_comp.keys())[-1]
                    check_score1 = dice1.upper_calc(final_collection, int(lost_turn_key))
                    player1.add_rolled(lost_turn_value, check_score1)
                    player1.add_top_score(check_score1)
                    # Remove the played game from dict comprehension
                    upper_comp.popitem()
                    print_no_choice = player1.logging(under_, spaces, 29)
                    print_no_choice("NOTHING ENTERED, YOUR LAST GAME IS NOW REMOVED, ", "REMAINING GAME LIST:")
                    player1.print_games(upper_comp)

            else:
                print(f'\tYou Have Chosen  >----->  {upper_comp[keep_game_no]}\n\n')
                item = upper_comp[keep_game_no]
                check_score1 = dice1.upper_calc(final_collection, int(keep_game_no))
                player1.add_rolled(item, check_score1)
                player1.add_top_score(check_score1)
                # Remove the played game from dict comprehension
                upper_comp.pop(keep_game_no)
        else:
            lost_turn_value = list(upper_comp.values())[-1]
            lost_turn_key = list(upper_comp.keys())[-1]
            check_score1 = dice1.upper_calc(final_collection, int(lost_turn_key))
            player1.add_rolled(lost_turn_value, check_score1)
            player1.add_top_score(check_score1)
            upper_comp.popitem()
            print_no_choice = player1.logging(under_, spaces, 29)
            print_no_choice("NOTHING ENTERED, YOUR LAST GAME IS NOW REMOVED, ", "REMAINING GAME LIST:")
            player1.print_games(upper_comp)

    player1.add_top_bonus()
    time.sleep(250 / 1000)

    # Second (bottom) part of the game starts here
    for i in range(len(lower)):

        print_rolling_dice = player1.logging(under_, spaces, 33)
        print_rolling_dice("ROLLING THE DICE NOW  ------------>  GAME : ", i+1)

        # 1st roll:
        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        # 2nd roll:
        dice1.roll_again(keep1)
        keep2 = dice1.keep_dice()

        # 3rd roll:
        roll3 = dice1.roll_again(keep2)
        dice1.forced_keep(roll3)
    
        # The final roll collection of dice to check:
        final_collection = dice1.get_dice_kept()

        print_final_collection = player1.logging(under_, spaces, 54)
        print_final_collection("FINAL ROLL COLLECTION: ", final_collection)
        print_choose_game = player1.logging(dash, spaces, 62)
        print_choose_game("NOW WHICH GAME ", "DO YOU WANT TO CHOOSE?")
        player1.print_games(lower_comp)

        keep_game_no = input()

        if keep_game_no:
            if keep_game_no not in lower_comp.keys():
                print_bad_choice = player1.logging(under_, spaces, 49)
                print_bad_choice("THE CHOISE NOT IN THE LIST, ", "PLEASE CHOOSE AGAIN! ")
                player1.print_games(lower_comp)

                keep_game_no = input()
                if keep_game_no:
                    if keep_game_no not in lower_comp.keys():
                        lost_turn_value = list(lower_comp.values())[-1]
                        check_score2 = dice1.lower_calc(final_collection, "")
                        player1.add_rolled(lost_turn_value, check_score2)
                        player1.add_bottom_score(check_score2)
                        lower_comp.popitem()
                        print_lost_one_turn = player1.logging(under_, spaces, 40)
                        print_lost_one_turn("YOU NOW LOST ONE OF YOUR GAME TURNS: ", lost_turn_value)
                        continue
                    else:
                        print(f'\tYou Have Chosen  >----->  {lower_comp[keep_game_no]}\n\n')
                        item = lower_comp[keep_game_no]
                        check_score2 = dice1.lower_calc(final_collection, item)
                        player1.add_rolled(item, check_score2)
                        player1.add_bottom_score(check_score2)
                        # Remove the played game from dict comprehension
                        lower_comp.pop(keep_game_no)
                else:
                    lost_turn_value = list(lower_comp.values())[-1]
                    check_score2 = dice1.lower_calc(final_collection, lost_turn_value)
                    player1.add_rolled(lost_turn_value, check_score2)
                    player1.add_bottom_score(check_score2)
                    lower_comp.popitem()
                    print_no_choice = player1.logging(under_, spaces, 29)
                    print_no_choice("NOTHING ENTERED, YOUR LAST GAME IS NOW REMOVED, ", "REMAINING GAME LIST:")
                    player1.print_games(lower_comp)

            else:
                print(f'\tYou Have Chosen  >----->  {lower_comp[keep_game_no]}\n\n')
                item = lower_comp[keep_game_no]
                check_score2 = dice1.lower_calc(final_collection, item)
                player1.add_rolled(item, check_score2)
                player1.add_bottom_score(check_score2)
                # Remove the played game from dict comprehension
                lower_comp.pop(keep_game_no)
        else:
            lost_turn_value = list(lower_comp.values())[-1]
            check_score2 = dice1.lower_calc(final_collection, lost_turn_value)
            player1.add_rolled(lost_turn_value, check_score2)
            player1.add_bottom_score(check_score2)
            lower_comp.popitem()
            print_no_choice = player1.logging(under_, spaces, 29)
            print_no_choice("NOTHING ENTERED, YOUR LAST GAME IS NOW REMOVED, ", "REMAINING GAME LIST:")
            player1.print_games(lower_comp)

    player1.add_bottom_bonus()
    player1.print_scoreboard()

main()
